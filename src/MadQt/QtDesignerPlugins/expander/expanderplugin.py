############################################################################
    ##
    ## Copyright (C) 2021 The Qt Company Ltd.
    ## Contact: https://www.qt.io/licensing/
    ##
    ## This file is part of the Qt for Python examples of the Qt Toolkit.
    ##
    ## $QT_BEGIN_LICENSE:BSD$
    ## Commercial License Usage
    ## Licensees holding valid commercial Qt licenses may use this file in
    ## accordance with the commercial license agreement provided with the
    ## Software or, alternatively, in accordance with the terms contained in
    ## a written agreement between you and The Qt Company. For licensing terms
    ## and conditions see https://www.qt.io/terms-conditions. For further
    ## information use the contact form at https://www.qt.io/contact-us.
    ##
    ## BSD License Usage
    ## Alternatively, you may use this file under the terms of the BSD license
    ## as follows:
    ##
    ## "Redistribution and use in source and binary forms, with or without
    ## modification, are permitted provided that the following conditions are
    ## met:
    ##   * Redistributions of source code must retain the above copyright
    ##     notice, this list of conditions and the following disclaimer.
    ##   * Redistributions in binary form must reproduce the above copyright
    ##     notice, this list of conditions and the following disclaimer in
    ##     the documentation and/or other materials provided with the
    ##     distribution.
    ##   * Neither the name of The Qt Company Ltd nor the names of its
    ##     contributors may be used to endorse or promote products derived
    ##     from this software without specific prior written permission.
    ##
    ##
    ## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    ## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    ## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    ## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    ## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    ## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    ## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    ## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    ## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    ## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    ## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
    ##
    ## $QT_END_LICENSE$
    ##
############################################################################
"""
Widget: Expander
Version: 0.0.1

Contributors: Fabio Goncalves
Email: fabiogoncalves@live.co.uk

Description: A Expandable and animated container
"""
# We use the os module to get this file's directory
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

from MadQt.Widgets import AnimPicker

# Importing from the MadQt package Widgets folder
from MadQt.Widgets import Expander

# We import any necessary PySide6 modules
from PySide6.QtCore import QObject, Slot, QEasingCurve
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLineEdit
from PySide6.QtDesigner import (QExtensionManager,
    QExtensionFactory,
    QDesignerCustomWidgetInterface,
    QPyDesignerTaskMenuExtension,
    QDesignerFormWindowInterface)

# Extension Type | Id
E_ID = {
    'TaskMenu': 'org.qt-project.Qt.Designer.TaskMenu'
}

#============================================================================#
# ExtensionFactory                                                           #
#----------------------------------------------------------------------------#
class Factory(QExtensionFactory):
    """The Extension Factory is used to register extensions"""
    def __init__(self, manager, _type):
        super().__init__(manager)
        self.type = _type

    def createExtension(self, obj, iid, parent):
        if isinstance(obj, Expander) and iid == E_ID[self.type]:
            if self.type == 'TaskMenu':return TaskMenu(obj, parent)
        return None


#============================================================================#
# TaskMenuExtension                                                          #
#----------------------------------------------------------------------------#
class TaskMenu(QPyDesignerTaskMenuExtension):
    def __init__(self, widget, parent):
        """
            This function gets called when you first
            request a menu in QtDesigner by right
            clicking on your custom widget.
        """
        super().__init__(parent)
        self._widget = widget

        # Each action is a menu entry
        # You still have to add them bellow to
        # the 'taskActions' method and connect them to a method
        self._dialogAction = QAction('Edit Animation', None)
        self._dialogAction.triggered.connect(self.popupDialog)

    def taskActions(self):
        """Adds actions to task menu"""
        return [self._dialogAction]

    def preferredEditAction(self):
        """Triggers when plugin is double clicked in QtDesigner"""
        return self._dialogAction

    @Slot()
    def popupDialog(self):
        """
            Pops up dialog

            This is just an example of how you can add a
            popup dialog to let the user further edit
            your plugin parameters.
        """
        w=self._widget
        dialog = AnimPicker(
            curve=w.curve,
            loop=False,
            duration=w.duration,
            period=w.period,
            amplitude=w.amplitude,
            overshoot=w.overshoot,
            parent=w
            )

        if dialog.exec() == QDialog.Accepted:
            self._widget.curve = dialog.curve()
            # self._widget.loop = dialog.loop()
            self._widget.duration = dialog.duration()
            self._widget.period = dialog.period()
            self._widget.amplitude = dialog.amplitude()
            self._widget.overshoot = dialog.overshoot()

            form = QDesignerFormWindowInterface.findFormWindow(w)
            if form:
                form.cursor().setWidgetProperty(w, "curve", dialog.curve())
                form.cursor().setWidgetProperty(w, "duration", dialog.duration())
                form.cursor().setWidgetProperty(w, "period", dialog.period())
                form.cursor().setWidgetProperty(w, "amplitude", dialog.amplitude())
                form.cursor().setWidgetProperty(w, "overshoot", dialog.overshoot())

#============================================================================#
# CustomWidgetPlugin                                                         #
#----------------------------------------------------------------------------#
DOM_XML = """
<ui language='c++'>
    <widget class='Expander' name='expander'/>
</ui>
"""

class ExpanderPlugin(QDesignerCustomWidgetInterface):
    def __init__(self):
        super().__init__()
        self._form_editor = None

    def createWidget(self, *args, **kwargs):
        t = Expander(*args, **kwargs)
        return t

    def domXml(self):
        return DOM_XML

    def group(self):
        return 'Containers'

    def icon(self):
        imgLocation = os.path.join(CURRENT_DIR,'expander.ico')
        return QIcon(imgLocation)

    def includeFile(self):
        # Importing from the MadQt package Widgets folder
        return 'MadQt.Widgets.expander'

    def initialize(self, form_editor):
        if self.isInitialized():return
        manager = form_editor.extensionManager()
        if not manager: return
        self._form_editor = form_editor
        manager.registerExtensions(Factory(manager,'TaskMenu'), E_ID['TaskMenu'])

    def isContainer(self):
        return True

    def isInitialized(self):
        return self._form_editor is not None

    def name(self):
        return 'Expander'

    def toolTip(self):
        return 'An animated expandable container'

    def whatsThis(self):
        return self.toolTip()
