# EdFoil

[![Version](https://img.shields.io/github/v/release/miguelavc/edfoil)](https://github.com/miguelavc/edfoil/releases)
[![Release Date](https://img.shields.io/github/release-date/miguelavc/edfoil)](https://github.com/miguelavc/edfoil/releases)
![Commits](https://img.shields.io/github/commit-activity/t/miguelavc/edfoil)
![Read the Docs](https://img.shields.io/readthedocs/edfoil)

Repository for the future EdFoil software (codename: edfoil) for tidal turbine blade structural modelling. To run the application follow the next steps depending on your OS. For now this is a .py file but a .exe will be delivered eventually.

> [!NOTE]  
> This has only been tested on Windows 10/11.
> Compatibility is expected for Windows 7/8.

## Install on Windows

### Pre-Requirements

- Git installed (Any version)
- Python installed on the system (version 3.12.2 or 3.12)

### Software Installation

Follow the next steps:

1. Clone the repository. (Open cmd in the root directory)

```bat
git clone https://github.com/MiguelAVC/edfoil.git
```

2. Create a python virtual environment inside the root directory. This can be done in the terminal with the following:

```bat
python -m venv .venv
```

3. Install all the required dependencies with the following commands:

```bat
.venv\Scripts\activate
```

```bat
pip install -r requirements.txt
```

4. Run main.py

```bat
python main.py
```

## Bugs

> [!NOTE]  
> Submitting a bug report starts a collaboration. To help us help you, please:  
> - Stay available to answer questions or provide clarifications if needed  
> - Test and confirm fixes in your own environment when a pull request (PR) is created for your issue 
