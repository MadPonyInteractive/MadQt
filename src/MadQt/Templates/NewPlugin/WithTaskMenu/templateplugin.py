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
# We use the os module to get this file's directory
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

# We import our custom widget
from template import Template

# We import any necessary PySide6 modules
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLineEdit
from PySide6.QtDesigner import (QExtensionManager, QExtensionFactory,
    QDesignerCustomWidgetInterface, QPyDesignerTaskMenuExtension)

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
        if isinstance(obj, Template) and iid == E_ID[self.type]:
            if self.type == 'TaskMenu':return TaskMenu(obj, parent)
        return None


#============================================================================#
# TaskMenuExtension                                                          #
#----------------------------------------------------------------------------#
class Dialog(QDialog):
    """This is the pop up dialog"""
    def __init__(self, parent):
        super().__init__(parent)
        self._widget = parent

        layout = QVBoxLayout(self)

        self._edited = QLineEdit(self)
        layout.addWidget(self._edited)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

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
        self._dialogAction = QAction('Edit Something...', None)
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
        dialog = Dialog(self._widget)
        if dialog.exec() == QDialog.Accepted:
            # here you could do something to your plugin
            # For example if your plugin had a property
            # called 'state', you could set it by doing:

            # self._widget.state = dialog._edited.text()
            # form = QDesignerFormWindowInterface.findFormWindow(self._widget)
            # if form:
                ## We force setting the property to see the changes
                ## reflected in the property editor in real time
                # form.cursor().setWidgetProperty(self._widget, "state", dialog._edited.text())

            pass

#============================================================================#
# CustomWidgetPlugin                                                         #
#----------------------------------------------------------------------------#
DOM_XML = """
<ui language='c++'>
    <widget class='Template' name='template'/>
</ui>
"""

class TemplatePlugin(QDesignerCustomWidgetInterface):
    def __init__(self):
        super().__init__()
        self._form_editor = None

    def createWidget(self, *args, **kwargs):
        t = Template(*args, **kwargs)
        return t

    def domXml(self):
        return DOM_XML

    def group(self):
        return 'Custom Widgets'

    def icon(self):
        imgLocation = os.path.join(CURRENT_DIR,'IconName')
        return QIcon(imgLocation)

    def includeFile(self):
        return 'template'

    def initialize(self, form_editor):
        if self.isInitialized():return
        manager = form_editor.extensionManager()
        if not manager: return
        self._form_editor = form_editor
        manager.registerExtensions(Factory(manager,'TaskMenu'), E_ID['TaskMenu'])

    def isContainer(self):
        return False

    def isInitialized(self):
        return self._form_editor is not None

    def name(self):
        return 'Template'

    def toolTip(self):
        return 'tooltip'

    def whatsThis(self):
        return self.toolTip()
