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
# If you care about performance you can edit
# this and import only what you need
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtDesigner import *

# Extension Type | Id
E_ID = {
    'TaskMenu': 'org.qt-project.Qt.Designer.TaskMenu',
    'Container': 'org.qt-project.Qt.Designer.Container'
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
            if self.type == 'Container':return Container(obj, parent)
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

        self._checkBox = QCheckBox("Check me",self)
        self._checkBox.setChecked(self._widget.getCurrentIndex())
        layout.addWidget(self._checkBox)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def index(self):
        return self._checkBox.isChecked()

class TaskMenu(QPyDesignerTaskMenuExtension):
    def __init__(self, widget, parent):
        """
            This function gets called when you first
            request a menu in QtDesigner by right
            clicking on your custom widget.
        """
        super().__init__(parent)
        self._widget = widget

        # Each of these actions are a menu entry
        # You still have to add them bellow to
        # the 'taskActions' method and connect them to a method
        self._dialogAction = QAction('Edit Something...', None)
        self._dialogAction.triggered.connect(self.popupDialog)

        self._previousPageAction = QAction('Prev Page', None)
        self._previousPageAction.triggered.connect(self.previousPage)

        self._nextPageAction = QAction('Next Page', None)
        self._nextPageAction.triggered.connect(self.nextPage)

    def taskActions(self):
        """Adds actions to task menu"""
        return [self._dialogAction,self._previousPageAction,self._nextPageAction]

    def preferredEditAction(self):
        """Triggers when plugin is double clicked in QtDesigner"""
        return self._dialogAction

    # Action's Methods
    def popupDialog(self):
        """
            Pops up dialog

            This is just an example of how you can add a
            popup dialog to let the user further edit
            your plugin parameters.
        """
        dialog = Dialog(self._widget)
        if dialog.exec() == QDialog.Accepted:
            self._widget.setCurrentIndex(dialog.index())

    def previousPage(self):
        return self._widget.previousPage()

    def nextPage(self):
        return self._widget.nextPage()

#============================================================================#
# ContainerExtension                                                         #
#----------------------------------------------------------------------------#
class Container(QPyDesignerContainerExtension):
    """
        This class is responsible for adding the 'Insert Page'
        and 'Page' options to the QtDesigner menu.

        The methods in this class are used by QtDesigner
        to manage and retrieve pages.

        This methods should be overwritten and connected
        to your custom widget.
    """
    def __init__(self, widget, parent=None):
        """
            This function gets called when you add
            an instance of your Custom Widget to
            a ui in QtDesigner.
        """
        super().__init__(parent)
        self._widget = widget

    def canAddWidget(self):
        """QtDesigner uses this method to check if it can add a new page"""
        return True

    def canRemove(self, index):
        """QtDesigner uses this method to check if it can remove a page"""
        return self._widget.canRemovePage(index)

    def addWidget(self, page):
        """
            This is called based on the startup pages you
            add on the DOM_XML string

            It appends the given page to existent pages in QtDesigner

            You then have to figure out what to do with
            the given page within your custom widget.
        """
        self._widget.addPage(page)

    def insertWidget(self, index, page):
        """
            When you insert a page via the QtDesigner insert page
            menu, it calls this method

            'index' is based on insert after or before
            'page' is a QWidget inserted by QtDesigner

            You then have to figure out what to do with
            the given page within your custom widget.
        """
        self._widget.insertPage(index, page)

    def remove(self, index):
        """
            This method gets called when you use the menu
            in QtDesigner to remove a page.
        """
        self._widget.removePage(index)

    def currentIndex(self):
        """QtDesigner uses this method to check the currentIndex"""
        return self._widget.getCurrentIndex()

    def setCurrentIndex(self, index):
        """QtDesigner uses this method to set the currentIndex"""
        self._widget.setCurrentIndex(index)

    def widget(self, index):
        """QtDesigner uses this method to get the current page"""
        return self._widget.widget(index)

    def count(self):
        """QtDesigner uses this method to count the number of existing pages"""
        return self._widget.count()

#============================================================================#
# CustomWidgetPlugin                                                         #
#----------------------------------------------------------------------------#
DOM_XML = """
<ui language='c++'>
    <widget class='Template' name='template'>
        <widget class="QWidget" name="page" />
        <widget class="QWidget" name="page_2" />
    </widget>
    <customwidgets>
        <customwidget>
            <class>Template</class>
            <extends>QWidget</extends>
            <addpagemethod>addPage</addpagemethod>
        </customwidget>
    </customwidgets>
</ui>
"""

class TemplatePlugin(QObject, QDesignerCustomWidgetInterface):
    """
        This is our Plugin class, it is responsible to process our
        plugin registration and gets called when QtDesigner starts.

        Notice we also inherit from QObject so that bellow on
        'currentIndexChanged' and 'pageNameChanged' methods we can
        call self.sender() to figure out winch widget called the method
    """
    def __init__(self, parent=None):
        QObject.__init__(self)
        QDesignerCustomWidgetInterface.__init__(self)
        self._form_editor = None

    def createWidget(self, parent):
        widget = Template(parent)
        widget.currentIndexChanged.connect(self.currentIndexChanged)
        widget.pageNameChanged.connect(self.pageNameChanged)
        return widget

    def domXml(self):
        return DOM_XML

    def group(self):
        return 'Custom Widgets'

    def icon(self):
        imgLocation = os.path.join(CURRENT_DIR,'IconName')
        return QIcon(imgLocation)

    def includeFile(self):
        return 'template'

    def initialize(self, form_editor:QDesignerFormEditorInterface):
        if self.isInitialized():return
        manager = form_editor.extensionManager()
        if not manager: return
        self._form_editor = form_editor
        manager.registerExtensions(Factory(manager,'Container'), E_ID['Container'])
        manager.registerExtensions(Factory(manager,'TaskMenu'), E_ID['TaskMenu'])

    def isContainer(self):
        return True

    def isInitialized(self):
        return self._form_editor is not None

    def name(self):
        return 'Template'

    def toolTip(self):
        return 'tooltip'

    def whatsThis(self):
        return self.toolTip()

    def currentIndexChanged(self, index):
        widget = self.sender()
        if not widget or not isinstance(widget, Template):return
        if not widget.isWidgetType():return
        form = QDesignerFormWindowInterface.findFormWindow(widget)
        if form:
            # We force setting the currentIndex to see the changes
            # reflected in the property editor in real time
            form.cursor().setWidgetProperty(widget, "currentIndex", index)

    def pageNameChanged(self, title):
        widget = self.sender()
        if not widget or not isinstance(widget, Template):return
        if not widget.isWidgetType():return

        page = widget.widget(widget.getCurrentIndex())
        form = QDesignerFormWindowInterface.findFormWindow(page)

        if form:
            # form.cursor() == QDesignerFormWindowCursorInterface
            form.cursor().setWidgetProperty(page, "objectName", title)
