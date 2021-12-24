from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import PySide6, os, json, shutil, webbrowser, tempfile, subprocess, sys, fileinput
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
# Globals
MadQt_Designer_Paths = []
window = None

def pySideDir():
    """returns the path to PySide6"""
    return os.path.dirname(PySide6.__file__)

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

def customWidgetModule(_class,qt_class):
    return f"""from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class {_class}({qt_class}):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)"""

def customWidgetClass(_class,qt_class):
    return f"""

class {_class}({qt_class}):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)"""


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

class Project:
    """
        If a project file is provided (.mqpm):
            it loads that project
        elif name and folder are provided:
            Copies a template project to the provided folder.

            Creates a new MadQt project JSON
            file with project information.
            ProjectName.mqpm

        If no name nor folder is provided it just inits

        class Project

        Project(name='New MadQt project',folder,ico)

        Parameters:
            name - str
            folder - str
            ico - str


        Folder Structure

        self.folder
            *.mqpm
            *.sublime-project
            dev
                main.py
                *_rc.py
                gui
                    *.ui
                    *.py
                    *.qrc
                    *.img
                widgets
                    *.py
    """
    def __init__(self,name='',folder=None,icon=None):
        self.valid=False
        if '.mqpm' in name:
            self.loadSett(name)
        else:
            self.name = 'New MadQt project' if not name else name
            self.folder = folder
            if len(name) and folder:
                self.valid = self.create(icon)

    def create(self,icon):
        """creates a new project"""
        # Copy files in template folder to self.folder/dev
        source_dir = os.path.join(MadQt.get_path('Templates'),'NewProject')
        if os.path.isdir(self.devPath()):return False
        # copy template folder
        shutil.copytree(source_dir, self.devPath(), ignore=shutil.ignore_patterns('*.ico'))
        # copy .ico file
        shutil.copyfile(icon, self.guiFile('logo.ico'))
        if isTemp(icon): os.remove(icon)
        self.icon = 'logo.ico'

        # self.compileQrc('resources.qrc')
        # Create settings file
        self.settings = {
            'name':self.name,
            'folder':self.folder,
            'date':QDateTime.currentDateTime().toString(),
            'icon': 'logo.ico',
            'uiFiles':[],
            'customWidgets':{},
            'qrcFiles':['resources.qrc'],
        }
        self.saveSett()
        return True

    def compileQrc(self,qrc):
        """compiles a qrc file"""
        src = self.guiFile(qrc)
        Mt.compileQrc(src,self.devPath())

    def devPath(self):
        """returns dev folder"""
        return os.path.join(self.folder,'dev')

    def devFile(self,file):
            """returns file in dev path"""
            return os.path.join(self.devPath(),file)

    def guiFile(self,file):
            """returns file in gui path"""
            return os.path.join(self.devPath(),'gui',file)

    def widgetFile(self,file):
        """returns file in widgets path"""
        return os.path.join(self.devPath(),'widgets',file)

    def iconPath(self):
        """returns full path and filename for project icon"""
        return self.guiFile(self.icon)

    def setIcon(self,filename):
        self.icon = self.settings['icon'] = filename
        self.saveSett()

    def file(self):
        """returns full path and filename of madqt_project.mqpm """
        if not self.folder:return None
        return os.path.join(self.folder,f'{Mt.cleanString(self.name)}.mqpm')

    def saveSett(self):
        with open(self.file(), "w") as f:
            json.dump(self.settings, f, indent=4)

    def loadSett(self,file=None):
        file = self.file() if not file else file
        if os.path.isfile(file):
            with open(file, "r") as f:
                self.settings = json.loads(f.read())
            self.valid = True
            self.name = self.settings['name']
            self.icon = self.settings['icon']
            self.folder = self.settings['folder']
            self.date = self.settings['date']
        else:
            self.valid = False

    def runApp(self):
        """run main.py"""
        if not len(self.settings['uiFiles']):return None
        os.chdir(self.devPath())
        subprocess.Popen(['python', 'main.py'],shell=True)

    def saveToNewFolder(self,folder):
        if folder in self.folder:return False
        for file in os.listdir(self.folder):
            src = os.path.join(self.folder,file)
            dst = os.path.join(folder,file)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
        self.settings['name']=self.name
        self.folder=self.settings['folder']=folder
        self.settings['date']=QDateTime.currentDateTime().toString()
        self.saveSett()
        return True

    def uiFiles(self):
        """returns generator with full path to ui files"""
        return (self.guiFile(ui) for ui in self.settings['uiFiles'])

    def qrcFiles(self):
        """returns generator with full path to qrc files"""
        return (self.guiFile(qrc) for qrc in self.settings['qrcFiles'])

    def customWidgetsFiles(self):
        """returns generator with full path to customWidgets module files"""
        return (self.widgetFile(cw) for cw in self.settings['customWidgets'].keys())

    def updateUi(self,ui_file):
        """
            Updates ui custom widgets and qrc files
            Compiles Qrc files
            Compiles py file
            Adds Ui class to compiled file:
                class Ui(QMainWindow):
                    def __init__(self):
                        super().__init__()
                        ui = Ui_MainWindow()
                        ui.setupUi(self)
        """
        plugin_locations = MadQt_Designer_Paths
        widget_folder = os.path.join(self.devPath(),'widgets')
        plugin_locations.append(widget_folder)
        ui = Mt.Ui(ui_file,plugin_locations)

        # add qrc resources
        for qrc in self.settings['qrcFiles']: ui.add_qrc(qrc)

        # add promoted widgets
        for mod, classes in self.settings['customWidgets'].items():
            for cD in classes:
                ui.add_custom_widget(cD['class'],cD['qt_class'],mod.replace('.py','.h'))

        # save/overwrite ui to place qrc includes and custom widgets
        ui.save()

        # close to compile qrc files and a py
        # version that will work right off the box
        close_dict = ui.close()

        # Copy plugins that were found in our paths
        # but are not importable to widgets folder
        for plugin_mod in close_dict['in_paths']:
            py_name = plugin_mod+'.py'
            # already in widgets folder
            if os.path.isfile(self.widgetFile(py_name)):continue
            for path in plugin_locations:
                # don't check widgets folder
                if path == widget_folder: continue
                for file in os.listdir(path):
                    if file == py_name:
                        src = os.path.join(path,file)
                        dst = os.path.join(widget_folder,file)
                        shutil.copy2(src,dst)

        # add widget folder to widgets imports
        # from myWidgets >> from widgets.myWidgets
        from_widgets = close_dict['promoted_widgets']+close_dict['in_paths']
        for line in fileinput.input(close_dict['compiled_file'], inplace=1):
            for cw in from_widgets:
                if f'from {cw} import ' in line:
                    line = line.replace(cw, 'widgets.'+cw)
            sys.stdout.write(line)

        # inform user of removed plugins and widgets
        if close_dict['removed_plugins']:

            msg = F"Missing plugins in '{os.path.basename(ui_file)}' \n\n"

            msg += F"The following plugins were removed: \n"
            for rp in close_dict['removed_plugins']:
                msg += F"- class:{rp['class']} | module:{rp['module']}\n"
            msg += F"As a consequence, widgets were removed: \n"
            for rw in close_dict['removed_widgets']:
                msg += F"- {rw['name']} \n"

            msg += F"\nQtDesigner plugins must be present either in\n"
            msg += F"Plugin Paths(in settings) or in the dev/widgets folder! \n\n"

            msg += F"To stop receiving this message: \n"
            msg += F"- ADD MISSING PLUGINS TO PLUGIN/DEV/WIDGETS \n"
            msg += F"or\n"
            msg += F"- ADD THE PLUGINS DIRECTORIES TO PLUGIN PATHS \n"
            msg += F"or\n"
            msg += F"- REMOVE MISSING PLUGINS FROM UI"
            reply = QMessageBox.information(
                window,
                "Could not import or find plugins!",
                msg
            )

    def addUi(self,file):
        """
        Copies file to dev/gui
        Adds custom widgets and qrc files to ui
        Compiles py file
        Adds ui to settings
        """
        # Copy file to dev/gui
        base = os.path.basename(file)
        dest = self.guiFile(base)
        shutil.copyfile(file, dest)

        if isTemp(file):os.remove(file)

        self.updateUi(base)

        self.settings['uiFiles'].append(base)
        self.saveSett()
        return dest

    def removeUi(self,file):
        """
        Removes ui
        Deletes ui file and compiled py file
        """
        os.remove(file)
        py_file = file.replace('.ui','.py')
        if os.path.isfile(py_file):os.remove(py_file)
        self.settings['uiFiles'].remove(os.path.basename(file))
        self.saveSett()

    def updateUis(self):
        """updates all UIs"""
        [self.updateUi(ui) for ui in self.uiFiles()]
        self.saveSett()

    def addQrc(self,basename):
        if basename in self.settings['qrcFiles']:return False
        self.settings['qrcFiles'].append(basename)
        self.updateUis()
        return True

    def createQrc(self,qrcName='resources.qrc'):
        """copies an empty qrc file from templates/Uis"""
        if qrcName in self.settings['qrcFiles']:
            pName,_=os.path.splitext(qrcName)
            qrcName = qrcName.replace(pName,pName+'_2')
        source_dir = os.path.join(MadQt.get_path('Templates'),'Uis','resources.qrc')
        shutil.copyfile(source_dir, self.guiFile(qrcName))
        self.addQrc(qrcName)
        return self.guiFile(qrcName)

