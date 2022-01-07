---
layout: default
title: AnimPicker
parent: Input Widgets
grand_parent: Widgets
---

# MadQt.Widgets.AnimPicker
#### Version: 0.0.1
AnimPicker is a QDialog based on the PySide6 QEasing animation example
that allows for a user to pick animation curves and parameters.

![image](https://user-images.githubusercontent.com/30872066/148591426-3cc8db1e-0531-4a78-baf2-21f6bd336593.png)


### Contributors
Fabio Goncalves

### Contact
[GitHub Page](https://github.com/MadPonyInteractive)

| QtDesigner Plugin? | No |

| Inheritance                   |
|:------------------------------|
| PySide6.QtWidgets.QDialog     |

***

| Methods |
|:----------|
|def [setCurve()](AnimPicker.html#setcurve)|
|def [curve()](AnimPicker.html#curve)|
|def [loop()](AnimPicker.html#loop)|
|def [duration()](AnimPicker.html#duration)|
|def [period()](AnimPicker.html#period)|
|def [amplitude()](AnimPicker.html#amplitude)|
|def [overshoot()](AnimPicker.html#overshoot)|

***

## Detailed Description
AnimPicker is a QDialog based on the PySide6 QEasing animation example
that allows for a user to pick animation curves and parameters.

You can see this dialog in action in the [Expander Plugin](https://madponyinteractive.github.io/MadQt/Widgets/Containers/Expander.html) \
Or simply by opening it's file located in MadQt/Widgets/anim_picker.py

You can use it as any other QDialog
```python
from MadQt.Widgets import AnimPicker

dialog = AnimPicker()
if dialog.exec() == QDialog.Accepted:
    print(dialog.curve())
    print(dialog.loop())
    print(dialog.duration())
    print(dialog.period())
    print(dialog.amplitude())
    print(dialog.overshoot())
```

## MadQt.Widgets.AnimPicker
* Parameters
    * **curve** - `int`
    * **loop** - `bool`
    * **duration** - `int`
    * **period** - `float`
    * **amplitude** - `float`
    * **overshoot** - `float`
    * **parent** - `QWidget`

```python
from MadQt.Widgets import AnimPicker
dialog = AnimPicker(
        curve=35,
        loop=True,
        duration=2000,
        period=None,
        amplitude=None,
        overshoot=None,
        parent=None)
```

***

### setCurve
* Parameters
    * **curve** - `int`

Sets the curve number to use. |

***

### curve
* Return type
    * `int`

Returns the curve number. |

***

### loop
* Return type
    * `bool`

Returns if loop active. |

***

### duration
* Return type
    * `int`

Returns animation duration. |

***

### period
* Return type
    * `float`

Returns animation curve period. |

***

### amplitude
* Return type
    * `float`

Returns animation curve amplitude. |

***

### overshoot
* Return type
    * `float`

Returns animation curve overshoot. |


