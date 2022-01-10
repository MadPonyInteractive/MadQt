---
layout: default
title: Expander
parent: Containers
grand_parent: Widgets
---

# MadQt.Widgets.Expander
#### Version: 0.0.1
A Expandable and animated container

### Contributors
Fabio Goncalves

### Contact
[GitHub Page](https://github.com/MadPonyInteractive)

### There's a [video on YouTube](https://www.youtube.com/watch?v=tbCJ9UkSh7k) to help you get started.
[![MadQt Plugin Creator](https://img.youtube.com/vi/tbCJ9UkSh7k/0.jpg)](https://www.youtube.com/watch?v=tbCJ9UkSh7k)

***

| QtDesigner Plugin? | Yes |

| Inheritance                   |
|:------------------------------|
| PySide6.QtWidgets.QWidget |

***

| Properties    |      |
|:--------------|:-----|
| curve         | int  |
| loop          | bool |
| duration      | int  |
| period        | float|
| amplitude     | float|
| overshoot     | float|
| expanded      | bool |
| animateOnHover| bool |
| animFrom      | QSize|
| animTo        | QSize|
| animateMaxWidth  | bool |
| animateMaxHeight | bool |
| animateMinWidth  | bool |
| animateMinHeight | bool |

| Property Methods |
|:----------|
|def getExpanded(bool)|
|def setExpanded(bool)|
|def getAnimateOnHover(bool)|
|def setAnimateOnHover(bool)|
|def getAnimFrom(QSize)|
|def setAnimFrom(QSize)|
|def getAnimTo(QSize)|
|def setAnimTo(QSize)|
|def getAnimateMaxWidth(bool)|
|def getAnimateMinWidth(bool)|
|def setAnimateMaxWidth(bool)|
|def setAnimateMinWidth(bool)|
|def getAnimateMaxHeight(bool)|
|def getAnimateMinHeight(bool)|
|def setAnimateMaxHeight(bool)|
|def setAnimateMinHeight(bool)|

| Signals |
|:----------|
|maxWidthChanged(int)|
|minWidthChanged(int)|
|maxHeightChanged(int)|
|minHeightChanged(int)|

| Slots |
|:----------|
|setAnimFrom(QSize)|
|setAnimTo(QSize)|
|setExpanded(bool)|
|setAnimateOnHover(bool)|

***

## Detailed Description
With this container you can easily animate any widget even within QtDesigner.\
It animates the maximumWidth and minimumWidth properties and you can
use the setAnimFrom and setAnimTo slots to set these.

You can use the provided signals to do other things in therms of animation.

The setExpanded method can be used to trigger the animation and the setAnimateOnHover
to trigger animations when the container is hovered with the mouse.


```python
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from MadQt.Widgets import Expander

# Construct application
app = QApplication(sys.argv)

# Create QWidget
window = QWidget()
window.setMinimumWidth(260)

# Create layout
QHBoxLayout(window)

# Create a label
label = QLabel('  Hello  ')
label.setStyleSheet("background-color:gray;")

# Construct an Expander widget
expander = Expander()

# Setting properties
expander.curve = QEasingCurve.OutCubic
expander.duration = 300

# Set stylesheet
expander.setStyleSheet("background-color:gray;")

# Set Expander layout
QVBoxLayout(expander)
expander.layout().setContentsMargins(0,0,0,0)

# Add widgets to main widget layout
expander.layout().addWidget(QLabel('Expandable'))
window.layout().addWidget(label)
window.layout().addWidget(expander)

# Show and execute app
window.show()
sys.exit(app.exec())
```

