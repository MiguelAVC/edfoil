import json, subprocess, tempfile, re
import numpy as np
from pathlib import Path
from scipy.interpolate import CubicSpline
from edfoil.utils.dev import resource_path
from edfoil.utils.utils import cosSpacing

# Name stripping regex
def strip_name(name:str) -> tuple[str,str]:

    m = re.match(r'^\s*([A-Za-z]+)', name)
    prefix = m.group(1) if m else ''
    rest = name[m.end():] if m else name

    # All digits from the rest
    digits = ''.join(re.findall(r'\d+', rest))

    # Is there an 'A' between digits (allowing separators before the next digit)?
    has_a_between_digits = bool(re.search(r'(?<=\d)[Aa](?=\D*\d)', rest))

    # Insert 'A' after first two digits only when appropriate
    if has_a_between_digits and len(digits) >= 3:
        body = digits[:2] + 'A' + digits[2:]
    else:
        body = digits

    return prefix, body

# --- Airfoil Class ---
class Airfoil:
    def __init__(self, name:str = '__edit__') -> None:
        self.path = None
        self.name = name
        self.xy = [] # unified upper+lower list
        self.upper = [] # for easier access
        self.lower = [] # for easier access
        self.n_points = 0
        self.family = None   # e.g. 'NACA'
        self.profile = None  # e.g. '63-206', '2412', etc.
        self.Imported = False
        self.report = None   # contents of naca.out if using Fortran backend
        
    def __str__(self) -> str:
        return 'Airfoil Object'
    
    # --- Methods ---
    
    def importCoords(self, path:str) -> None:
        coords = np.genfromtxt(path)
        filename = Path(path).stem
        self.path = path
        self.xy = coords.tolist()
        self.n_points = len(coords)
        self.family, self.profile = strip_name(filename)
        self.Imported = True
        
        if self.family and self.profile:
            self.name = f"{self.family}{self.profile}"
        else:
            self.name = self.family or self.profile
        
    def update(self,coords:list) -> None:
        self.xy = coords
        self.n_points = len(coords)
    
    def changeName(self, name:str) -> None:
        self.name = name
        
    def exportAirfoil(self, path:str) -> None:
        filepath = path + self.name + '.txt'
        with open(filepath, 'w') as file:
            for x, y in self.xy:
                line = f'{x} {y}'
                file.write(line + '\n')
    
    def plotAirfoil(self) -> None:
        import matplotlib.pyplot as plt
        font_size = 'x-large'
        x, y = zip(*self.xy)
        fig, ax = plt.subplots(figsize=(10,3))
        ax.set_title(self.name, fontsize='xx-large')
        ax.plot(x,y)
        ax.set_xlabel('x/c [-]', fontsize=font_size)
        ax.set_ylabel('y/c [-]', fontsize=font_size)
        ax.minorticks_on()
        ax.tick_params(
            axis='both', which='both', direction='in',
            top=True, right=True, zorder=10, labelsize=font_size,
        )
        ax.grid(visible=True, which='major', linestyle='-', linewidth=0.75)
        ax.axis('equal')
        plt.show()
    
    # NACA 6 series implementation (Deprecated)
    def naca6(self, profile:str, path:str, n_points:int) -> dict:
        """
        Loads NACA 6-series airfoil tabulated data, fits splines, and returns a
        list of x and y points with the desired number of points.
        Returns: [x, y] points.
        """
        
        self.path = path
        self.n_points = n_points
        self.profile = profile
        self.name = f"NACA {profile}"
        
        with open(path, 'r') as f:
            data = json.load(f)
        # Assume JSON has keys 'upper' and 'lower'
        upper = np.array(data[profile]['upper'])
        lower = np.array(data[profile]['lower'])

        # Fit CubicSplines
        cs_upper = CubicSpline(upper[:,0], upper[:,1])
        cs_lower = CubicSpline(lower[:,0], lower[:,1])

        n_half = n_points // 2 + 1
        x_upper = cosSpacing(upper[:,0].min(), upper[:,0].max(), n_half)
        x_lower = cosSpacing(lower[:,0].min(), lower[:,0].max(), n_half)

        y_upper = cs_upper(x_upper)
        y_lower = cs_lower(x_lower)
        
        # Turn to [x,y] format
        upper_points = list(zip(x_upper, y_upper))
        lower_points = list(zip(x_lower, y_lower))
        
        # XY list
        xy = np.array(upper_points + lower_points[:-1][::-1])
        xy = xy / xy.max()  # normalize to chord=1
        self.xy = [tuple(row) for row in xy]
    
    # --- Fortran Wrapper ---
    
    def naca456(self, namelist_text: str, keep_files: bool = False) -> None:
        """
        Run bundled Fortran 'naca456.exe' (at edfoil/naca456/naca456.exe),
        feed a namelist on stdin, and parse 'naca.gnu' (+ 'naca.out') into 
        the Airfoil object.
        """

        # --- fixed location (bundled with the app) ---
        exe_path = Path(resource_path('edfoil/naca456/naca456.exe'))
        
        # --- isolated temp run dir ---
        tmpdir_ctx = tempfile.TemporaryDirectory()
        try:
            tdir = Path(tmpdir_ctx.name)
            # print(tdir)  # for debugging
            (tdir / "input.txt").write_text(namelist_text, encoding="utf-8")

            try:
                proc = subprocess.run(
                    [str(exe_path)],
                    input="input.txt\n", # program expects the filename on stdin
                    cwd=tdir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,             # keep as text; Fortran writes ASCII
                    check=True
                )
            except subprocess.CalledProcessError as e:
                raise RuntimeError(
                    f"naca456 exited with code {e.returncode}\n"
                    f"--- STDOUT ---\n{e.stdout}\n"
                    f"--- STDERR ---\n{e.stderr}\n"
                    "(Check your namelist syntax and required fields.)"
                )

            gnu_path = tdir / "naca.gnu"
            out_path = tdir / "naca.out"

            if not gnu_path.exists():
                raise RuntimeError(
                    "naca.gnu was not produced by naca456.\n"
                    f"--- STDOUT ---\n{proc.stdout}\n"
                    f"--- STDERR ---\n{proc.stderr}"
                )

            # Optional report
            self.report = out_path.read_text(encoding="utf-8") if out_path.exists() else None

            # Parse coordinates
            upper = []
            lower = []
            temp_xy = upper
            for line in gnu_path.read_text(encoding="utf-8").splitlines():
                s = line.strip()
                if not s or s.startswith("#"):
                    temp_xy = lower
                    continue
                parts = s.split()
                if len(parts) >= 2:
                    try:
                        x, y = float(parts[0]), float(parts[1])
                        temp_xy.append((x, y))
                    except ValueError:
                        continue
                    
            xy = upper[::-1] + lower[1:-1]
                    
            # If Fortran output is empty
            if not xy:
                raise RuntimeError("Parsed zero coordinates from naca.gnu.")
            
            self.upper = upper
            self.lower = lower
            self.xy = xy
            self.n_points = len(xy)

            # Attempt to fill name/profile from the namelist
            name_match = re.search(r"name\s*=\s*'([^']+)'", namelist_text, flags=re.IGNORECASE)
            if name_match:
                self.family = 'NACA'
                _, self.profile = strip_name(name_match.group(1))
                self.name = f'{self.family}{self.profile}'
            
            # prof_match = re.search(r"profile\s*=\s*'([^']+)'", namelist_text, flags=re.IGNORECASE)
            # if prof_match:
            #     self.profile = prof_match.group(1)
            # else:
            #     name_digits = re.search(r"\bNACA[-\s]*([0-9\-A-Za-z]+)", self.name or "", flags=re.IGNORECASE)
            #     if name_digits:
            #         self.profile = name_digits.group(1)

            # Optionally keep artifacts in CWD (useful for debugging)
            if keep_files:
                safe = re.sub(r"\W+", "_", self.name or "naca")
                (Path.cwd() / f"{safe}_naca.gnu").write_text(gnu_path.read_text(encoding="utf-8"), encoding="utf-8")
                if out_path.exists():
                    (Path.cwd() / f"{safe}_naca.out").write_text(out_path.read_text(encoding="utf-8"), encoding="utf-8")

        finally:
            if not keep_files:
                tmpdir_ctx.cleanup()

    
    @staticmethod
    def nameinput(
        profile_code: str, 
        name: str | None = None, 
        chord: float = 1.0, 
        dencode: int = 2) -> str:
        """
        Build a NACA456 namelist from a short code:
        - 4-digit: "2412", "0012", ...
        - 6-series: "63-206", "63206", "64-415", "65A-410", ...
        """
        code = profile_code.strip().upper().replace(" ", "")

        # ---------- 4-digit ----------
        if code.isdigit() and len(code) == 4:
            d1, d2, d34 = int(code[0]), int(code[1]), int(code[2:])
            cmax = d1 / 100.0
            xmaxc  = d2 / 10.0
            toc    = d34 / 100.0
            name   = name or f"NACA {code}"
            return (
                "&NACA\n"
                f"  name    = '{name}',\n"
                "  camber  = '2',\n"
                "  profile = '4',\n"
                f"  toc     = {toc},\n"
                f"  cmax    = {cmax},\n"
                f"  xmaxc   = {xmaxc},\n"
                f"  chord   = {chord},\n"
                f"  dencode = {dencode}/\n"
            )

        # ---------- 6-series ----------
        m = re.match(r"^6(3|4|5)(A)?-?([0-9])([0-9]{2})$", code)
        if m:
            loc, Aflag, cl_digit, t_digits = m.groups()
            profile = f"6{loc}A" if Aflag else f"6{loc}"
            camber = '6M' if Aflag else '6'
            # Standard mapping used in practice:
            # 63 -> a=0.8, 64 -> a=0.6, 65 -> a=0.5
            a_map = {"3": 0.8, "4": 0.6, "5": 0.5}
            a   = a_map[loc]
            cl  = int(cl_digit) / 10.0
            toc = int(t_digits) / 100.0
            pretty = f"6{loc}{'A' if Aflag else ''}-{cl_digit}{t_digits}"
            name = name or f"NACA {pretty}"
            return (
                f"&NACA\n"
                f"  name    = '{name}',\n"
                f"  camber  = '{camber}',\n"
                f"  profile = '{profile}',\n"
                f"  cl      = {cl},\n"
                f"  toc     = {toc},\n"
                f"  a       = {a},\n"
                f"  chord   = {chord},\n"
                f"  dencode = {dencode}/\n"
            )

        raise ValueError(f"Unrecognised profile code: {profile_code}")


        
if __name__ == '__main__':
    
    test = 3
    
    if test == 1:
    
        # Test 1
        # Task: Import airfoil straight from txt file
        path = 'edfoil/airfoils/NACA63416.txt'
        # path = 'edfoil/airfoils/circle.txt'
        airfoil = Airfoil(name='example')
        airfoil.importCoords(path=path)
        airfoil.plotAirfoil()
    
    elif test == 2:
        
        # Test 2
        # Task: NACA 6 inclusion
        path = './edfoil/naca/naca_6.json'
        airfoil = Airfoil(name='NACA 63-206')
        airfoil.naca6(path=path, profile='63-206' ,n_points=100)
        airfoil.plotAirfoil()
        
    elif test == 3:
        
        # Test 3
        # Task: NACA 4 and 6 series using Fortran backend
        
        # nl = Airfoil.nameinput("63A409")
        nl = Airfoil.nameinput("63-006")
        
        foil = Airfoil("tmp")
        foil.naca456(
            nl, 
            # keep_files=True,  # keep_files=True to debug
        )
        print(foil.name, foil.profile, foil.n_points)
        foil.plotAirfoil()