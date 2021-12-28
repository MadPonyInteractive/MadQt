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
# from pyside6_loader import PySide6Ui
# PySide6Ui('gui.ui').toPy()

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

class ParamDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Add Property')
        layout = QVBoxLayout(self)

        self._prop_name = QLineEdit(self)
        self._prop_name.setPlaceholderText('propertyName')
        self._prop_name.setToolTip('Property Name')
        self._prop_type = QComboBox(self)
        self._prop_type.setToolTip('Property Type')
        self._prop_type.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self._prop_type.addItems(['str','int','float','bool'])
        self._prop_default = QLineEdit(self)
        self._prop_default.setPlaceholderText("None")
        self._prop_default.setToolTip('Default value')

        layout.addWidget(self._prop_name)
        layout.addWidget(self._prop_type)
        layout.addWidget(self._prop_default)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout.addWidget(button_box)



class App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowMaximizeButtonHint|Qt.WindowMinimizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.selectedIcon=None
        self.threads = []
        self.properties = []
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

        self.ui.pluginName.textChanged.connect(self.pluginNameChanged)
        self.ui.QtClass.textChanged.connect(self.qtClassChanged)

        self.ui.regOpen.clicked.connect(self.openReg)

        reg = self.settings.value("usrInput/regPath",False)
        if reg:self.ui.regPath.setText(reg)

        add = self.settings.value("usrInput/addToExisting",False)
        if add:self.ui.addToExistingCb.setChecked(add)

        self.ui.newPIconBrowse.pressed.connect(self.openImg)

        self.ui.createPluginBtn.clicked.connect(self.submit)


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
            self.ui.newPIcon.setPixmap(QPixmap(file))
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
        if file:
            self.ui.regPath.setText(file)
            self.settings.setValue("usrInput/regPath",file)

    def addProperty(self):
        dialog = ParamDialog(self)
        if dialog.exec() == QDialog.Accepted:
            p_name=dialog._prop_name.text()
            p_type=dialog._prop_type.currentText()
            p_default=dialog._prop_default.text() or 'None'
            if not p_name:return
            prop = f"{p_name}({p_type}) = {p_default}"
            self.ui.propList.addItem(prop)
            self.properties.append({
                'name':p_name,
                'type':p_type,
                'default':p_default
                })

    def removeProperty(self):
        removed = self.ui.propList.removeCurrentItem()
        for prop in self.properties:
            if f"{prop['name']}({prop['type']}) = {prop['default']}" == removed.text():
                self.properties.remove(prop)
                break

    def pluginNameChanged(self,text):
        if text:self.ui.pluginName.setText(Mt.cleanString(text[0].upper() + text[1:]))

    def qtClassChanged(self,text):
        if text:
            if text[0] != 'Q':
                self.ui.QtClass.setText('Q' + text[1:])

    def submit(self):
        self.ui.statusbar.showMessage('Getting things ready...')

        pluginName=self.ui.pluginName.text()
        pluginName=pluginName or self.ui.pluginName.placeholderText()

        QtClass=self.ui.QtClass.text()
        QtClass=QtClass or self.ui.QtClass.placeholderText()

        x=self.ui.geoX
        y=self.ui.geoY
        w=self.ui.geoW
        h=self.ui.geoH

        toolTip=self.ui.tooltipIn.text()
        toolTip=toolTip if toolTip else self.ui.tooltipIn.placeholderText()

        mad_icon = os.path.join(MadQt.get_path('Templates'),'NewProject','gui','logo.ico')
        iconFile = self.selectedIcon or mad_icon
        if not os.path.isfile(iconFile):
            self.ui.statusbar.showMessage('Error: Provided icon file not valid!')
            return

        regFile = self.ui.regPath.text()
        if not regFile:
            self.ui.statusbar.showMessage('Error: Provided registry file not valid!')
            return

        addToExisting=self.ui.addToExistingCb.isChecked()
        if addToExisting:
            if not os.path.isfile(regFile) or 'register' not in regFile:
                self.ui.statusbar.showMessage('Error: Provided registry file not valid! Must start with "register"')
                return
            directory = os.path.dirname(regFile)
        else:
            if not os.path.isdir(regFile):
                self.ui.statusbar.showMessage('Error: Provided registry folder not valid!')
                return
            directory = regFile
            regFile = os.path.join(directory,f"register_{pluginName.lower()}.py")
        MadQt.addEnvPath(directory)

        group = self.ui.widgetGroup.text()
        group=group or self.ui.widgetGroup.placeholderText()

        isContainer = self.ui.isContainerCb.isChecked()

        addMenu = self.ui.addMenuCb.isChecked()

        def prop_type(prop):
            if prop['type']=='str':return 'string'
            elif prop['type']=='int':return 'number'
            elif prop['type']=='float':return 'double'
            elif prop['type']=='bool':return 'bool'

        # for prop in self.properties:
        #     prop['name']
        #     prop['type']
        #     prop['default']

        # copy template files ---------------------------------------------
        self.ui.statusbar.showMessage('Copying files...')
        templateDir = os.path.join(MadQt.get_path('Templates'),'NewPlugin')
        reg_file_src = os.path.join(templateDir,'register_template.py')
        widget_file_src = os.path.join(templateDir,'template.py')
        plugin_file_src = os.path.join(templateDir,'templateplugin.py')
        menu_file_src = os.path.join(templateDir,'templatetaskmenu.py')

        widget_file_dst = os.path.join(directory,pluginName.lower())
        plugin_file_dst = os.path.join(directory,pluginName.lower()+'plugin')
        menu_file_dst = os.path.join(directory,pluginName.lower()+'taskmenu')

        if addToExisting:# register
            self.ui.statusbar.showMessage('Editing registry file...')
            with open(regFile,"a") as f:
                f.write(F"    QPyDesignerCustomWidgetCollection.addCustomWidget({pluginName}Plugin())\n")
        else:# copy register template
            shutil.copy2(reg_file_src,regFile)
        shutil.copy2(widget_file_src,widget_file_dst)
        shutil.copy2(plugin_file_src,plugin_file_dst)
        if addMenu: shutil.copy2(menu_file_src,menu_file_dst)

        # Widget File-----------------------------------------------
        self.ui.statusbar.showMessage('Editing widget file...')
        for line in fileinput.input(widget_file_dst, inplace=1):
            if 'Template' in line:
                line = line.replace('Template', pluginName)
            if 'QWidget' in line:
                line = line.replace('QWidget', QtClass)
            if 'QSize(200, 200)' in line:
                line = line.replace('QSize(200, 200)', f'QSize({w}, {h})')
            if '#PROPERTY_VALUES#' in line:
                cnt=""
                for prop in self.properties:
                    if prop['type']=='str':
                        cnt+=f"        self._{prop['name']} = '{prop['default']}'\n"
                    else:
                        cnt+=f"        self._{prop['name']} = {prop['default']}\n"
                line = line.replace("        #PROPERTY_VALUES#",cnt)
            if '#PROPERTY_SETTER#' in line:
                cnt=""
                for prop in self.properties:
                    cnt+=f"    def set{prop['name'][0].upper()+prop['name'][1:]}(self, new_{prop['name']}):\n"
                    cnt+=f"        self._{prop['name']} = new_{prop['name']}\n"
                line = line.replace("    #PROPERTY_SETTER#",cnt)
            if '#PROPERTY_GETTER#' in line:
                cnt=""
                for prop in self.properties:
                    cnt+=f"    def {prop['name']}(self):\n"
                    cnt+=f"        return self._{prop['name']}\n"
                line = line.replace("    #PROPERTY_GETTER#",cnt)
            if '#PROPERTY_ASSIGN# ' in line:
                cnt=""
                for prop in self.properties:
                    cnt+=f"    {prop['name']} = Property({prop['type']}, {prop['name']}, set{prop['name'][0].upper()+prop['name'][1:]})\n"
                line = line.replace("    #PROPERTY_ASSIGN#",cnt)
            sys.stdout.write(line)

        # Plugin File-----------------------------------------------
        self.ui.statusbar.showMessage('Editing plugin file...')
        for line in fileinput.input(plugin_file_dst, inplace=1):
            if 'Template' in line:
                line = line.replace('Template', pluginName)
            if 'template' in line:
                line = line.replace('template', pluginName.lower())
            if '<x>0</x>' in line:
                line = line.replace('<x>0</x>', f'<x>{x}</x>')
            if '<y>0</y>' in line:
                line = line.replace('<y>0</y>', f'<y>{y}</y>')
            if '<width>200</width>' in line:
                line = line.replace('<width>200</width>', f'<width>{w}</width>')
            if '<height>200</height>' in line:
                line = line.replace('<height>200</height>', f'<height>{h}</height>')

            if not addMenu:
                line = line.replace("from templatetaskmenu import TemplateTaskMenuFactory","")
                line = line.replace("manager = form_editor.extensionManager()","")
                line = line.replace("iid = TemplateTaskMenuFactory.task_menu_iid()","")
                line = line.replace("manager.registerExtensions(TemplateTaskMenuFactory(manager), iid)","")

            if '#XML_PROPERTY# ' in line:
                cnt=""
                for prop in self.properties:
                    cnt+=f"        <property name='{prop['name']}'>\n"
                    cnt+=f"            <{p_type}>{prop['default']}</{prop_type(prop)}>\n"
                    cnt+=f"        </property>\n"
                line = line.replace("        #XML_PROPERTY#",cnt)

            if 'Custom Widgets' in line:
                line = line.replace('Custom Widgets', group)

            if 'fullIconPath' in line:
                line = line.replace('fullIconPath', iconFile)

            if 'return False' in line:
                line = line.replace('return False', isContainer)

            if 'tooltip' in line:
                line = line.replace('tooltip', toolTip)

            sys.stdout.write(line)

        # Task Menu File-----------------------------------------------
        if addMenu:
            self.ui.statusbar.showMessage('Editing task menu file...')
            for line in fileinput.input(menu_file_dst, inplace=1):
                if 'Template' in line:
                    line = line.replace('Template', pluginName)
                if 'template' in line:
                    line = line.replace('template', pluginName.lower())
                sys.stdout.write(line)

        self.ui.statusbar.showMessage('Plugin ready!')
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
