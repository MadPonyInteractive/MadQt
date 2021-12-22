"""
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

    WARNING: The code bellow will only work if in the
    Project Manager you have an Ui called MainWindow!
"""
from PySide6.QtWidgets import QApplication
import sys

from gui import MainWindow

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow.Ui()
    window.show()
    sys.exit(app.exec())

"""
## SUB-CLASSING EXAMPLE
## WARNING: The bellow code will only work if in the
## Project Manager you have an Ui called MainWindow
## and a module called button.py with a class Button

from PySide6.QtWidgets import QApplication
from widgets.button import Button
from gui import MainWindow
import sys

class MyApp(MainWindow.Ui):
    def __init__(self):
        super().__init__()
        # accessing ui
        print(self.ui.centralwidget)
        self.button = Button()
        self.setCentralWidget(self.button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
"""
