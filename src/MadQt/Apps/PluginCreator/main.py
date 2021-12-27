from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6, os, shutil, webbrowser, tempfile, subprocess, sys, fileinput
import xml.etree.ElementTree as xml
import MadQt
from MadQt import Tools as Mt

# give this to users for them to create a shortcut
# https://pypi.org/project/psgshortcut/

# pyside6-uic gui.ui -o gui.py
# pyside6-rcc resources.qrc -o resources_rc.py

# To use only in development
from pyside6_loader import PySide6Ui
PySide6Ui('gui.ui').toPy()

import gui

def isTemp(path):
    temp_dir = os.path.join(tempfile.gettempdir(),'MadQt')
    return temp_dir in path

def tempDir():
    """
        returns the temp directory
        if it doesn't exist, it creates it
    """
    temp_dir = os.path.join(tempfile.gettempdir(),'MadQt')
    if not os.path.isdir(temp_dir): os.mkdir(temp_dir)
    return temp_dir

class ThreadF(QThread):
    # Basic Worker Thread for PyQt
    # Usage: ThreadF(parent,myFunctionName,*args,**kwargs)
    def __init__(self, parent=None, func=None, *args, **kwargs):
        QThread.__init__(self, parent)
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.start()
    def run(self):
        self.func(self.parent(),*self.args,**self.kwargs)
        self.quit()

