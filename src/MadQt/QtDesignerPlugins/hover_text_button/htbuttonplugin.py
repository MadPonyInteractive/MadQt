"""
Widget: HtButton
Version: 0.0.1

Contributors: Fabio Goncalves
Email: fabiogoncalves@live.co.uk

Description: A QPushButton with a hovered state and text
"""
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

# Importing from the MadQt package Widgets folder
from MadQt.Widgets import HtButton

from PySide6.QtCore import QObject
from PySide6.QtGui import QIcon
from PySide6.QtDesigner import (QExtensionManager,
    QDesignerCustomWidgetInterface,
    QDesignerFormWindowInterface)

DOM_XML = """
<ui language='c++'>
    <widget class='HtButton' name='htbutton'/>
</ui>
"""

class HtButtonPlugin(QObject, QDesignerCustomWidgetInterface):
    def __init__(self):
        QObject.__init__(self)
        QDesignerCustomWidgetInterface.__init__(self)
        self._form_editor = None

    def createWidget(self, *args, **kwargs):
        widget = HtButton(*args, **kwargs)
        widget.defaultTextChanged.connect(self.defaultTextChanged)
        widget.hoverStateChanged.connect(self.hoverStateChanged)
        return widget

    def domXml(self):
        return DOM_XML

    def group(self):
        return 'Buttons'

    def icon(self):
        imgLocation = os.path.join(CURRENT_DIR,'htbutton.ico')
        return QIcon(imgLocation)

    def includeFile(self):
        # Importing from the MadQt package Widgets folder
        return 'MadQt.Widgets.htbutton'

    def initialize(self, form_editor):
        self._form_editor = form_editor

    def isContainer(self):
        return False

    def isInitialized(self):
        return self._form_editor is not None

    def name(self):
        return 'HtButton'

    def toolTip(self):
        return 'A button that changes text when hovered'

    def whatsThis(self):
        return self.toolTip()

    def defaultTextChanged(self, text):
        widget = self.sender()
        if not widget or not isinstance(widget, HtButton):return
        if not widget.isWidgetType():return
        form = QDesignerFormWindowInterface.findFormWindow(widget)
        if form:
            form.cursor().setWidgetProperty(widget, "text", text)

    def hoverStateChanged(self, state):
        widget = self.sender()
        if not widget or not isinstance(widget, HtButton):return
        if not widget.isWidgetType():return
        form = QDesignerFormWindowInterface.findFormWindow(widget)
        if form:
            form.cursor().setWidgetProperty(widget, "hovered", state)
