---
layout: default
title: Plugin Creator
nav_order: 3
---
# MadQt Plugin Creator
A gui application for creating QtDesigner python plugins.


##### Prerequisites
In order to run this application you will need to first
[install the MadQt pip package.](https://madponyinteractive.github.io/MadQt/get-started.html)

In a command line type the following
```python
MadQtPluginCreator
```

You should see the MadQt Project Manager

![image](https://user-images.githubusercontent.com/30872066/147564757-4022a05d-09b1-46f1-ab56-04056f3b8a38.png)


***

### Single registry file for multiple plugins
If you would like to create a file to register multiple plugins with an unique name
create a python file that starts with the word "register" for example: \
- register_jimmy_plugins.py

In the file paste the following code:
```python
#EXTRA_IMPORTS#

from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection
if __name__ == '__main__':
```
You can now create multiple plugins and add them to register_jimmy_plugins.py for
multiple registration in a single file.

When creating a new plugin check the "Add to Existing" checkbox, press
the browse button next to it and select register_jimmy_plugins.py.

***

### Create a executable for Windows
1 - Create a new file in a text editor and paste the following code
```python
@echo off
MadQtPluginCreator
```
2 - Save the file as PluginCreator.bat

Note: Creating a shortcut from this file so that the command line window\
does not show will stop Project Manager from receiving drag drops.

### Create a shortcut for windows
[PsgShortcut](https://pypi.org/project/psgshortcut/) is a cool tool that allows for
creating windows shortcuts for python scripts.

This will create the same result as the above example but you can have a icon for it.
