# TBlade-Designer

Repository for the future TBlade-Designer software for tidal turbine blade structural modelling. To run the application follow the next steps depending on your OS. For now this is a .py file but a .exe will be delivered eventually.

## Install on Windows

Follow the next steps:

1. Clone the repository. (Open cmd in the root directory)

```bat
git clone https://github.com/MiguelAVC/TBlade-Designer.git
```

3. Install python version 3.12.2 (or 3.12) in your computer.

4. Create a python virtual environment inside the root directory. This can be done in the terminal with the following:

```bat
python -m venv .venv
```

4. Install all the required dependencies with the following commands:

```bat
.venv\Scripts\activate
```

```bat
pip install -r requirements.txt
```

5. Run main.py

```bat
python main.py
```
