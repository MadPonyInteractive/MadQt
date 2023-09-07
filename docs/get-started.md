---
layout: default
title: Getting Started
nav_order: 1
---

# Getting Started

***

#### Python
MadQt is a python package, this means you will need to have python installed.

[Download and install Python](https://www.python.org/downloads/)

##### We prioritized the usage of higher versions of python!

- MadQt uses PySide6.

- PySide6 recommends the usage of Python 3.7 for maximum compatibility.

- When using higher versions of python with PySide 6.5 and over, 
certain features of PySide6 will not work properly, 
like multiple class inheritance in certain situations.

For this reason we limited the PySide6 version to 6.4.3 until the PySide6 team
bumps its python compatibility. This way we can use python 3.9 and over.

<!-- ##### If you already have PySide6 6.5.0 installed, you can downgrade it by running the following command:
```bash
pip install PySide6==6.4.3
``` -->
***

#### Pip
MadQt is a pip package, this means you will need to have pip installed
in order to install MadQt.

[Installing Pip](https://pip.pypa.io/en/stable/installation/)


***

Once you have Python and pip installed in your system you can
install and update MadQt from a command line.

### Install
```python
pip install MadQt
```

### Update
```python
pip install --upgrade MadQt
```

***

### Dependencies
Apart from python, the dependencies bellow will automatically be
installed or updated once you install MadQt via pip.

```python
Python >= 3.9
PySide6 >= 6.0.0, <= 6.4.3
Pillow >= 8.3.0
pyinstaller >= 4.7
```

***

### Checking installation

#### From a python script.py
```python
import MadQt
print("MadQt version:", MadQt.__version__)
```

#### From a python environment
```python
import MadQt
MadQt.__version__
```
***

### Unlocking QtDesigner Plugins
Importing MadQt or any module from it will unlock it's plugins in QtDesigner \
You only have to do it once so that MadQt can create a permanent environment variable.
```python
import MadQt
```

If you are using a virtual environment like "pyenv", in order to access the plugins
in QtDesigner, you will have to run QtDesigner from the virtual environment.

pyenv example:
```python
pyenv exec path/to/env/Lib/site-packages/PySide6/designer.exe
```