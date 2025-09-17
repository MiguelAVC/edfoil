from scipy.interpolate import splrep, splev

def norm_olp(coords:tuple[tuple[float,float],...],
             x_target:list[float,],
             order:int,
             ) -> list[list,list]:
    
    # Unzip coordinates of measurements
    x, y = zip(*coords)
    
    # Linear and quadratic splines
    tck = [splrep(x, y, k=i) for i in range(1,order+1)]
    
    # Extrapolate x_target values
    y_target = [splev(x_target, x).tolist() for x in tck]
    
    return y_target, tck

if __name__ == '__main__':
    
    # Define the tuple of 3 tuples with coordinates
    coords_overlap_start = (
        (1500, 0.033),
        (2400, 0.039),
        (4200, 0.047),
    )
    
    coords_overlap_length = (
        (1500, 0.065),
        (2400, 0.066),
        (4200, 0.081),
    )
    
    # List of x-values to extrapolate
    x_values_to_extrapolate = [
        1200, 1300, 1500, 1600, 1800, 2000, 3000, 4000, 5000, 6000, 6250,
    ]
    
    olp_sta = norm_olp(
        coords = coords_overlap_start, 
        x_target = x_values_to_extrapolate,
        order = 2,
    )
    print('Overlap start:')
    print('- Linear')
    print(olp_sta[0][0])
    print('- Quadratic')
    print(olp_sta[0][1])
    
    olp_len = norm_olp(
        coords = coords_overlap_length,
        x_target = x_values_to_extrapolate,
        order = 2,
    )
    print('Overlap length:')
    print('- Linear')
    print(olp_len[0][0])
    print('- Quadratic')
    print(olp_len[0][1])