"""
Widget: HtButton
Version: 0.0.1

Contributors: Fabio Goncalves
Email: fabiogoncalves@live.co.uk

Description: A QPushButton with a hovered state and text
"""
from PySide6.QtCore import Signal, Slot, QSize, Property
from PySide6.QtWidgets import QPushButton, QApplication

class HtButton(QPushButton):
    hoveredTextChanged = Signal(str)
    defaultTextChanged = Signal(str)
    hoverStateChanged = Signal(bool)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hovered = False
        self._defaultText = 'Hover Me'
        self._hoveredText = 'Hello'
        self.setText(self._defaultText)

    @Slot(bool)
    def setHovered(self, new_hovered):
        self._hovered = new_hovered

    @Slot(str)
    def setHoveredText(self, new_hoveredText):
        self._hoveredText = new_hoveredText
        self.hoveredTextChanged.emit(new_hoveredText)

    @Slot(str)
    def setDefaultText(self, new_defaultText):
        self._defaultText = new_defaultText
        self.defaultTextChanged.emit(new_defaultText)

    def getHovered(self):
        return self._hovered

    def getHoveredText(self):
        return self._hoveredText

    def getDefaultText(self):
        return self._defaultText

    def minimumSizeHint(self):
        return QSize(75, 24)

    def sizeHint(self):
        return QSize(75, 24)

    def enterEvent(self,event):
        self.setText(self._hoveredText)
        self._hovered = True
        self.hoverStateChanged.emit(True)

    def leaveEvent(self,event):
        self.setText(self._defaultText)
        self._hovered = False
        self.hoverStateChanged.emit(False)

    defaultText = Property(str, getDefaultText, setDefaultText)
    hoveredText = Property(str, getHoveredText, setHoveredText)
    hovered = Property(bool, getHovered, setHovered)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = HtButton()
    window.show()
    sys.exit(app.exec())
