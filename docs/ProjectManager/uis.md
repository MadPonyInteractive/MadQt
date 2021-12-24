---
layout: default
title: QDesigner Uis
parent: Project Manager
nav_order: 4
---

# QDesigner Ui files
The Ui files project page is where you can manage your project QDesigner Ui files.\
You can drag and drop ui files into this page but keep in mind that any qrc and
custom widget references will be replaced with the project qrc files and promoted widgets.

![image](https://user-images.githubusercontent.com/30872066/146858067-7c3db91f-829e-41bb-acb0-bd7682de58e1.png)

### Creating QDesigner Uis
Pressing the "New Ui" button will take you to the New Ui page.\
Here you can create QDesigner startup uis that inherit from QMainWindow or QWidget.

![image](https://user-images.githubusercontent.com/30872066/146858108-df0c359b-26de-4842-8587-7b1b20c59d33.png)

When a project is first created, it creates a file named main.py found in the dev folder.\
This file contains some information and starter code to run your app right out of the box.\
In main.py file there's a reference to a ui named "MainWindow".
```python
from PySide6.QtWidgets import QApplication
import sys

from gui import MainWindow# <<<- THIS REFERENCE

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow.Ui()# <<<- AND THIS REFERENCE
    window.show()
    sys.exit(app.exec())
```
So if you name your main ui something else you will need to edit the references made in
the main.py file.

Notice how we access uis in the code above.\
We first need to import them from the "gui" folder
```python
from gui import MyAwesomeGui
```
And the we can access them by initializing the .Ui() method
```python
ready_to_go_ui = MyAwesomeGui.Ui()
```
Once that is done, you can access its elements
```python
ready_to_go_ui.pushButton.clicked.connect()
```
#### You can create as many uis as you like for you application!

Once you have Uis populating your ui page, you can double click to open
them in QDesigner or drag drop them into QDesigner(faster).

![QDesnMadQt](https://user-images.githubusercontent.com/30872066/146858156-83f69b13-1cd5-4565-b8be-6c46fa49c5cb.png)

When you make changes in QDesigner and come back to MadQt Project Manager\
you should press the "Refresh" button to have those changes reflected.

### Sub-classing
The main.py has a sub-classing example at the end.\
Notice we sub class MainWindow.Ui not QMainWindow.\
This is so that we can then access our ui by simply calling self.ui

Also notice how we can access our custom widgets by getting them from
the widgets folder.

```python
from PySide6.QtWidgets import QApplication
import sys
# Getting custom widget class "Button"
# From custom widget module "button"
from widgets.button import Button
from gui import MainWindow

class MyApp(MainWindow.Ui):# <<< - sub-classing ui
    # Here "self" is a QMainWindow because we created
    # a ui that inherits from QMainWindow
    # And self.ui is the initialized ui
    def __init__(self):
        super().__init__()
        print(self.ui.centralwidget)# <<< - accessing ui
        self.button = Button()# <<< - accessing custom widget class
        self.setCentralWidget(self.button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
```
