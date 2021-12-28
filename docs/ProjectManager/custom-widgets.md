---
layout: default
title: Custom Widgets
parent: Project Manager
nav_order: 5
---

# Custom Widgets
Custom Widgets as classes that inherit from supported promote able classes
in QDesigner.

Example:
You can code a class that inherits from QPushButton called MyButton.
```python
class MyButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
```
Then in QDesigner you can add a button and promote it to your custom class.

#### MadQt Project Manager makes this easy
You can drag and drop existing custom widgets .py modules into the Widgets list
and the app will automatically detect promote able classes and display them.

![image](https://user-images.githubusercontent.com/30872066/146861650-5b9392ee-0c10-4af8-b3a3-0bdd897df5cb.png)

Keep in mind that when editing your modules you will need to press the "Refresh" button
to see your changes reflected in Project Manager.

***

Another way to add custom widget modules is by simply clicking on the "New Module" button.\
This will take you to the "New Custom Widget" page where you can
create .py template files for you to get started coding your subclass.

![image](https://user-images.githubusercontent.com/30872066/146861676-4cdd5379-a8a0-4719-a2fe-0e0689578aff.png)

If you right click on a module(Custom Widget) you can then choose "Add Class"\
this will append the new class to the end of the Custom Widget module.

### Opening for coding
Double clicking on a class will open sublime text and go to that line of code.\
If you don't use sublime, no problem, you can drag and drop modules to any text editor or IDE.


Final Note:
```
Just like images and qrc files are automatically added to
all ui files custom widgets have the same behavior.
```
