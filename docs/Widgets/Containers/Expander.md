---
layout: default
title: Expander
parent: Containers
grand_parent: Widgets
---

# MadQt.Widgets.Expander
#### Version: 0.0.1
A QPushButton with a hovered state and text

### Contributors
Fabio Goncalves

### Contact
[GitHub Page](https://github.com/MadPonyInteractive)

| QtDesigner Plugin? | Yes |

| Inheritance                   |
|:------------------------------|
| PySide6.QtWidgets.QPushButton |

***

| Attributes    |      |
|:--------------|:-----|
| defaultText   | str  |
| hoveredText   | str  |
| hovered       | bool |

| Methods |
|:----------|
|def [setHoveredText()](HtButton.html#sethoveredtext)|
|def [getHoveredText()](HtButton.html#gethoveredtext)|
|def [setDefaultText()](HtButton.html#setdefaulttext)|
|def [getDefaultText()](HtButton.html#getdefaulttext)|
|def [getHovered()](HtButton.html#gethovered)|

***

## Detailed Description
HtButton is a handy little button that uses the enterEvent and the leaveEvent
to set a property (hovered) based on if the button is hovered by the mouse.

I also allows for setting text for when the button is hovered.

```python
from MadQt.Widgets import HtButton
button = HtButton()
button.setDefaultText("Who's there?")
button.setHoveredText("It's me, MARIO!")
```

***

### setHoveredText
* Parameters
    * **new_hoveredText** - `str`

Sets the text to display when the button is hovered. |

***

### getHoveredText
* Return type
    * `str`

Returns text displayed when button is hovered. |

***

### setDefaultText
* Parameters
    * **new_defaultText** - `str`

Sets the text to display when the button is not hovered. |

***

### getDefaultText
* Return type
    * `str`

Returns text displayed when button is not hovered. |

***

### getHovered
* Return type
    * `bool`

Returns True if button is hovered. |