class App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowMaximizeButtonHint|Qt.WindowMinimizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.selectedIcon=None
        self.threads = []
        self.prevGeo = self.geometry()
        self.settings = QSettings("Mad Pony Interactive", "MadQt | Plugin Maker")
        self.initUi()
        self.readWindowSettings()

    # Ui Methods
    def thread(f):
        def wrapp(self, *a, **kw):
            return self.threads.append(ThreadF(self,f,*a,**kw))
        return wrapp

    def saveWindowSettings(self):
        self.settings.beginGroup("MainWindow")
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        self.settings.endGroup()

    def readWindowSettings(self):
        self.settings.beginGroup("MainWindow")
        geometry = self.settings.value("geometry", QByteArray())
        state = self.settings.value("windowState", QByteArray())
        if not geometry.isEmpty():
            self.restoreGeometry(geometry)
            self.restoreState(state)
        self.settings.endGroup()

    def closeEvent(self, event):
        self.saveWindowSettings()
        [thread.terminate() for thread in self.threads if thread.isRunning()]
        # delete temp files
        for file in os.listdir(tempDir()):
            file = os.path.join(tempDir(),file)
            if os.path.isfile(file):
                os.remove(file)
        event.accept()

    def eventFilter(self, obj, event):
        # print(event.type())
        if obj.objectName() == 'header':
            if self.ui.logo.underMouse():
                if event.type() == QEvent.MouseButtonRelease:
                    webbrowser.open('https://madponyinteractive.github.io/MadQt/')
                    return True
            else:
                if event.type() == QEvent.MouseButtonDblClick:
                    self.setWindowState(self.windowState() ^ Qt.WindowFullScreen)
                    return True

                if event.type() == QEvent.MouseButtonRelease:
                    if event.globalPosition().y() < 10 and self.moved:
                        self.prevGeo = self.geometry()
                        self.showMaximized()
                        return True

                if event.type() == QEvent.MouseButtonPress:
                    self.prevMousePos = event.scenePosition()
                    self.moved = False

                if event.type() == QEvent.MouseMove:
                    if self.windowState() == Qt.WindowFullScreen\
                    or self.windowState() == Qt.WindowMaximized:
                        self.showNormal()
                        self.prevMousePos = QPointF(self.prevGeo.width()*.5,50)

                    gr=self.geometry()
                    screenPos = event.globalPosition()
                    pos = screenPos-self.prevMousePos
                    x = max(pos.x(),0)
                    y = max(pos.y(),0)
                    screen = QGuiApplication.screenAt(QPoint(x,y)).size()
                    x = min(x,screen.width()-gr.width())
                    y = min(y,screen.height()-gr.height())

                    self.move(x,y)
                    self.moved = True

                    # print(QGuiApplication.screens())
        return QMainWindow.eventFilter(self, obj, event)

    def initUi(self):
        self.ui.header.installEventFilter(self)
        self.ui.statusbar.insertPermanentWidget(0,QLabel('V.0.0.1'),0)

        properties = self.settings.value("usrInput/properties", [])
        [self.ui.propList.addItem(prop) for prop in properties]

        self.ui.pluginName.textChanged.connect(self.pluginNameChanged)

        self.ui.regOpen.clicked.connect(self.openReg)

        reg = self.settings.value("usrInput/regPath",False)
        if reg:self.ui.regPath.setText(reg)

        add = self.settings.value("usrInput/addToExisting",False)
        if add:self.ui.addToExistingCb.setChecked(add)

        self.ui.newPIconBrowse.pressed.connect(self.openImg)


    # Helper Dialogues
    def openFile(self,fType='All Files (*)',prefix=''):
        return QFileDialog.getOpenFileName(self,
                "MadQt Plugin Creator",
                prefix,
                fType, "")

    def openFolder(self,widget):
        """ Opens a file dialogue
            Sets text on provided widget
        """
        text = widget.text() if len(widget.text()) else ''
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self,
                "MadQt Plugin Creator - Select folder",
                text, options)
        if directory:
            widget.setText(directory)
            self.selectedPath = directory

    def openImg(self):
        file = self.openFile('Images (*.png *.ico *.jpg *.gif *.svg)')[0]
        if len(file):
            if '.ico' not in file:
                dest_ico = os.path.join(tempDir(),'logo.ico')
                file = Mt.createIco(file,dest_ico,self.defaultIcoSize())
            self.ui.newPIconBrowse.setPixmap(QPixmap(file))
            self.selectedIcon = file

    def labelBox(self,msg,text):
        usrInput, ok = QInputDialog.getText(self, "MadQt Plugin Creator",
            msg, QLineEdit.Normal, text)
        if ok and usrInput != '':
            return usrInput

    def defaultIcoSize(self):
        return [(32,32)]

    def openReg(self):
        if self.ui.addToExistingCb.isChecked():
            file = self.openFile('Registry File (*.py)')[0]
        else:
            file = self.openFolder(self.ui.regPath)
        if len(file):
            self.ui.regPath.setText(file)
            self.settings.setValue("usrInput/regPath",file)

    def addProperty(self):
        p_name = self.labelBox('msg','text')
        if p_name:
            properties = self.settings.value("usrInput/properties",[])
            properties.append(p_name)
            self.settings.setValue("usrInput/properties",properties)
            self.ui.propList.addItem(p_name)

    def removeProperty(self):
        properties = self.settings.value("usrInput/properties",[])
        removed = self.ui.propList.removeCurrentItem()
        for prop in properties:
            if prop == removed.text():
                properties.remove(prop)
                break
        self.settings.setValue("usrInput/properties",properties)

    def pluginNameChanged(self,text):
        self.ui.pluginName.setText(text[0].upper() + text[1:])

    def submit(self):
        pluginName=self.ui.pluginName.text()
        pluginName=pluginName if pluginName else self.ui.pluginName.placeholderText()

        QtClass=self.ui.QtClass.text()
        QtClass=QtClass if QtClass else self.ui.QtClass.placeholderText()

        x=self.ui.geoX
        y=self.ui.geoY
        w=self.ui.geoW
        h=self.ui.geoH

        properties = self.settings.value("usrInput/properties",[])

        toolTip=self.ui.tooltipIn.text()
        toolTip=toolTip if toolTip else self.ui.tooltipIn.placeholderText()

        mad_icon = os.path.join(MadQt.get_path('Templates'),'NewProject','gui','logo.ico')
        iconFile = self.selectedIcon if self.selectedIcon else mad_icon
        if not os.path.isfile(iconFile):
            self.ui.statusbar.showMessage('Error: Provided icon file not valid!')
            return

        regFile = self.ui.regPath.text()
        if not len(regFile):
            self.ui.statusbar.showMessage('Error: Provided registry file not valid!')
            return

        addToExisting=self.ui.addToExistingCb.isChecked()
        if addToExisting:
            if not os.path.isfile(regFile) or 'register' not in regFile:
                self.ui.statusbar.showMessage('Error: Provided registry file not valid!')
                return
            directory = os.path.dirname(regFile)
        else:
            if not os.path.isdir(regFile):
                self.ui.statusbar.showMessage('Error: Provided registry folder not valid!')
                return
            directory = regFile
        MadQt.addEnvPath(directory)

        group = self.ui.widgetGroup.text()
        group=group if group else self.ui.widgetGroup.placeholderText()

        isContainer = self.ui.isContainerCb.isChecked()

        # if addToExisting:
        #     shutil.copy2()
        # else


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


# def sub_classes(_cls):
#     return [cls.__name__ for cls in _cls.__subclasses__()]

# def all_subclasses(cls):
#     return set(cls.__subclasses__()).union(
#         [s for c in cls.__subclasses__() for s in all_subclasses(c)])

# print(all_subclasses(QWidget))
