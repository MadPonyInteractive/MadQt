#############################################################################
    ##
    ## Copyright (C) 2021 The Qt Company Ltd.
    ## Contact: http://www.qt.io/licensing/
    ##
    ## This file is part of the Qt for Python examples of the Qt Toolkit.
    ##
    ## $QT_BEGIN_LICENSE:BSD$
    ## You may use this file under the terms of the BSD license as follows:
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
#############################################################################
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Template(QWidget):
    currentIndexChanged = Signal(int)
    pageNameChanged = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)

        #PROPERTY_VALUES#
        self._pages = []
        self._currentIndex = -1

        # Creating main layout
        l=QVBoxLayout(self)
        l.setContentsMargins(0,0,0,0)
        l.setSpacing(0)

        # Creating prev/next button layout
        bl=QBoxLayout(QBoxLayout.LeftToRight)

        # Adding previous button
        pb=QToolButton(self)
        # Using __qt__passive_ prefix to make sure
        # the button works in QtDesigner
        pb.setObjectName('__qt__passive_prevButton')
        pb.setText('<')
        pb.clicked.connect(self.previousPage)
        bl.addWidget(pb)

        # Adding next button
        nb=QToolButton(self)
        nb.setObjectName('__qt__passive_nextButton')
        nb.setText('>')
        nb.clicked.connect(self.nextPage)
        bl.addWidget(nb)

        # Adding buttons layout to main layout
        l.addLayout(bl)
        l.setAlignment(bl,Qt.AlignRight)

    #PROPERTY_SETTER#

    #PROPERTY_GETTER#

    @Slot()# this will insure this method will show in QtDesigner slots
    def nextPage(self):
        """
            Sets next page, if current page is last page,
            it sets current page as page 0
        """
        ci = self.getCurrentIndex()
        index = 0 if ci == self.count()-1 else ci+1
        self.setCurrentIndex(index)

    @Slot()
    def previousPage(self):
        """
            Sets previous page, if current page is first page,
            it sets current page as last page
        """
        ci = self.getCurrentIndex()
        index = self.count()-1 if ci == 0 else ci-1
        self.setCurrentIndex(index)

    def displayPage(self, index):
        """displays requested page"""
        for i, p in enumerate(self._pages):
            if i == index:
                self.layout().addWidget(p)
                p.show()
            else:
                self.layout().removeWidget(p)
                p.hide()

    def pageExists(self, index):
        return index < self.count() and index != -1

    def canRemovePage(self, index):
        return self.pageExists(index) and self.count()

    @Slot(int, QWidget)
    def insertPage(self, index, page=None):
        """
            Inserts page into requested index

            This method is requested by the Container extension
            page is a QWidget added by QtDesigner and it's parent
            is self (this widget).
        """
        if not page:page = QWidget()

        # Adding given page to the layout
        self.layout().addWidget(page)

        # getting the object name, if None we set it
        objName = page.objectName()
        if objName == "":
            objName = "Page %d" % (self.count() + 1)
            page.setObjectName(objName)

        # Inserting page into our page list
        self._pages.insert(index, page)

        self.setCurrentIndex(index)
        self.setPageName(objName)

        return page

    @Slot(QWidget)
    def addPage(self, page=None):
        if not page: page = QWidget()
        return self.insertPage(self.count(), page)

    def removePage(self, index):
        if not self.canRemovePage(index): return
        newIndex = max(self.getCurrentIndex()-1,0)
        self._pages.pop(index)
        self.setCurrentIndex(newIndex)

    def widget(self, index):
        return self._pages[index] if self._pages else None

    def currentPage(self):
        ci=self.getCurrentIndex()
        if self.pageExists(ci):
            return self._pages[ci]

    def getCurrentIndex(self):
        return self._currentIndex

    @Slot(int)
    def setCurrentIndex(self, index):
        index = min(max(index,0),self.count()-1)
        if index != self.getCurrentIndex():
            self._currentIndex = index
            self.displayPage(index)
            self.currentIndexChanged.emit(index)

    def getPageName(self):
        cp = self.currentPage()
        if cp: return cp.objectName()

    @Slot(str)
    def setPageName(self, newName):
        cp = self.currentPage()
        if cp:
            cp.setObjectName(newName)
            self.pageNameChanged.emit(newName)

    def count(self):
        return len(self._pages)

    def minimumSizeHint(self):
        return QSize(140, 140)

    def sizeHint(self):
        return QSize(140, 140)

    currentIndex = Property(int, getCurrentIndex, setCurrentIndex)
    currentPageName = Property(str, getPageName, setPageName, stored=False)
    #PROPERTY_ASSIGN#

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Template()

    # Adding page 1
    page1=window.addPage()
    # Adding a button to page 1
    QPushButton('Page 1 Button',page1)

    # Adding page 2
    page2=window.addPage()
    # Adding a button to page 2
    QPushButton('Page 2 Button',page2)

    # Setting widget to page 1
    window.setCurrentIndex(0)

    window.show()
    sys.exit(app.exec())
