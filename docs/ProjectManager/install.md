---
layout: default
title: Running
parent: Project Manager
nav_order: 0
---

# Running MadQt Project Manager

##### Prerequisites
In order to run this application you will need to first
[install the MadQt pip package.](https://madponyinteractive.github.io/MadQt/get-started.html)

In a command line type the following
```python
MadQtProjectManager
```

You should see the MadQt Project Manager

![image](https://user-images.githubusercontent.com/30872066/146767192-5e3f2ad9-58d3-444c-a39a-3deb8d576b02.png)


### Create a executable for Windows
1 - Create a new file in a text and paste the following code
```python
@echo off
MadQtProjectManager
```
2 - Save the file as project_manager.bat

Note: Creating a shortcut from this file so that the command line window\
does not show will stop Project Manager from receiving drag drops.

### Create a shortcut for windows
[PsgShortcut](https://pypi.org/project/psgshortcut/) is a cool tool that allows for
creating windows shortcuts for python scripts.

This will create the same result as the above example but you can have a icon for it.
