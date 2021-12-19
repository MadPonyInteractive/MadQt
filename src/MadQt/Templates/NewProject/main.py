from MadQt.Qt.QtWidgets import QApplication

from gui import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow.Ui()
    window.show()
    app.exec()

"""
    WARNING: The above code will only work if in the
    Project Manager you have an Ui called MainWindow!

    ## Getting PyQt or PySide classes
        Notice that the first line in this file is:
            from MadQt.Qt.QtWidgets import QApplication

        We do this because MadQt has a wrapper for PyQt and PySide
        You could also do the following:
            from PyQt6.QtWidgets import QApplication
        or:
            from PySide6.QtWidgets import QApplication

        Or you can simply keep using the MadQt wrapper and change
        framework by invoking it like so:
            import PyQt5
            from MadQt.Qt.QtWidgets import QApplication
            ## Using PyQt5 here :)

        ! The default wrapper is PySide6 !

    ## ACCESSING UIs
        Any Ui created in the MadQt Project Manager can be constructed
        here by importing them, calling they're names and adding .Ui() at the end.
        Example:
            - You created a ui in Project Manager called: MyNewUi
            - You can now initialize and use it here by calling:
                from gui import MyNewUi
                ui = MyNewUi.Ui()
                ui.show()

    ## ACCESSING WIDGETS
        You can access your custom widget modules here by importing them from
        the widgets directory.
        Example:
            - You created a custom widget module in Project Manager called myWidgets
            - Here you can access it using
                from widgets import myWidgets
            - To grab a class from it
                button = myWidgets.MyCustomButton()
"""

"""
## SUB-CLASSING EXAMPLE
## WARNING: The above code will only work if in the
## Project Manager you have an Ui called MainWindow
## and a module called myCustomButton.py with a class MyCustomButton

from MadQt.Qt.QtWidgets import QApplication
from widgets.myCustomButton import MyCustomButton
from gui import MainWindow

class MyApp(MainWindow.Ui):
    def __init__(self):
        super().__init__()
        print(self.windowTitle())
        self.button = MyCustomButton()
        self.setCentralWidget(self.button)

if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()
"""
