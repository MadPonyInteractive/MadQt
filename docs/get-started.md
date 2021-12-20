---
layout: default
title: Getting Started
nav_order: 1
---

# Getting Started

#### Prerequisites

##### Python
MadQt was developed in a Python 3.10 environment
and not tested in Python 3.9 but should work
from version 3.9 as we refrained from using 3.10 new features.

[Download and install Python](https://www.python.org/downloads/)

##### Pip
MadQt is a pip package, this means you will need to have pip installed
in order to install MadQt.

[Installing Pip](https://pip.pypa.io/en/stable/installation/)

#### Dependencies
This dependencies will automatically be installed or updated once
you install MadQt via pip.

```
Python >= 3.9
PySide6 >= 6.0.0
Pillow >= 8.3.0
pyinstaller >= 4.7
```

#### Install via Pip
Once you have Python and pip installed in your system you can
install MadQt from a command line.

```python
pip install MadQt
```

#### Checking installation

##### From a python script.py
```python
import MadQt
print("MadQt version:", MadQt.__version__)
```

##### From a python environment
```python
import MadQt
MadQt.__version__
```
