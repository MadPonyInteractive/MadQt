""" MadQt - Tutorials and Tools for PySide

    All the Code in this package can be used freely for personal and
    commercial projects under a MIT License but remember that because
    this is an extension of the PyQt framework you will need to abide
    to the QT licensing scheme when releasing.

    ## $MADQT_BEGIN_LICENSE
    ## MIT License
    ##
    ## Copyright (c) 2021 Fabio Goncalves
    ##
    ## Permission is hereby granted, free of charge, to any person obtaining a copy
    ## of this software and associated documentation files (the "Software"), to deal
    ## in the Software without restriction, including without limitation the rights
    ## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    ## copies of the Software, and to permit persons to whom the Software is
    ## furnished to do so, subject to the following conditions:
    ##
    ## The above copyright notice and this permission notice shall be included in all
    ## copies or substantial portions of the Software.
    ##
    ## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    ## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    ## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    ## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    ## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    ## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    ## SOFTWARE.
    ## $MADQT_END_LICENSE

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
"""
from __future__ import absolute_import
import sys, os, subprocess, fileinput, platform, io, importlib, tempfile
from PIL import Image, ImageChops
import xml.etree.ElementTree as xml
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QDir
import MadQt

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

def breakArgs(string):
    """turns name(arg1,arg2) into ('name','arg1,arg2')"""
    split = string.split('(')
    split[1]=split[1][:-1]
    return tuple(split)

def packageHasMethod(package,method):
    """
        checks if the package exits and if it has the method
        returns None if no package was found
        returns a bool for found class
        example: packageHasMethod('PySide6.QtWidgets','QApplication')
    """
    try:
        imported = importlib.import_module(package)
        if imported: return hasattr(imported,method)
    except:
        return None

def createIco(file_in,file_out=None,sizes=[(32,32)]):
    """
        file_in must be in read format
            file_in = r'filename'
        size may be [
            (16, 16), (24, 24), (32, 32),
            (48, 48), (64, 64), (128, 128), (255, 255)
        ]

    """
    if not file_out:
        file_out = os.path.splitext(file_in)[0]+'.ico'

    with Image.open(file_in) as img:
        img = img.convert('RGBA')# windows fix
        img.save(file_out, format = 'ICO', sizes=sizes)
        # img.save(file_out, format = 'ICO', bitmap_format="bmp", sizes=sizes)
    return file_out

def tintImage(image, tint_color, _type=0):
    """usage: tintImage(dest_img,(255,0,0))"""
    with Image.open(image) as img:
        if _type == 0 and img.mode == 'RGBA':
            img=ImageChops.composite(Image.new(img.mode, img.size, tint_color),Image.new(img.mode, img.size, (0,0,0,0)), img)
        else:
            img = img.convert('RGBA')# windows fix
            img=ImageChops.multiply(img, Image.new(img.mode, img.size, tint_color))
        img.save(image)

def QDesignerBaseClasses():
    """QDesigner accepted custom widget sub classes"""
    return [
        'QGroupButton',
        'QCalendarWidget',
        'QCheckBox',
        'QColumnView',
        'QComboBox',
        'QCommandLinkButton',
        'QDateEdit',
        'QDateTimeEdit',
        'QDial',
        'QDialogButtonBox',
        'QDockWidget',
        'QDoubleSpinBox',
        'QFontComboBox',
        'QFrame',
        'QGraphicsView',
        'QGroupBox',
        'QKeySequenceEdit',
        'QLCDNumber',
        'QLabel',
        'QLineEdit',
        'QListView',
        'QListWidget',
        'QMenu',
        'QMenuBar',
        'QOpenGLWidget',
        'QPlainTextEdit',
        'QProgressBar',
        'QPushButton',
        'QRadioButton',
        'QScrollArea',
        'QScrollBar',
        'QSlider',
        'QSpinBox',
        'QSplitter',
        'QStackedWidget',
        'QStatusBar',
        'QTabWidget',
        'QTableView',
        'QTableWidget',
        'QTextBrowser',
        'QTextBrowser',
        'QTextEdit',
        'QTimeEdit',
        'QToolBar',
        'QToolBox',
        'QToolButton',
        'QTreeView',
        'QTreeWidget',
        'QUndoView',
        'QWebEngineView',
        'QWidget',
        'QWizard',
        'QWizardPage',
    ]

