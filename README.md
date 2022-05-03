# Init Flask

A simple package, to initialise Flask project file structure.

# Installation

After cloning the repo, use package manager [pip](https://pip.pypa.io/en/stable/) to install init_flask:

```bash
pip install -e init_flask
```

# Usage

```bash
python -m init_flask -n <project_name>
```

# Structure

```
├── project/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
├── setup.py
└── MANIFEST.in
```
