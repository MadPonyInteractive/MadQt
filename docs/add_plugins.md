---
layout: default
title: Adding Plugins to MadQt
nav_order: 4
---
# Adding Plugins to MadQt
A way to contribute to this project is to add your QtDesigner plugins to it. \
It is also a great way to share your code skills with the world.

You can use [MadQtPluginCreator](https://madponyinteractive.github.io/MadQt/plugin_creator.html)
to easily create a startup template for your plugin.

Make sure you have a [GitHub account](https://github.com/) and follow the following steps...

In this Tutorial we will use the already present HtButton Widget as an example.

#### STEP 1 - FORK MADQT
Go to the [MadQt GitHub page](https://github.com/MadPonyInteractive/MadQt) and press the
Fork button on the top right corner.

Once you forked it, you should have access to a fully editable copy of the package.

#### STEP 2 - EDIT YOUR WIDGET
Make sure you add information about your plugin/widget in a comment at the top of this file.
I was lazy and gave it a short description but you can make it as long as you want.
Version and description are the most important things here.
And of course email or any contact method so that companies
 can hire you for a job cuz your code rocks ;)
```python
"""
Widget: HtButton
Version: 0.0.1

Contributors: Fabio Goncalves
Email: my@email.com

Description: A QPushButton with a hovered state and text
"""
```

#### STEP 3 - ADD YOUR WIDGET
In your system create a folder that best describes your widget or simply use your widget name
if that makes sense.\
In our case we named our folder "hover_text_button"

In that folder place your widget file \
In our case it was "htbutton.py"

- hover_text_button
    - htbutton.py

Drag and drop the folder to your forked version of MadQt into the directory MadQt/Widgets/

Add a description saying something like new widget submission and press commit.

#### STEP 4 - EDIT YOUR PLUGIN
At the top of your plugin file you should add the same code as in STEP 2.
```python
"""
Widget: HtButton
Version: 0.0.1

Contributors: Fabio Goncalves
Email: my@email.com

Description: A QPushButton with a hovered state and text
"""
```

You should edit the import of your widget in your plugin like so:

Before:
```python
# Importing from the same folder
from htbutton import HtButton
```

After
```python
# Importing from the MadQt package Widgets folder
from MadQt.Widgets.hover_text_button.htbutton import HtButton
```
As you can see we are now importing from the MadQt/Widgets/hover_text_button
folder that we previously created.

Another place you need to edit the import is in the include section of your plugin

Before:
```python
    def includeFile(self):
        # Importing from the same folder
        return 'htbutton'
```

After:
```python
    def includeFile(self):
        # Importing from the MadQt package Widgets folder
        return 'MadQt.Widgets.hover_text_button.htbutton'
```

#### STEP 5 - ADD YOUR PLUGIN
Just like we did in STEP 3, create a folder in your system using the same
name as the one you used for your widget and place all necessary files in it.

Remember in our case we used "hover_text_button"

- hover_text_button
    - htbuttonplugin.py
    - htbutton.ico


Drag and drop the folder to your forked version of MadQt into the directory MadQt/QtDesignerPlugins/

Add a description saying something like new plugin submission and press commit.

#### STEP 6 - CREATE A PULL REQUEST
Navigate to the topmost folder in your forked repository and press
"New pull request" button.

On the new page that pops, press "Create pull request"

Add the details of your new plugin and press "Create pull request"

#### STEP 7 - WAIT FOR REVIEW
You are all done, now all you need is patience and wait for us to
review and accept your new plugin.