def cleanString(s,spaces_for_underscores=False):
    """cleans a string from special chars and spaces"""
    if spaces_for_underscores: s= s.strip().replace(' ','_')
    return "".join(x for x in s if x.isalnum() or x == '_')

def openFileExplorer(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

def fullPath(file,_dir=None):
    """returns full path and file name for given file
       if no _dir is provided, current dir is used
    """
    _dir = _dir or os.getcwd()
    return os.path.join(_dir,file)

def isFile(file,_dir=None):
    """returns True if file exists
       if no _dir is provided, current dir is used
    """
    return os.path.isfile(fullPath(file,_dir))

def replaceInFile(file, _from, _to):
    """ replaces all occurrences of _from to _to in given file """
    for line in fileinput.input(file, inplace=1):
        line = line.replace(_from, _to)
        sys.stdout.write(line)

def getUi_class(file):
    """returns Ui_"class" from compiled ui file"""
    with open(file,"r") as f:
        for line in f:
            if 'class' in line and 'Ui_' in line:
                start = line.index('Ui_')
                end = line.index('(')
                return line[start:end]

def deleteLineFromFile(file,string):
    """Deletes all lines matching string"""
    with io.open(file, "r", encoding='utf-8') as fp:
        lines = fp.readlines()

    with io.open(file, "w", encoding='utf-8') as fp:
        for line in lines:
            if string not in line:
                fp.write(line)

def removeQrcs(uiFile):
    try:
        parsed = xml.parse(uiFile)
    except:
        # returns error because it found:
        # </resources> closed tag
        # so we remove it
        deleteLineFromFile(uiFile,'</resources>')
        parsed = xml.parse(uiFile)

    resourcesElem = parsed.find('resources')
    if resourcesElem:
        parsed.getroot().remove(resourcesElem)
        xml.indent(parsed.getroot())
        parsed.write(uiFile,xml_declaration=True, encoding='UTF-8')

def addQrc(qrc,uiFile):
    """
        Params:
            qrc - filename = resource.qrc
            uiFile - full path to ui file

        Includes qrc file in ui file if not already present
        return True if included
        return False if was already included
    """
    try:
        parsed = xml.parse(uiFile)
    except:
        # returns error because it found:
        # </resources> closed tag
        # so we remove it
        deleteLineFromFile(uiFile,'</resources>')
        parsed = xml.parse(uiFile)

    resourcesElem = parsed.find('resources')
    if resourcesElem:
        for include in resourcesElem.findall('include'):
            if qrc==include.get('location'):
                # qrc already included
                return False
    else:
        resourcesElem = xml.Element('resources')
        parsed.getroot().append(resourcesElem)

    inc = xml.SubElement(resourcesElem,'include')
    inc.set('location',qrc)
    xml.indent(parsed.getroot())
    parsed.write(uiFile,xml_declaration=True, encoding='UTF-8')
    return True

def cleanQrc(uiFile):
    """
        Looks for included resources files in provided .ui file

        If it doesn't find any, it returns the original file else:
           Adds all search paths to Qt
           Converts all paths
                turns this> :/images/C:/Users/mindd/Desktop/CircleOfFifths.jpg
                into this>  images:CircleOfFifths.jpg
           Removes resources 'include' tag
           Creates and returns new _mpi.ui file or original
    """

    # uiFile = os.path.join(os.getcwd(),uiFile)
    parsed = xml.parse(uiFile)

    # No resource.qrc files found
    # we return the original file
    if parsed.find('resources') is None: return uiFile

    # Add search paths
    for include in parsed.iter('include'):
        location = include.get('location')# qrc file
        if 'qrc' in location:
            qrcFile = xml.parse(location)
            for qresource in qrcFile.iter('qresource'):
                prefix = qresource.get('prefix')# prefix
                for file in qresource.findall('file'):
                    QDir.addSearchPath(prefix, os.path.dirname(file.text))
                    # print(location,prefix, file.text)

    # fix resources paths
    def fixPath(path):
        """
            turns this> :/images/C:/Users/mindd/Desktop/CircleOfFifths.jpg
            into this>  images:CircleOfFifths.jpg
        """
        path = path.replace(':/','')
        s = path.index('/')
        e = path.rindex('/')
        path = path.replace(path[s:e+1],':')
        return path

    for _any in parsed.iter():
        txt = _any.text
        if txt:
            txt = txt.strip()
            if txt != '' and txt.count(':/'):
                newTxt = txt
                if 'url' in txt:# StyleSheet
                    # All occurrences of 'url(:' in string
                    for i in range(len(txt)):
                        if txt.startswith('url(:', i):
                            all_from_here = txt[i:]
                            start = all_from_here.index(':/')
                            end = all_from_here.index(')')
                            actual_txt = all_from_here[start:end]
                            newTxt = newTxt.replace(actual_txt,fixPath(actual_txt))
                else:
                    newTxt = newTxt.replace(txt,fixPath(txt))
                _any.text = newTxt

    if parsed.find('resources') is not None:
        parsed.getroot().remove(parsed.find('resources'))

    mpi_file = uiFile.replace('.ui','_mpi.ui')
    xml.indent(parsed.getroot())
    parsed.write(mpi_file)
    return mpi_file

def compileUi(ui_file,py_file=None):
    """
        Function to compile .ui files to .py files

        Runs cleanQrc()
            Adds Qt search paths if .qrc file is included
            Removes any _rc imports like:
                import resources_rc

            more: help(cleanQrc)

        based on:
        http://stackoverflow.com/a/14195313/3781327

        usage:
        compileUi('myUi.ui','myUi.py')
        compileUi('myUi.ui')
    """
    if not isFile(ui_file):
        raise ValueError('MadQt.Tools.compileUi: Provided .ui file not found!')

    ui_file = cleanQrc(ui_file)

    uipy = subprocess.check_output(['pyside6-uic', ui_file],
        shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    if '_mpi.ui' in ui_file:
        py_file = py_file or ui_file.replace('_mpi.ui','.py')
    else:
        py_file = py_file or ui_file.replace('.ui','.py')

    # print(ui_file)
    try:
        # Write the file
        with open(py_file, 'w') as f:
            f.write(uipy.decode("utf-8"))
        return True
    except:
        return False

def getFiles(*args, **kwargs):
    """
        Gets all files in _dir
        Filters files by extension using 'ext' - .py
        Filters files by name using 'name' in filename
        Excludes files containing 'exc' - string or list of strings
        if 'full':
            Yields full path, file name and extension
        else:
            Yields file name with no extension

        Params:
            name=None (in name)
            ext=None (extension to retrieve)
            exc=None (name/s to exclude)
            rec=False (recursive)
            _dir=None (or current dir)
            full=False (full path)

        Return list[str]

        Examples:
        print(getFiles(ext='.py',exc=['__init__','-'],full=True))
        # print(getFiles(ext='.py',exc='__init__'))
    """
    name = kwargs.get('name')
    ext = kwargs.get('ext')
    exc = kwargs.get('exc')
    rec = kwargs.get('rec')
    _dir = kwargs.get('_dir',os.getcwd())
    full = kwargs.get('full',True)

    al = len(args)
    if al: name=args[0]
    if al>1: ext=args[1]
    if al>2: exc=args[2]
    if al>3: rec=args[3]
    if al>4: _dir=args[4]
    if al>5: full=args[5]

    def loop_files(files,root):
        for file in files:
            file_name, file_ext = os.path.splitext(file)
            if ext:
                if not file.endswith(ext):continue
            if name:
                if name not in file_name:continue
            if exc:
                if isinstance(exc,list):
                    if any([e in file_name for e in exc]):continue
                else:
                    if exc in file_name:continue
            if full:
                yield os.path.join(root,file)
            else:
                yield file_name
    if rec:
        rsl=[]
        for root, dirs, files in os.walk(cdir):
            [rsl.append(r) for r in loop_files(files,root)]
        return rsl
    else:
        return list(loop_files(os.listdir(_dir),_dir))

def loadUi(ui,win=None):
    win_provided = win is not None
    ui = cleanQrc(ui)
    setup_class, window_class = loadUiType(ui)
    win = win or window_class()
    setup = setup_class()
    setup.setupUi(win)
    if win_provided:
        return setup
    else:
        return setup, win

def compileUiSimple(ui_file,py_file=None):
    if not isFile(ui_file):
        raise ValueError('MadQt.Tools.compileUiSimple: Provided .ui file not found!')
    py_file = ui_file.replace('.ui','.py') if not py_file else py_file
    subprocess.Popen(['pyside6-uic', ui_file, '-o', py_file],shell=True).wait()
    return py_file

def compileQrc(qrc,dest_dir=None,overwrite=True):
    """Compiles a qrc file
        ex:
        from resources.qrc
        creates dest_dir/resources_rc.py
    """
    src_dir = os.path.dirname(qrc)
    base_name = os.path.basename(qrc)
    dest_dir = src_dir if not dest_dir else dest_dir
    compiled_name = base_name.replace('.qrc','_rc.py')

    if not isFile(compiled_name) or overwrite:
        compiled_path = os.path.join(dest_dir,compiled_name)
        p_dir = os.getcwd()
        os.chdir(src_dir)
        # subprocess.Popen(['MadQt-rcc', base_name, '-o', compiled_path], shell=True).wait()
        subprocess.Popen(['pyside6-rcc', base_name, '-o', compiled_path], shell=True).wait()
        os.chdir(p_dir)
    return compiled_path

class App:
    """ Creates a QApplication and launches it.

        class MadQt.Tools.App
        MadQt.Tools.App()

        Parameters:
            name - str
            window - QMainWindow
            ui - str 'my_gui.ui'
            qrc - str 'resources.qrc'
            compile - bool (compile qrc and ui?)

    """
    def __init__(self, *args, **kwargs):
        # kwargs
        name = kwargs.get("name")
        window = kwargs.get("window")
        ui = kwargs.get("ui")
        qrc = kwargs.get("qrc")
        _compile = kwargs.get("compile")
        # args
        for arg in args:
            if isinstance(arg,str):
                if '.ui' in arg:
                    ui=arg
                elif '.qrc' in arg:
                    qrc=arg
                else:
                    name=arg
            elif isinstance(arg,bool):
                _compile=arg
            elif issubclass(arg,QWidget):
                window=arg

        # Set Attributes
        self.name = name or 'MadQt App'
        self.window = window or QMainWindow
        self.ui = self.ui_file = ui
        self.qrc = qrc

        # init
        self.app = QApplication.instance()
        self.app.setApplicationName(self.name)

        if self.qrc:
            if not isFile(self.qrc):
                raise ValueError('MadQt.App: Provided .qrc file not found!')

            if _compile: compileQrc(self.qrc)


        if not window:
            if ui:
                if not isFile(ui):
                    raise ValueError('MadQt.App: Provided .ui file not found!')
                if _compile:
                    compileUi(ui)
                    # import compiled py file as module
                    pyFileInported = importlib.import_module(ui.replace('.ui',''))
                    # get the Ui_ class from py file as string
                    uiClass = getUi_class(ui.replace('ui','py'))
                    # convert it to a construct able class
                    self.ui = getattr(pyFileInported, uiClass)
                    # Construct Ui_ class
                    self.ui = self.ui()
                    # Construct QMainWindow
                    self.window = self.window()
                    self.ui.setupUi(self.window)
                else:
                    self.ui, self.window = loadUi(ui)

            else: self.window = self.window()
        else: self.window = self.window()
        # self.window.setWindowTitle()
        self.window.show()
        self.app.aboutToQuit.connect(self.aboutToQuit)
        self.app.exec()

    def aboutToQuit(self):
        [os.remove(file) for file in getFiles('_mpi','.ui')]

    def __repr__(self):
        return " ".join(F"""App(
        name = {self.name},
        window = {self.window})
        """.split())



class Ui:
    """
        This class can handle ui file operations

        class MadQt.Tools.Ui

        MadQt.Tools.Ui(file, plugin_paths=None)

        Parameters:
            file - str
            plugin_paths - list


        Notes:
            custom_widgets can be plugins or promoted_widgets
            plugins are custom_widgets from the widget box
            promoted_widgets are custom_widgets made by user
    """
    def __init__(self,file,plugin_paths=None):
        self.file = file
        self.folder = os.path.dirname(self.file)
        self.basename = os.path.basename(self.file)
        self.filename,_ = os.path.splitext(self.basename)
        self.plugin_paths = []
        if plugin_paths:
            for path in plugin_paths:
                if os.path.isdir(path):
                    self.plugin_paths.append(path)
        if not self.plugin_paths: self.plugin_paths.append(self.folder)
        self.parse()


    def __repr__(self):
        return " ".join(F"""Ui(
        file = {self.file}
        """.split())

    def root(self):
        """returns xml root"""
        return self.parsed.getroot()

    def parse(self):
        try:
            self.parsed = xml.parse(self.file)
        except:
            # returns error because it found:
            # </resources> closed tag
            # so we remove it
            deleteLineFromFile(self.file,'</resources>')
            self.parsed = xml.parse(self.file)

    def get_class(self):
        """returns ui class"""
        return self.parsed.find('class').text

    def get_qt_class(self):
        """returns ui qt class QMainWindow | QWidget | QDialog"""
        return self.parsed.find('widget').get('class')

    def add_qrc(self,qrc):
        """add qrc resource if not added returns bool"""
        for inc in self.qrcs_includes():
            qrc_basename = os.path.basename(inc.get('location'))
            if qrc_basename==qrc:return False
        resources = self.parsed.find('resources')
        if not resources: resources = self.root().append(xml.Element('resources'))
        include = xml.Element('include')
        include.set('location',qrc)
        resources.append(include)
        return True

    def add_custom_widget(self,_class,qt_class,module):
        """adds a widget"""
        if self.has_custom_widget(_class):return False
        cws = self.parsed.find('customwidgets')
        if not cws: cws = self.root().append(xml.Element('customwidgets'))
        cw=xml.Element('customwidget')
        _c=xml.Element('class')
        _e=xml.Element('extends')
        _h=xml.Element('header')
        _c.text=_class
        _e.text=qt_class
        _h.text=module
        cw.append(_c)
        cw.append(_e)
        cw.append(_h)
        cws.append(cw)
        return True

    def qrcs_includes(self):
        """returns a list with all includes in resources"""
        resources = self.parsed.find('resources')
        if resources: return [inc for inc in resources.findall('include')]
        return []

    def get_parent(self,elem):
        """returns elem parent"""
        parent_map = {c: p for p in self.root().iter() for c in p}
        return parent_map[elem]

    def has_widget(self,_class):
        """checks if widget by the given class is in Ui"""
        return any(w.get('class')==_class for w in self.widgets())

    def widgets(self):
        """returns a list with all found widgets"""
        return self.parsed.iter('widget')

    def custom_widgets(self):
        """returns list with all custom widgets"""
        cws = self.parsed.find('customwidgets')
        if cws: return [cw for cw in cws.findall('customwidget')]
        return []

    def has_custom_widget(self,_class):
        return any(cw.find('class').text == _class for cw in self.custom_widgets())

    def promoted_widgets(self):
        """returns a list with all found promoted_widgets"""
        return [w for w in self.custom_widgets() if '.h' in w.find('header').text]

    def has_promoted_widget(self,_class):
        return any(cw.find('class').text == _class for cw in self.promoted_widgets())

    def plugins(self):
        """returns a list with all found plugins"""
        return [w for w in self.custom_widgets() if '.h' not in w.find('header').text]

    def imported_plugins(self):
        """returns a list with all found plugins that are imported"""
        return [w for w in self.plugins() if '.' in w.find('header').text]

    def not_imported_plugins(self):
        """returns a list with all found plugins that are imported"""
        return [w for w in self.plugins() if '.' not in w.find('header').text]

    def has_plugin(self,_class):
        return any(cw.find('class').text == _class for cw in self.plugins())

    def plugin_in_paths(self,cw):
        """checks if custom widget is in plugin_paths"""
        plugin = cw.find('header').text+'.py'
        for path in self.plugin_paths:
            for file in os.listdir(path):
                if file == plugin:
                    return True
        return False

    def can_import_plugin(self,cw):
        """None or False if it cant"""
        return packageHasMethod(cw.find('header').text,cw.find('class').text)

    def plugin_valid(self,cw):
        return self.plugin_in_paths(cw) or self.can_import_plugin(cw)

    def slots(self):
        """returns a list with all found slots"""
        slots = self.parsed.find('slots')
        if not slots:return []
        return [breakArgs(signal.text) for signal in slots.findall('slot')]

    def signals(self):
        """returns a list of tuples [(slot,args)] with all found signals"""
        slots = self.parsed.find('slots')
        if not slots:return []
        return [breakArgs(signal.text) for signal in slots.findall('signal')]

    def compile_qrcs(self,dest_path=None):
        """
            compiles all qrc files to given folder or ui folder _rc.py
            ! qrc must be in same folder as ui file
        """
        dest_path = dest_path if dest_path else self.folder
        for inc in self.qrcs_includes():
            qrc_basename = os.path.basename(inc.get('location'))
            qrc_file = os.path.join(self.folder,qrc_basename)
            compileQrc(qrc_file,dest_path)

    def compile(self,file=None,out_file=None,compile_qrcs=True):
        """compiles ui to py and returns py file"""
        if compile_qrcs:self.compile_qrcs()
        file = file if file else self.file
        out_file = out_file if out_file else file.replace('.ui','.py')
        subprocess.Popen(['pyside6-uic', file, '-o', out_file],shell=True).wait()
        return out_file

    def save(self, out_file=None):
        """writes/saves ui file"""
        out_file = out_file if out_file else self.file
        xml.indent(self.parsed.getroot())# prettify
        self.parsed.write(out_file, xml_declaration=True, encoding='UTF-8')# save
        return out_file

    def close(self):
        """
            removes invalid plugins
            compiles everything
            adds signals, slots and widget imports to compiled.py
        """
        # remove invalid plugins
        cws = self.parsed.find('customwidgets')
        removed_plugins = []
        removed_widgets = []
        if cws:
            # remove invalid plugins
            for plugin in self.plugins():
                if not self.plugin_valid(plugin):
                    cws.remove(plugin)
                    removed_plugins.append({
                        'class':plugin.find('class').text,
                        'module':plugin.find('header').text
                        })
                    for w in self.widgets():
                        if w.get('class')==plugin.find('class').text:
                            removed_widgets.append(w.attrib)
                            self.get_parent(w).remove(w)

        ui_file = self.save(os.path.join(tempDir(),'temp.ui'))
        out_file = self.file.replace('.ui','.py')
        py_file = self.compile(ui_file,out_file)

        # Add Ui class to compiled py file
        with open(py_file,"a") as f:
            if len(self.signals()):f.write(F"from PySide6.QtCore import Signal\n")
            f.write(F"class Ui({self.get_qt_class()}):\n")
            [f.write(F"    {sig[0]} = Signal({sig[1]})\n") for sig in self.signals()]
            f.write(F"    def __init__(self):\n")
            f.write(F"        super().__init__()\n")
            f.write(F"        self.ui = Ui_{self.get_class()}()\n")
            f.write(F"        self.ui.setupUi(self)\n")
            [f.write(F"    def {slot[0]}(self,*a,**kw):pass\n") for slot in self.slots()]

        return {
            'compiled_file':py_file,
            'removed_plugins':removed_plugins,
            'removed_widgets':removed_widgets,
            # in paths but not importable
            'in_paths':[plugin.find('header').text for plugin in self.not_imported_plugins() if self.plugin_in_paths(plugin)],
            'promoted_widgets':[pw.find('header').text.replace('.h','') for pw in self.promoted_widgets()]
            }
