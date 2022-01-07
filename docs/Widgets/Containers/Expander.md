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

| QtDesigner Plugin? | Yes |

| Inheritance                   |
|:------------------------------|
| PySide6.QtWidgets.QWidget |

***

| Attributes    |      |
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
| animateWidth  | bool |
| animateHeight | bool |

| Property Methods |
|:----------|
|def getExpanded()|
|def setExpanded()|
|def getAnimateOnHover()|
|def setAnimateOnHover()|
|def getAnimFrom()|
|def setAnimFrom()|
|def getAnimTo()|
|def setAnimTo()|
|def getAnimateWidth()|
|def setAnimateWidth()|
|def getAnimateHeight()|
|def setAnimateHeight()|

***

## Detailed Description
HtButton is a handy little button that uses the enterEvent and the leaveEvent
to set a property (hovered) based on if the button is hovered by the mouse.

I also allows for setting text for when the button is hovered.

```python
from MadQt.Widgets import Expander
expander = Expander()

```
