# MadQt
#### Apps, widgets and tools for PyQt and PySide

***

MadQt is a pip package created to ease the process of using the Qt framework for python.

Qt is a powerful framework for designing Graphical User Interfaces written in c++ but
has a couple of wrappers (PyQt and PySide) that allow us to use the Python coding language.

MadQt aim is to automate and simplify many of the processes required by Qt as well
as provide custom widgets and QtDesigner plugins created to and by the community.

### [Visit the Documentation site to get started!](https://madponyinteractive.github.io/MadQt/get-started.html)


***

## Apps
### MadQt Project Manager
A gui application for organizing and managing your PyQt projects.

Coupled with QDesigner this app has many features that will help you create
and distribute PyQt apps faster.

#### Features include
- Auto compile .qrc and .ui files
- Tint and Multiply images
- Convert images to .ico format
- Easily create custom widgets and Ui's
- Automatically add custom widgets and qrc files to all exiting Ui's
- Create executable files for distribution
- Easy Sublime text integration

[![MadQt Project Manager](https://user-images.githubusercontent.com/30872066/146844155-228f4858-f0b8-4409-aec2-3a8d4a74fccb.png)](https://madponyinteractive.github.io/MadQt/ProjectManager/)

***
### MadQt Plugin Creator
A gui application for creating QtDesigner python plugins.

[![MadQt Plugin Creator](https://user-images.githubusercontent.com/30872066/147564757-4022a05d-09b1-46f1-ab56-04056f3b8a38.png)](https://madponyinteractive.github.io/MadQt/plugin_creator.html)



***

#### Visit our free PySide and PyQt course on [YouTube](https://youtube.com/playlist?list=PLuvCsqbtUSFAEmez6Tuyi2KitVcS4fLWX)

***

Support this project:

<a href="https://www.buymeacoffee.com/MadPonyInt" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" >
</a>



***
### Compatibility
MadQt is compatible with python 3.9+ 

Due to PySide6 6.5.0 having some class inheritance issues,we have to limit the PySide6 version to 6.4.3

##### If you already have PySide6 6.5.0 installed, you can downgrade it by running the following command:
```bash
pip install PySide6==6.4.3
```

##### Otherwise, simple install MadQt and it will install the correct version of PySide6 for you.
```bash
pip install MadQt
```