class ProjectItem(QListWidgetItem):
    def __init__(self,file):
        self.file = file
        p = Project(file)
        ps = p.settings
        QListWidgetItem.__init__(self,QIcon(p.iconPath()),ps['name'])
        self.setToolTip(p.file())
        self.setStatusTip(f"Dbl click to open | Created: {ps['date']}")

class UiItem(QListWidgetItem):
    def __init__(self,file):
        self.file = file
        self.name = os.path.basename(file)
        QListWidgetItem.__init__(self,self.name)
        self.setStatusTip('Double click to open new QDesigner window or Drag and drop into QDesigner!')

class QrcFile(QTreeWidgetItem):
    def __init__(self,file,treeview):
        QTreeWidgetItem.__init__(self, treeview, type=0)
        self.file = file
        self.setText(0,os.path.basename(file))
        self.setExpanded(True)

class QrcPrefix(QTreeWidgetItem):
    def __init__(self,text,parent):
        QTreeWidgetItem.__init__(self, parent, type=1)
        self.setText(0,text)
        self.setExpanded(True)

class QrcImage(QTreeWidgetItem):
    def __init__(self,file,parent):
        QTreeWidgetItem.__init__(self, parent, type=2)
        self.file = file
        self.setText(0,os.path.basename(file))
        self.setIcon(0,QPixmap(file))
        self.setStatusTip(0,'Drag and drop into a image editor like Photoshop!')
        self.setExpanded(True)
        self.tinted = False

    def tint(self,color,_type):
        if not self.tinted:
            self.savedOriginal = os.path.join(tempDir(),os.path.basename(self.file))
            shutil.copy2(self.file,self.savedOriginal)
        Mt.tintImage(self.file,color,_type)
        self.setIcon(0,QPixmap(self.file))
        self.tinted = True

    def restore(self):
        shutil.copy2(self.savedOriginal,self.file)
        self.setIcon(0,QPixmap(self.file))

class CustomWidgetFile(QTreeWidgetItem):
    def __init__(self,file,parent):
        QTreeWidgetItem.__init__(self,parent, type=0)
        self.file = file
        self.setStatusTip(0,'Drag and drop into a text editor!')
        self.setText(0,os.path.basename(file))
        self.setExpanded(True)

class CustomWidgetClass(QTreeWidgetItem):
    def __init__(self,_class,sub_class,parent):
        QTreeWidgetItem.__init__(self,parent, type=1)
        self.setText(0,_class)
        self.setText(1,sub_class)
        self.setStatusTip(0,'Double click to open in sublime text!')
        self.setExpanded(True)

