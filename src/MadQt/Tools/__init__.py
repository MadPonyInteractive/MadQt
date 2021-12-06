""" MadQt - Tutorials and Tools for PyQt and PySide

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
import sys, os, subprocess
import xml.etree.ElementTree as xml
from MadQt.Qt.QtWidgets import QApplication, QMainWindow, QWidget
from MadQt.Qt.QtCore import QDir
import MadQt

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

def getUi_class(file):
    with open(file,"r") as f:
        for line in f:
            if 'class' in line and 'Ui_' in line:
                start = line.index('Ui_')
                end = line.index('(')
                return line[start:end]

def cleanQrc(uiFile):
    """
        Looks for included resources files in provided .ui file

        If it doesn't found any, it returns the original file else:
           Adds all search paths to Qt
           Converts all paths
                turns this> :/images/C:/Users/mindd/Desktop/CircleOfFifths.jpg
                into this>  images:CircleOfFifths.jpg
           Removes resources 'include' tag
           Creates and returns new _mpi.ui file
    """
    parsed = xml.parse(uiFile)
    include_found=False
    # Add search paths
    for include in parsed.iter('include'):
        include_found=True
        location = include.get('location')# qrc file
        if 'qrc' in location:
            qrcFile = xml.parse(location)
            for qresource in qrcFile.iter('qresource'):
                prefix = qresource.get('prefix')# prefix
                for file in qresource.findall('file'):
                    QDir.addSearchPath(prefix, os.path.dirname(file.text))
                    # print(location,prefix, file.text)

    # No resource.qrc files found
    # we return the original file
    if not include_found: return uiFile

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

    mpi_file = uiFile.replace('.ui','.mpi')
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

    if 'PyQt' in MadQt.Qt.FRAMEWORK:
        uipy = subprocess.check_output(['pyuic'+MadQt.Qt.FRAMEWORK[-1], '-o', ui_file])
    else:
        uipy = subprocess.check_output([MadQt.Qt.FRAMEWORK.lower() + '-uic', ui_file])

    py_file = py_file or ui_file.replace('.mpi','.py')
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
    setup_class, window_class = MadQt.Qt.loadUiType(ui)
    win = win or window_class()
    setup = setup_class()
    setup.setupUi(win)
    if win_provided:
        return setup
    else:
        return setup, win


# TODO: TEST THIS
# DELETE C:\Users\mindd\AppData\Local\Programs\Python\Python310\Scripts\pyside6-rcc
# AND Try bellow
def compileQrc(qrc,_dir=None,overwrite=True):
    """Compiles a qrc file
        ex:
        from resources.qrc
        creates resources_rc.py
    """
    compiled_name, _ = os.path.splitext(qrc)
    compiled_name+='_rc.py'
    qrc = fullPath(qrc,_dir)
    if not isFile(compiled_name) or overwrite:
        p_dir = os.getcwd()
        _dir = os.path.dirname(MadQt.Tools.__file__)
        os.chdir(_dir)
        compiled_path = os.path.join(p_dir,compiled_name)
        subprocess.Popen(['pyside6-rcc', qrc, '-o', compiled_path], shell=True).wait()
        os.chdir(p_dir)

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
        self.app = MadQt.Qt.mkApp(self.name)

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
                    pyFileInported = __import__(ui.replace('.ui',''))
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
        if self.ui_file:
            os.remove(self.ui_file.replace('.ui','.mpi'))
        else:#look for .mpi files
            [os.remove(file) for file in getFiles(ext='.mpi')]

    def __repr__(self):
        return " ".join(F"""App(
        name = {self.name},
        window = {self.window})
        """.split())

