---
layout: default
title: Creating an Executable
parent: Project Manager
nav_order: 6
---

# Creating an Executable
This is really a simply process but depending on what you do in your code
it can go very wrong.

Note:

MadQt Project Manager uses pyinstaller in the background to do this, so it
is advisable to read trough pyinstaller documentation before structuring
your scripts. The usual issues are due to unsupported imports, badly formatted
paths and files that should have been included.

Navigate to the Executable page within your project

img

Notice the "Arguments" field already containing some popular arguments for pyinstaller.\
You can edit this as you wish.

Press the "Create Executable" button and patiently wait.\
When finished it should display the folder where your executable file is located at.\
Navigate to it and run it.

You can press the ? button to visit [pyintaller documentation](https://pyinstaller.readthedocs.io/en/stable/operating-mode.html).