class App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowMaximizeButtonHint|Qt.WindowMinimizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.selectedPath = None
        self.selectedFile = None
        self.extraMsgWidget=None
        self.threads = []
        self.prevGeo = self.geometry()
        # self.moved = False
        self.prevMainPageindex = 0
        self.project = Project() # current project loaded
        self.initSettings()
        self.initUi()
        self.readWindowSettings()

        # def pp():print(f"Hello")
        # self.act = QAction('Make tomatoes!')
        # self.act.triggered.connect(pp)
        # self.ui.runBtn.addAction(self.act)
        # self.act.trigger()
        # print(self.ui.runBtn.actions())
        # print(self.ui.actionPotatoes)

    # Ui Methods
    def thread(f):
        def wrapp(self, *a, **kw):
            return self.threads.append(ThreadF(self,f,*a,**kw))
        return wrapp

    def refresh(self):
        self.setCursor(Qt.WaitCursor)
        self.ui.statusbar.showMessage('Refreshing...')
        prevPF = self.project
        self.project = Project()
        self.openProject()
        self.project = prevPF
        self.openProject()
        self.ui.statusbar.showMessage('Project refreshed!')
        self.setCursor(Qt.ArrowCursor)

    def initSettings(self):
        self.settings = QSettings("Mad Pony Interactive", "MadQt | Project Manager")
        self.ui.NewPFolderName.setText(self.settings.value("usrInput/newProjectDir", None))
        # self.settings.remove('projects')
        # Populate Projects List
        allP = self.settings.value("projects",[])
        [self.addProject(p) for p in allP]

    def extraMsg(self,msg,timeout=5000):
        """adds extra message to StatusBar"""
        if self.extraMsgWidget!=None:self.ui.statusbar.removeWidget(self.extraMsgWidget)
        self.extraMsgWidget = QLabel(msg)
        self.extraMsgWidget.setObjectName('extraMsg')
        self.ui.statusbar.insertWidget(1,self.extraMsgWidget,1)
        QTimer.singleShot(timeout,self.removeExtraMsg)

    def removeExtraMsg(self):
        self.ui.statusbar.removeWidget(self.extraMsgWidget)
        self.extraMsgWidget=None

    def setMainPageIndex(self,i):
        """open previous page if i == None"""
        i = self.prevMainPageindex if i is None else i
        self.prevMainPageindex = self.ui.mainPage.currentIndex()
        if i == 0:
            self.ui.startPageBtn.setChecked(1)
        elif i == 2:
            self.ui.PpageBtn.setChecked(1)
        self.ui.mainPage.setCurrentIndex(i)

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

    '''
    # A play around with custom resize handles
    def event(self, event):
        if event.type() == QEvent.MouseButtonRelease:
            self.grabbedHandle = False

        if event.type() == QEvent.MouseMove:
            if self.handle and event.buttons()==Qt.LeftButton:
                self.grabbedHandle=True
                gr=self.geometry()
                gp=event.globalPosition()
                minW=self.minimumSizeHint().width()
                minH=self.minimumSizeHint().height()
                x = int(gp.x())
                y = int(gp.y())
                # x = max(x,minW)
                if self.handle == 'top':
                    # y = min(y,minH)
                    gr.setTop(y)
                    # self.move(self.x(),y)
                elif self.handle == 'bottom':
                    gr.setBottom(y)



                # self.resize(gr.size())
                self.setGeometry(gr)
                self.updateGeometry()

        if event.type() == QEvent.HoverMove and not self.grabbedHandle:
            x=int(event.position().x())
            y=int(event.position().y())
            gr=self.geometry()
            w=gr.width()
            h=gr.height()
            o=8
            yr=y in range(o,h-o)
            xr=x in range(o,w-o)
            if not yr and not xr:
                # corners
                if y<o and x<o:
                    self.handle ='top left'
                    self.setCursor(Qt.SizeFDiagCursor)
                elif x>w-o and y<o:
                    self.handle ='top right'
                    self.setCursor(Qt.SizeBDiagCursor)
                elif x<o and y>h-o:
                    self.handle ='bottom left'
                    self.setCursor(Qt.SizeBDiagCursor)
                elif x>w-o and y>h-o:
                    self.handle ='bottom right'
                    self.setCursor(Qt.SizeFDiagCursor)
                else: self.handle = None
            else:
                # edges
                if x<o and yr:
                    self.handle ='left'
                    self.setCursor(Qt.SizeHorCursor)
                elif x>w-o and yr:
                    self.handle ='right'
                    self.setCursor(Qt.SizeHorCursor)
                elif y<o and xr:
                    self.handle ='top'
                    self.setCursor(Qt.SizeVerCursor)
                elif y>h-o and xr:
                    self.handle ='bottom'
                    self.setCursor(Qt.SizeVerCursor)
                else: self.handle = None

            if self.handle:
                pass
            else:
                self.setCursor(Qt.ArrowCursor)

        return QMainWindow.event(self, event)
    '''

    def initUi(self):
        self.ui.header.installEventFilter(self)
        self.ui.statusbar.insertPermanentWidget(0,QLabel('V.0.0.2'),0)

        # Start Page
        self.ui.startPageBtn.clicked.connect(lambda: self.setMainPageIndex(0))
        self.ui.newP.clicked.connect(lambda: self.setMainPageIndex(1))
        self.ui.addP.clicked.connect(self.addProjectFromFile)
        self.ui.delSelectedP.clicked.connect(lambda: self.removeSelectedProjects())
        self.ui.settBtn.clicked.connect(lambda: self.setMainPageIndex(3))
        self.ui.PpageBtn.clicked.connect(lambda: self.setMainPageIndex(2))
        self.ui.ProjectsList.itemDoubleClicked.connect(self.openProject)
        self.ui.ProjectsList.dropped.connect(self.droppedProject)

        # Settings Page
        default_qtPath = os.path.join(pySideDir())
        self.ui.QtDesignerPathInput.setText(self.settings.value("usrInput/designerPath", default_qtPath))
        self.ui.sublimePathInput.setText(self.settings.value("usrInput/sublimePath", ''))

        self.ui.icoSizeCb.setCurrentText(self.settings.value("usrInput/icoSize",str(64)))
        def changedIco(v): self.settings.setValue("usrInput/icoSize",v)
        self.ui.icoSizeCb.currentTextChanged.connect(changedIco)

        self.ui.QtDesignerPathBtn.clicked.connect(lambda: self.openFolder(self.ui.QtDesignerPathInput))
        self.ui.sublimePathBtn.clicked.connect(lambda: self.openFolder(self.ui.sublimePathInput))

        global MadQt_Designer_Paths
        MadQt_Designer_Paths = self.settings.value("usrInput/pluginPaths", [MadQt.get_path('QtDesignerPlugins')])
        for item in MadQt_Designer_Paths:
            self.ui.designerPathsList.addItem(item)

        self.ui.SettDoneBtn.clicked.connect(lambda: self.setMainPageIndex(None))
        self.ui.saveSett.clicked.connect(self.saveUserSettings)

        self.ui.createMQEXEC.clicked.connect(lambda: webbrowser.open("https://madponyinteractive.github.io/MadQt/ProjectManager/install.html"))

        # New custom widget page
        self.ui.cwQtClass.addItems(Mt.QDesignerBaseClasses())
        self.ui.cwQtClass.setCurrentText('QPushButton')
        self.ui.createWidget.clicked.connect(self.createWidget)
        self.ui.cancelCreateW.clicked.connect(lambda: self.setMainPageIndex(None))

        # New project page
        self.ui.newPFolder.clicked.connect(lambda: self.openFolder(self.ui.NewPFolderName))
        self.ui.newPIconBrowse.clicked.connect(lambda: self.openImg(self.ui.newPIcon,True))
        self.ui.createP.clicked.connect(self.createNewProject)
        self.ui.cancelCreateP.clicked.connect(lambda: self.setMainPageIndex(None))

        # New Ui Page
        self.ui.createNewUi.clicked.connect(self.createUi)
        self.ui.cancelCreateUi.clicked.connect(lambda: self.setMainPageIndex(None))

        # Project Page menu buttons
        self.ui.refreshBtn.clicked.connect(self.refresh)
        self.ui.openPFolder.clicked.connect(self.openProjectFolder)
        if self.hasSublime():
            self.ui.sublimePBtn.setStatusTip('Open sublime project')
        else:
            self.ui.sublimePBtn.setStatusTip('Setup sublime path in settings to open sublime projects')

        self.ui.sublimePBtn.clicked.connect(self.openSublimeProject)
        self.ui.uiFilesBtn.clicked.connect(lambda: self.ui.PStackedWidget.setCurrentIndex(0))
        self.ui.custWidgetsBtn.clicked.connect(lambda: self.ui.PStackedWidget.setCurrentIndex(1))
        self.ui.qrcPBtn.clicked.connect(lambda: self.ui.PStackedWidget.setCurrentIndex(2))
        self.ui.execPBtn.clicked.connect(lambda: self.ui.PStackedWidget.setCurrentIndex(3))
        self.ui.runBtn.clicked.connect(self.runApp)
        self.ui.saveAsBtn.clicked.connect(self.saveToNewFolder)

        # Ui page
        self.ui.uiList.itemDoubleClicked.connect(self.openUi)
        self.ui.uiList.dropped.connect(self.addUiFiles)
        self.ui.addUiBtn.clicked.connect(self.addUiFiles)
        self.ui.delSelectedUiBtn.clicked.connect(self.removeUi)
        self.ui.newUiBtn.clicked.connect(lambda: self.setMainPageIndex(5))

        # Custom Widget page
        self.ui.moduleTree.header().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.moduleTree.droppedModule.connect(self.addModules)
        self.ui.moduleTree.itemDoubleClicked.connect(self.openClass)
        self.ui.addModuleBtn.clicked.connect(self.addModuleDialogue)
        self.ui.delSelectedMods.clicked.connect(self.deleteModules)
        self.ui.newModuleBtn.clicked.connect(self.newModule)
        self.ui.cwClass.textChanged.connect(self.cwClassChanged)
        self.ui.cwMod.textChanged.connect(self.cwModChanged)
        self.ui.cwQtClass.currentTextChanged.connect(self.cwQtClassChanged)

        # Qrc Image page
        self.ui.qrcTree.header().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.qrcTree.droppedQrc.connect(self.addQrc)
        self.ui.qrcTree.droppedImg.connect(self.addImages)

        iSize = self.settings.value("usrInput/iconSize",QSize(64,64))
        self.ui.qrcTree.setIconSize(iSize)
        self.ui.imgSizeSlider.setValue(iSize.width())
        def setIconSize(s):
            size=QSize(s,s)
            self.ui.qrcTree.setIconSize(size)
            self.settings.setValue("usrInput/iconSize",size)
            self.ui.statusbar.showMessage(f'Icon size: {s}px')
        self.ui.imgSizeSlider.valueChanged.connect(setIconSize)

        # Create Executable page
        self.ui.createExecBtn.clicked.connect(self.createExec)
        self.ui.pyinstallerHelp.clicked.connect(lambda:\
         webbrowser.open('https://pyinstaller.readthedocs.io/en/stable/when-things-go-wrong.html'))

    # Create Executable
    @thread
    def runExec(self,arguments):
        process = subprocess.Popen(arguments, shell=True, bufsize = 1,
            stdout=subprocess.PIPE, stderr = subprocess.STDOUT,
            encoding='utf-8', errors = 'replace')
        while True:
            realtime_output = process.stdout.readline()
            if realtime_output == '' and process.poll() is not None:
                self.finishExec()
                break
            if realtime_output:
                self.ui.execOutput.append(realtime_output.strip())

    def finishExec(self):
        for file in os.listdir(self.project.devPath()):
            if os.path.splitext(file)[1] == '.spec':
                os.remove(file)
                break
        shutil.rmtree(self.project.devFile('build'))
        src = self.project.devFile('dist')
        dst = self.project.folder

        findAt = os.path.join(dst,'dist')
        if os.path.isdir(findAt):shutil.rmtree(findAt)
        shutil.move(src, dst, copy_function = shutil.copytree)

        self.ui.execOutput.append(F"Successfully created executable for project: {self.project.name}!")
        self.ui.execOutput.append(F"Output files located @ {findAt}")
        self.ui.execOutput.moveCursor(QTextCursor.End)

        self.ui.statusbar.showMessage('Executable created!')

    def createExec(self):
        self.ui.statusbar.showMessage('Creating executable...')
        self.project.updateUis()
        os.chdir(self.project.devPath())
        arguments = F"pyinstaller "
        arguments += self.ui.execArgs.text()
        arguments +=F" --icon {os.path.join('gui',self.project.icon)} main.py"
        self.ui.execOutput.ensureCursorVisible()
        self.ui.execOutput.append(f'Running: {arguments}')
        self.runExec(arguments)

    # Helper Dialogues
    def openFile(self,fType='All Files (*)',prefix=''):
        return QFileDialog.getOpenFileName(self,
                "MadQt Project Manager",
                prefix,
                fType, "")

    def openFiles(self,fType='All Files (*)',prefix=''):
        return QFileDialog.getOpenFileNames(self,
                "MadQt Project Manager",
                prefix,
                fType, "")

    def openFolder(self,widget):
        """ Opens a file dialogue
            Sets text on provided widget
        """
        text = widget.text() if len(widget.text()) else ''
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self,
                "MadQt Project Manager - Select folder",
                text, options)
        if directory:
            widget.setText(directory)
            self.selectedPath = directory

    def openImg(self,widget,ico=False):
        """ Opens a file dialogue
            Sets pixmap on provided widget
        """
        file = self.openFile('Images (*.png *.ico *.jpg *.gif *.svg)',widget.text())[0]
        if len(file):
            if ico:
                if '.ico' not in file:
                    dest_ico = os.path.join(tempDir(),'logo.ico')
                    file = Mt.createIco(file,dest_ico,self.defaultIcoSize())
            widget.setPixmap(QPixmap(file))
            self.selectedFile = file
            # self.settings.setValue("usrInput/newProjectIcon", directory)

    def questionBox(self,msg):
        reply = QMessageBox.question(self, "MadQt Warning!",
                msg,
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            return "Yes"
        elif reply == QMessageBox.No:
            return "No"
        else:
            return "Cancel"

    def labelBox(self,msg,text):
        usrInput, ok = QInputDialog.getText(self, "MadQt Project Manager",
            msg, QLineEdit.Normal, text)
        if ok and usrInput != '':
            return usrInput

    # Project Methods
    def addProject(self,file=None,save=False):
        """
            Adds item to the start page project list
            Saves project to settings if save=True
        """
        if isinstance(file,QListWidgetItem):
            file=file.file
            save=True
        elif not file:
            file = self.project.file()

        # File was deleted from system?
        if not os.path.isfile(file):
            self.removeProject(file,True)
            return

        # File already added?
        for item in self.ui.ProjectsList.getItems():
            if item.file == file:
                # self.removeProject(file,True)
                self.extraMsg('Project folder already in list!')
                return

        # Add project to the start page project list
        self.ui.ProjectsList.insertItem(0,ProjectItem(file))
        # Save project to settings
        if not save:return
        allP = self.settings.value("projects",[])
        # remove projects with same folder
        [self.removeProject(p,True) for p in allP if p == file]
        allP.append(file)
        self.settings.setValue("projects", allP)

    def removeProject(self,file=None,save=False):
        """
            Removes item from the start page project list
            Removes project from settings if save=True
        """
        if isinstance(file,QListWidgetItem):
            file=file.file
            save=True
        elif not file:
            file = self.project.file()

        self.ui.ProjectsList.removeItem(file)

        # Removes project from settings
        if not save:return
        allP = self.settings.value("projects",[])
        [allP.remove(p) for p in allP if p == file]
        self.settings.setValue("projects", allP)
        if not len(allP):self.ui.PpageBtn.setEnabled(False)

    def removeSelectedProjects(self):
        """removes all selected projects in project list"""
        [self.removeProject(item) for item in self.ui.ProjectsList.selectedItems()]

    def addProjectFromFile(self,file=None):
        """Add and open a project from an existing file"""
        file = self.openFile('MadQt Project Files (*.mqpm)')[0]\
         if not file else file
        if not len(file):return

        if not file.endswith('mqpm'):
            self.extraMsg('Not a valid project file!')
            return

        # Update folder path
        prevSettings = {}
        with open(file, "r") as f: prevSettings = json.loads(f.read())
        prevSettings['folder'] = os.path.dirname(file)
        with open(file, "w") as f: json.dump(prevSettings, f, indent=4)

        self.addProject(file,True)

    def createNewProject(self):
        name = self.ui.projectNameInput.text()
        folder = self.ui.NewPFolderName.text()
        if not os.path.isdir(folder):
            self.ui.statusbar.showMessage('Provided path not found!',5000)
            return
        name = 'New MadQt project' if not name else name.strip()
        self.settings.setValue("usrInput/newProjectDir", folder)

        folder = os.path.join(folder,Mt.cleanString(name))

        ico = os.path.join(MadQt.get_path('Templates'),'NewProject','gui','logo.ico')
        if self.selectedFile is not None:
            ico = ico if '.ico' not in self.selectedFile else self.selectedFile
        self.project = Project(name,folder,ico)

        if not self.project.valid:
            self.project = Project()
            self.ui.statusbar.showMessage('Could not create project! Provided folder has a project?')
            return

        # self.settings.remove('projects')#333333333333333333333333333333333
        self.addProject(save=True)
        self.extraMsg(f'Successfully created "{name}"!')
        self.openProject()

    def saveToNewFolder(self):
        """open file dialogue"""
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        fileName, filtr = QFileDialog.getSaveFileName(self,
                "MadQt Project Manager - Save to new folder",
                self.project.folder,
                "MadQt Project Files (*.mqpm)", "", options)

        file_name = os.path.basename(fileName)
        file, ext = os.path.splitext(file_name)
        directory = os.path.dirname(fileName)

        if fileName != '':
            self.project.name = file
            if self.project.saveToNewFolder(directory):
                self.addProject(save=True)
                self.extraMsg(f'Successfully saved and opened!')
                self.openProject()
            else:
                self.extraMsg(f'Could not save, saving in a project folder?')

    def droppedProject(self, urls):
        """when user drops file on projects list"""
        [self.addProjectFromFile(file) for file in urls]

    def openProject(self,item=None):
        """open existing project"""
        if item:
            # Avoid re-opening same project
            if item.file == self.project.file():
                self.setMainPageIndex(2)
                return
            self.project = Project(item.file)
        self.setCursor(Qt.WaitCursor)

        self.ui.qrcTree.clear()
        self.ui.moduleTree.clear()
        self.ui.uiList.clear()
        if not self.project.valid:return

        self.ui.statusbar.showMessage('Loading project...')

        self.ui.PpageBtn.setEnabled(True)
        if self.hasSublime(): self.ui.sublimePBtn.setEnabled(True)
        self.ui.PpageBtn.setChecked(True)
        self.ui.PrjName.setText(self.project.name)

        self.project.updateUis()

        # Populate Ui list
        [self.addUi(ui) for ui in self.project.uiFiles() if os.path.isfile(ui)]
        # Populate Qrc list
        [self.addQrc(qrc) for qrc in self.project.qrcFiles() if os.path.isfile(qrc)]
        # Populate Custom Widget list
        [self.addModule(mod) for mod in self.project.customWidgetsFiles() if os.path.isfile(mod)]

        self.ui.execArgs.setText(F"--onefile --windowed --name={Mt.cleanString(self.project.name)}")

        self.setMainPageIndex(2)
        self.ui.statusbar.showMessage(f'{self.project.name} project loaded!')
        self.setCursor(Qt.ArrowCursor)

    def openProjectFolder(self):
        # Open base on project page
        Mt.openFileExplorer(self.project.folder)

    # Qrc Methods
    def createQrc(self):
        qrcName = self.labelBox("New Qrc name:",'resources.qrc')
        if not qrcName:return
        self.setCursor(Qt.WaitCursor)
        if '.' not in qrcName: qrcName = qrcName + '.qrc'
        fn,ext=os.path.splitext(qrcName)
        qrcName=Mt.cleanString(fn,True)+ext
        qrcFile = self.project.createQrc(qrcName)
        self.addQrc(qrcFile)
        self.setCursor(Qt.ArrowCursor)

    def addQrc(self,file=None,save=False):
        """
            Adds qrc files, prefixes and images
            to the project qrc tree
            Saves qrc to project settings if save=True
        """
        if file is None:# file dialogue
            qrcs = self.openFiles('Qrc Resource files (*.qrc)')[0]
            [self.addQrc(qrc,True) for qrc in qrcs]
            return
        if isinstance(file,list):# dropped
            [self.addQrc(qrc,True) for qrc in file]
            return

        if save:
            base = os.path.basename(file)
            if not self.project.addQrc(base):
                self.extraMsg(f"{base} not added, a file with the same name already exists in project!")
                return

        res_item=QrcFile(file,self.ui.qrcTree)
        parsed = xml.parse(file)
        for resource in parsed.findall('qresource'):
            # print(resource.get('prefix'))
            pre_item=self.addPrefix(resource.get('prefix'),res_item)
            for img in resource.findall('file'):
                self.addImage(self.project.guiFile(img.text),pre_item,file)
                # print(img.text)
        return res_item
        # self.ui.qrcTree.addTopLevelItem()

    def addPrefix(self,prefix=None,parent=None,save=False,add=True):
        qrc=None
        if not prefix:# QLineEdit popup
            msg = ''
            # add=self.ui.addPrefixBtn.text()=='Add Prefix'
            if add:
                placeholder='newPrefix'
                topLevel = parent = self.ui.qrcTree.topLevelItem(0)
                if topLevel:# not empty
                    items = self.ui.qrcTree.selectedItems()
                    if not len(items):
                        qrc = topLevel.text(0)
                        msg+='No qrc file selected, will add prefix to ' + qrc
                    else:
                        foundQrcs=[]
                        [foundQrcs.append(item) for item in items if item.type()==0]
                        if len(foundQrcs)>1:
                            qrc = topLevel.text(0)
                            msg+='Multiple qrc files selected, will add prefix to ' + qrc
                        else:
                            parent = foundQrcs[0]
                            qrc = parent.text(0)
                    qrc = self.project.guiFile(qrc)# full path
                else:
                    msg +="This will create a resources.qrc file!"
                msg +="\nPrefix name:"
            else:# rename
                placeholder=self.ui.qrcTree.currentItem().text(0)
                msg +="WARNING:\n"
                msg +="When renaming prefixes your ui paths do not get updated!\n"
                msg +="If you rename a prefix that is already in use by an ui,\n"
                msg +="you will need to update the ui resource path to display its images.\n"
                msg +="\n New Prefix name:"

            prefix, ok = QInputDialog.getText(self, "MadQt Project Manager",
                    msg, QLineEdit.Normal,
                    placeholder)
            if ok and prefix != '':
                if add:
                    if not qrc:
                        qrc = self.project.createQrc()
                        parent = self.addQrc(qrc)
                    save=True
                else:# rename
                    current = self.ui.qrcTree.currentItem()
                    prevPrefix = current.text(0)
                    current.setText(0,prefix)
                    qrc = current.parent().file
                    parsed = xml.parse(qrc)
                    for res in parsed.findall('qresource'):
                        if res.get('prefix')==prevPrefix:
                            res.set('prefix',prefix)
                            break
                    xml.indent(parsed.getroot())
                    parsed.write(qrc)
                    return

        if save:
            # add prefix to qrc file
            if not qrc: qrc = parent.file
            parsed = xml.parse(qrc)
            pfE = xml.Element('qresource')
            pfE.set('prefix',prefix)
            parsed.getroot().append(pfE)
            self.project.updateUis()
            xml.indent(parsed.getroot())
            parsed.write(qrc)
            self.ui.statusbar.showMessage('Done')

        return QrcPrefix(prefix,parent)

    def addImagesDialogue(self):
        imgs = self.openFiles('Images (*.png *.ico *.jpg *.gif *.svg)')[0]
        if len(imgs):self.addImages(imgs)

    @thread
    def addImages(self,imgs=None):
        if isinstance(imgs,dict):# dropped
            [self.addImage(img,imgs['prefix'],imgs['qrc'],True) for img in imgs['imgs']]
        else:# file dialogue
            prefix=None
            qrc = self.ui.qrcTree.topLevelItem(0)# could be None
            if qrc:# not empty
                items = self.ui.qrcTree.selectedItems()
                if not len(items):# nothing selected
                    prefix = qrc.child(0)# could be None
                else:
                    current = self.ui.qrcTree.currentItem()
                    if current.type()==2:# current image
                        prefix = current.parent()
                        qrc = current.parent().parent()
                    elif current.type()==1:# current prefix
                        prefix=current
                        qrc=current.parent()
                    else:# current qrc
                        qrc=current
            [self.addImage(img,prefix,qrc,True) for img in imgs]

    def addImage(self,img,prefix=None,qrc=None,save=False):
        """
            adds image to qrcTree
            adds to qrc file if save
        """
        if save:
            self.ui.statusbar.showMessage(f'Saving {img}...')
            if not qrc:
                qrc = self.project.createQrc()
                qrc = self.addQrc(qrc)
            if not prefix:
                prefix = self.addPrefix('newPrefix',qrc,True)

            # add image file to qrc file
            parsed = xml.parse(qrc.file)
            fE = xml.Element('file')
            fE.text = os.path.basename(img)
            for res in parsed.findall('qresource'):
                if res.get('prefix') == prefix.text(0):
                    res.append(fE)

            xml.indent(parsed.getroot())
            parsed.write(qrc.file)

            dest_img = self.project.guiFile(fE.text)
            shutil.copy2(img,dest_img)
            img=dest_img

            self.project.updateUis()
            self.ui.statusbar.showMessage('Done')

        QrcImage(img,prefix)

    def tintImagesDlg(self,imgs,_type):
        """tint selected images dialogue"""
        c = QColorDialog.getColor(self.settings.value("usrInput/tintColor",Qt.red), self)
        if c.isValid():
            self.settings.setValue("usrInput/tintColor", c)
            self.tintImages(imgs,c,_type)

    @thread
    def tintImages(self,imgs,c,_type):
        """tint selected images"""
        [img.tint((c.red(),c.green(),c.blue()),_type) for img in imgs]

    @thread
    def restoreImages(self,imgs):
        """undo tinted selected images"""
        [img.restore() for img in imgs if img.tinted]

    @thread
    def makeIco(self,imgs):
        for img in imgs:
            if '.ico' not in img.file:
                base = os.path.basename(img.file)
                fname,_=os.path.splitext(base)
                dest_ico = os.path.join(tempDir(),fname+'.ico')
                Mt.createIco(img.file,dest_ico,self.defaultIcoSize())
                self.addImage(dest_ico,img.parent(),img.parent().parent(),True)

    @thread
    def setIcon(self,img):
        """Sets current image as project icon"""
        base = os.path.basename(img.file)
        self.project.setIcon(base)
        for project in self.ui.ProjectsList.getItems():
            if project.file == self.project.file():
                project.setIcon(QPixmap(img.file))
                break

    def renameImage(self,item):
        fName,fExt=os.path.splitext(item.text(0))
        usrInput = self.labelBox("New Image name:",fName)
        if usrInput:
            if '.' in usrInput:
                usrInput = usrInput.replace(os.path.splitext(usrInput)[1],'')
            usrInput=Mt.cleanString(usrInput,True)+fExt
            qrc = item.parent().parent().file
            prefix = item.parent().text(0)
            dest = item.file.replace(item.text(0),usrInput)
            os.rename(item.file, dest)
            # project icon?
            if self.project.iconPath() == item.file:self.setIcon(item)
            item.file = dest
            parsed = xml.parse(qrc)
            for res in parsed.findall('qresource'):
                if res.get('prefix')==prefix:
                    for file in res.findall('file'):
                        if file.text == item.text(0):
                            file.text=usrInput
                            break
            item.setText(0,usrInput)
            xml.indent(parsed.getroot())
            parsed.write(qrc)
            self.project.updateUis()

    def renameQrc(self,item):
        fName,fExt=os.path.splitext(item.text(0))
        usrInput = self.labelBox("New Qrc name:",fName)
        if usrInput:
            if '.' in usrInput:
                usrInput = usrInput.replace(os.path.splitext(usrInput)[1],'')
            usrInput=Mt.cleanString(usrInput,True)+fExt

            dest = item.file.replace(item.text(0),usrInput)
            os.rename(item.file, dest)
            item.file = dest
            self.project.settings['qrcFiles'].remove(item.text(0))
            self.project.settings['qrcFiles'].append(usrInput)
            item.setText(0,usrInput)
            self.project.updateUis()

    def deleteQrcs(self,items):
        msg ="This will delete the selected qrc files and all it's images!\n"
        msg +="Do you wish to proceed?"
        answer = self.questionBox(msg)
        if answer != 'Yes':return
        [self.deleteQrc(i) for i in items]

    @thread
    def deleteQrc(self,item):
        self.ui.statusbar.showMessage(f'Deleting Qrc: {item.text(0)}...')
        parsed = xml.parse(item.file)
        for resource in parsed.findall('qresource'):
            for image in resource.findall('file'):
                imgPath = self.project.guiFile(image.text)
                os.remove(imgPath)
        os.remove(item.file)
        self.project.settings['qrcFiles'].remove(item.text(0))
        self.project.updateUis()
        self.ui.qrcTree.removeTopLevelItem(item)
        self.ui.statusbar.showMessage('Done')

    def deletePrefixes(self,items):
        msg ="This will delete the selected prefixes and all it's images!\n"
        msg +="Do you wish to proceed?"
        answer = self.questionBox(msg)
        if answer != 'Yes':return
        [self.deletePrefix(i) for i in items]

    @thread
    def deletePrefix(self,item):
        self.ui.statusbar.showMessage(f'Deleting Prefix: {item.text(0)}...')
        parsed = xml.parse(item.parent().file)
        for resource in parsed.findall('qresource'):
            if resource.get('prefix')==item.text(0):
                for image in resource.findall('file'):
                    imgPath = self.project.guiFile(image.text)
                    os.remove(imgPath)
                parsed.getroot().remove(resource)

        xml.indent(parsed.getroot())
        parsed.write(item.parent().file)
        self.project.updateUis()
        item.parent().removeChild(item)
        self.ui.statusbar.showMessage('Done')

    def deleteImages(self,items):
        msg ="This will permanently delete the selected images!\n"
        msg +="Do you wish to proceed?"
        answer = self.questionBox(msg)
        if answer != 'Yes':return
        [self.deleteImage(i) for i in items]

    @thread
    def deleteImage(self,item):
        # project icon?
        if self.project.iconPath() == item.file:
            self.ui.statusbar.showMessage(f'Image {item.text(0)} is project icon and cannot be deleted!')
            return
        self.ui.statusbar.showMessage(f'Deleting Image: {item.text(0)}...')
        parsed = xml.parse(item.parent().parent().file)
        for resource in parsed.findall('qresource'):
            if resource.get('prefix')==item.parent().text(0):
                for image in resource.findall('file'):
                    if image.text==item.text(0):
                        imgPath = self.project.guiFile(image.text)
                        os.remove(imgPath)
                        resource.remove(image)
        xml.indent(parsed.getroot())
        parsed.write(item.parent().parent().file)
        self.project.updateUis()
        item.parent().removeChild(item)
        self.ui.statusbar.showMessage('Done')

    # Modules methods (Custom Widgets)
    def deleteModules(self):
        items=self.ui.moduleTree.selectedModules()
        msg ="This will permanently delete the selected modules!\n"
        msg +="Do you wish to proceed?"
        answer = self.questionBox(msg)
        if answer != 'Yes':return
        [self.deleteModule(i) for i in items]

    @thread
    def deleteModule(self,item):
        self.ui.statusbar.showMessage(f'Deleting Module: {item.text(0)}...')
        if os.path.isfile(item.file):os.remove(item.file)
        self.project.settings['customWidgets'].pop(item.text(0))
        self.project.updateUis()
        self.ui.moduleTree.removeTopLevelItem(item)
        self.ui.statusbar.showMessage('Done')

    def renameModule(self,item):
        fName,fExt=os.path.splitext(item.text(0))
        usrInput = self.labelBox("New Module name:",fName)
        if usrInput:
            if '.' in usrInput:
                usrInput = usrInput.replace(os.path.splitext(usrInput)[1],'')
            usrInput=Mt.cleanString(usrInput,True)+fExt

            dest = item.file.replace(item.text(0),usrInput)
            os.rename(item.file, dest)
            item.file = dest
            moduleValue = self.project.settings['customWidgets'].get(item.text(0))
            self.project.settings['customWidgets'].pop(item.text(0))
            self.project.settings['customWidgets'][usrInput] = moduleValue
            item.setText(0,usrInput)
            self.project.updateUis()

    def addModules(self,mods=None):
        if not mods: mods = self.openFiles('Custom Widgets (*.py)')[0]
        [self.addModule(mod,True) for mod in mods]

    def addModuleDialogue(self):
        mods = self.openFiles('Custom Widgets (*.py)')[0]
        if len(mods):self.addModules(mods)

    @thread
    def addModule(self,file=None,save=False):
        basename = os.path.basename(file)
        if save:
            if self.project.settings['customWidgets'].get(basename,False):
                self.ui.statusbar.showMessage(f'A custom widgets named: {basename} already exists!')
                return
            self.project.settings['customWidgets'][basename]=[]
            src=file
            file = self.project.widgetFile(basename)
            shutil.copy2(src,file)
        moduleItem = CustomWidgetFile(file, self.ui.moduleTree)
        valueList = []
        with open(file,"r") as f:
            for line in f:
                if 'class' in line:
                    qtClass = [_class for _class in Mt.QDesignerBaseClasses() if _class in line]
                    if len(qtClass):
                        start = line.index('class ')+6
                        end = line.index('(')
                        userClass = line[start:end]
                        CustomWidgetClass(userClass, qtClass[0], moduleItem)
                        valueList.append({'class':userClass,'qt_class':qtClass[0]})
        self.project.settings['customWidgets'][basename]=valueList
        self.project.saveSett()
        if save:
            self.project.updateUis()

    def openModule(self,item):
        """opens in sublime text"""
        # print(item.file)
        if not self.hasSublime():return
        os.chdir(self.ui.sublimePathInput.text())
        subprocess.Popen(['subl', item.file],shell=True)

    def openClass(self,item,col=None):
        """opens in sublime text"""
        if isinstance(item,CustomWidgetFile):return
        if not self.hasSublime():
            self.ui.statusbar.showMessage('Sublime Text path not set. Navigate to Settings to set it.')
            return
        lineToOpen=0
        with open(item.parent().file,"r") as f:
            for i, line in enumerate(f):
                if item.text(0) in line:
                    lineToOpen=str(i+1)
                    break
        os.chdir(self.ui.sublimePathInput.text())
        subprocess.Popen(['subl', item.parent().file+':'+lineToOpen],shell=True)

    def addClass(self):
        moduleItem = self.ui.moduleTree.currentItem()
        self.ui.cwModLbl.hide()
        self.ui.cwMod.hide()
        self.ui.cwMod.setText(moduleItem.text(0)[:-2])
        self.setMainPageIndex(4)

    def newModule(self):
        self.ui.cwModLbl.show()
        self.ui.cwMod.show()
        self.setMainPageIndex(4)

    def cwModChanged(self,text):
        if len(text):
            text = Mt.cleanString(text,True)
            self.ui.cwMod.setText(text[0].lower() + text[1:])

    def cwQtClassChanged(self,text):
        self.ui.cwClass.setPlaceholderText(text[1:])
        if self.ui.cwMod.isVisible():
            text = text[1:]
            text = text[0].lower() + text[1:]
            self.ui.cwMod.setPlaceholderText(text)

    def cwClassChanged(self,text):
        if len(text):
            text = Mt.cleanString(text,True)
            self.ui.cwClass.setText(text[0].upper() + text[1:])
            self.ui.cwMod.setPlaceholderText(text[0].lower() + text[1:])

    def createWidget(self):
        qt_class = self.ui.cwQtClass.currentText()

        _class = self.ui.cwClass.text()
        _class = _class if _class != '' else self.ui.cwClass.placeholderText()

        module = self.ui.cwMod.text()
        module = module if module != '' else self.ui.cwMod.placeholderText()

        filename = module +'.py'

        if self.ui.cwMod.isVisible():# new module
            file = os.path.join(tempDir(),filename)
            with open(file, "w") as fp:
                fp.write(customWidgetModule(_class,qt_class))
            self.addModule(file,True)
        else:# add class
            file = self.project.widgetFile(filename)
            with open(file, "a") as fp:
                fp.write(customWidgetClass(_class,qt_class))

            self.project.settings['customWidgets'][filename].append({'class':_class,'qt_class':qt_class})
            self.project.saveSett()
            self.refresh()

        self.setMainPageIndex(2)
        self.ui.statusbar.showMessage(f'Custom widget "{_class}" created!')

    # Ui Methods
    def openUi(self,item):
        """Opens ui file in QDesigner"""
        self.ui.statusbar.showMessage('Opening in QDesigner...')
        qd = self.settings.value("usrInput/designerPath", None)
        if os.path.isdir(qd):
            os.chdir(qd)
            subprocess.Popen(['designer', item.file],shell=True)

    def addUiFiles(self,file):
        """Adds ui file to project"""
        file = self.openFiles('Ui Files (*.ui)')[0]\
         if not file else file
        [self.addUi(ui,True) for ui in file if len(file)]

    def createUi(self):
        ui_type = self.ui.newUiType.currentText()# ex: QMainWindow
        ui_name = self.ui.newUiInput.text()
        ui_name = ui_name if len(ui_name) else 'MainWindow'
        clean_name=Mt.cleanString(ui_name)+'.ui'

        if clean_name in self.project.settings['uiFiles']:
            self.ui.newUiInput.setText(clean_name.replace('.ui',''))
            self.extraMsg(f'Ui with same name: "{clean_name}" found! Please rename ui!')
            return

        ui_filename = 'mainwindow.ui' if ui_type == 'QMainWindow' else 'widget.ui'
        ui_file = os.path.join(MadQt.get_path('Templates'),'Uis',ui_filename)
        # copy template to tempDir
        temp_dir = os.path.join(tempDir(),clean_name)
        shutil.copyfile(ui_file,temp_dir)
        self.addUi(temp_dir,True)
        self.setMainPageIndex(2)

    def addUi(self,file=None,save=False):
        """
            Adds ui to the project ui list
            Saves ui to project settings if save=True
        """
        if isinstance(file,QListWidgetItem):
            file=file.file
            save=True
        elif not file.endswith('ui'):
            self.extraMsg('Not a valid ui file!')
            return

        # File was deleted from system?
        if not os.path.isfile(file):
            self.removeUi(file,True)
            return

        # Ui name already added?
        for item in self.ui.uiList.getItems():
            bname = os.path.basename(file)
            if item.name == bname:
                self.extraMsg(f'Ui with same name: "{bname}" found! Please rename ui!')
                return

        # Add ui to the project ui list
        if not isTemp(file): self.ui.uiList.insertItem(0,UiItem(file))

        # Save ui to project settings
        if not save:return
        new_location = self.project.addUi(file)
        if isTemp(file): self.ui.uiList.insertItem(0,UiItem(new_location))

    def removeUi(self,file=None,save=False):
        """
            Removes item from the project page ui list
            Removes ui from project settings if save=True
        """
        if isinstance(file,QListWidgetItem):
            file=file.file
            save=True
        elif file is None:
            answer = self.questionBox("This will delete the .ui and compiled .py files from your system!\n Do you wish to proceed?")
            if answer != 'Yes':return
            [self.removeUi(ui) for ui in self.ui.uiList.selectedItems()]
        # Remove from uiList
        self.ui.uiList.removeItem(file)
        # Remove from project settings
        if not save:return
        self.project.removeUi(file)

    # Settings Methods
    def saveUserSettings(self):
        """save settings ui button"""
        dp = self.ui.QtDesignerPathInput.text()
        sp = self.ui.sublimePathInput.text()
        if os.path.isdir(dp):
            self.settings.setValue("usrInput/designerPath", dp)
        if os.path.isdir(sp):
            self.settings.setValue("usrInput/sublimePath", sp)
            self.ui.sublimePBtn.setStatusTip('Open sublime project')
            if self.project.valid:self.ui.sublimePBtn.setEnabled(1)

        self.setMainPageIndex(None)

    def defaultIcoSize(self):
        size = int(self.settings.value("usrInput/icoSize",str(64)))
        return [(size,size)]

    def addPluginPath(self):
        global MadQt_Designer_Paths
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self,
                "MadQt Project Manager - Select plugin folder",
                MadQt.get_path('QtDesignerPlugins'), options)
        if directory:
            paths = self.settings.value("usrInput/pluginPaths",[])
            paths.append(directory)
            self.settings.setValue("usrInput/pluginPaths",paths)
            self.ui.designerPathsList.addItem(directory)
            MadQt_Designer_Paths=paths

    def removePluginPath(self):
        global MadQt_Designer_Paths
        paths = self.settings.value("usrInput/pluginPaths",[])
        removed = self.ui.designerPathsList.removeCurrentItem()
        for item in paths:
            if item == removed.text():
                paths.remove(item)
                break
        self.settings.setValue("usrInput/pluginPaths",paths)
        MadQt_Designer_Paths=paths

    # other
    def openSublimeProject(self):
        """opens sublime project if not open"""
        subDir = self.ui.sublimePathInput.text()
        if not os.path.isdir(subDir):return
        # change to sublime dir
        os.chdir(subDir)

        foundProject=False
        for file in os.listdir(self.project.folder):
            fn,ext = os.path.splitext(file)
            if 'sublime-project' in ext:
                foundProject = os.path.join(self.project.folder,file)
                break

        if not foundProject:
            msg = "A sublime-project file was not found! \n"
            msg += "MadQt will start a new sublime project for you,\n"
            msg += "but you will have to save it to your MadQt project folder. \n"
            msg += "\nCopy the path bellow and press Ok, when sublime opens,\n"
            msg += " go to: Project -> Save Project As... \n"
            msg += " navigate to the provided path, and save your file there!"
            usrIn = self.labelBox(msg,self.project.folder)
            if usrIn:
                # open new window
                nw = subprocess.run('subl -n',capture_output=True)
                # add folder
                addF = subprocess.run(['subl', '-b', '--command <Project:Add Folder>',
                    self.project.folder],shell=True,capture_output=True)
        else:
            subprocess.run(['subl', '--project', foundProject],shell=True)

    def hasSublime(self):
        """returns sublime text is available"""
        return os.path.isdir(self.ui.sublimePathInput.text())

    def runApp(self):
        if self.project.runApp() is not None:
            self.ui.statusbar.showMessage('Cannot run, no Ui added yet!')

def main():
    global window
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
