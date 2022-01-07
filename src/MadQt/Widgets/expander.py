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
"""
Widget: Expander
Version: 0.0.1

Contributors: Fabio Goncalves
Email: fabiogoncalves@live.co.uk

Description: A Expandable and animated container
"""
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Expander(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._animFrom = QSize(100,100)
        self._animTo = QSize(150,100)
        self._animVal = QSize(100,100)
        self._expanded = False
        self._animateWidth = True
        self._animateHeight = False
        self._animateOnHover = True

        self._curve = 35
        self._loop = False
        self._duration = 250
        self._period = None
        self._amplitude = None
        self._overshoot = None

        self._anim = QPropertyAnimation(self, b'animVal')
        self._anim.setEasingCurve(QEasingCurve.Type(self._curve))
        self._anim.setStartValue(self._animFrom)
        self._anim.setEndValue(self._animTo)

    @Property(QSize, stored=False, designable=False)
    def animVal(self):
        return self._animVal

    @animVal.setter
    def animVal(self, val):
        self._animVal = val
        if self._animateWidth:self.setFixedWidth(val.width())
        if self._animateHeight:self.setFixedHeight(val.height())


    @Slot(QSize)
    def setAnimFrom(self, new_animFrom):
        self._animFrom = new_animFrom
        self._anim.setStartValue(new_animFrom)

    def getAnimFrom(self):
        return self._animFrom

    @Slot(QSize)
    def setAnimTo(self, new_animTo):
        self._animTo = new_animTo
        self._anim.setEndValue(new_animTo)

    def getAnimTo(self):
        return self._animTo

    @Slot(bool)
    def setExpanded(self, expand=True):
        self._expanded = expand
        if expand:
            self._anim.setDirection(self._anim.Forward)
        else:
            self._anim.setDirection(self._anim.Backward)

        if self._anim.state() == self._anim.State.Stopped:
            self._anim.start()

    def getExpanded(self):
        return self._expanded

    @Slot(bool)
    def setAnimateWidth(self, anim=True):
        self._animateWidth = anim

    def getAnimateWidth(self):
        return self._animateWidth

    @Slot(bool)
    def setAnimateHeight(self, anim=True):
        self._animateHeight = anim

    def getAnimateHeight(self):
        return self._animateHeight

    @Slot(bool)
    def setAnimateOnHover(self, anim=True):
        self._animateOnHover = anim

    def getAnimateOnHover(self):
        return self._animateOnHover

    def minimumSizeHint(self):
        return QSize(100, 100)

    def sizeHint(self):
        return QSize(100, 100)

    def enterEvent(self, event):
        if self.animateOnHover:
            self.setExpanded(True)

    def leaveEvent(self, event):
        if self.animateOnHover:
            self.setExpanded(False)

    @Property(int)
    def curve(self):
        return self._curve

    @curve.setter
    def curve(self,val):
        self._curve = val
        self._anim.setEasingCurve(QEasingCurve.Type(val))

    @Property(bool, designable=False)
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self,val):
        self._loop = val
        if val:
            self._anim.setLoopCount(-1)
        else:
            self._anim.setLoopCount(1)

    @Property(int, designable=False)
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self,val):
        self._duration = val
        self._anim.setDuration(val)

    @Property(float, designable=False)
    def period(self):
        return self._period

    @period.setter
    def period(self,val):
        if not val:return
        curve = self._anim.easingCurve()
        curve.setPeriod(val)
        self._period = val
        self._anim.setEasingCurve(curve)

    @Property(float, designable=False)
    def amplitude(self):
        return self._amplitude

    @amplitude.setter
    def amplitude(self,val):
        if not val:return
        curve = self._anim.easingCurve()
        curve.setAmplitude(val)
        self._amplitude = val
        self._anim.setEasingCurve(curve)

    @Property(float, designable=False)
    def overshoot(self):
        return self._overshoot

    @overshoot.setter
    def overshoot(self,val):
        if not val:return
        curve = self._anim.easingCurve()
        curve.setOvershoot(val)
        self._overshoot = val
        self._anim.setEasingCurve(curve)

    expanded = Property(bool, getExpanded, setExpanded)
    animateOnHover = Property(bool, getAnimateOnHover, setAnimateOnHover)
    animFrom = Property(QSize, getAnimFrom, setAnimFrom)
    animTo = Property(QSize, getAnimTo, setAnimTo)
    animateWidth = Property(bool, getAnimateWidth, setAnimateWidth)
    animateHeight = Property(bool, getAnimateHeight, setAnimateHeight)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = QWidget()

    QHBoxLayout(window)
    label = QLabel('  Hello  ')
    label.setStyleSheet("background-color:gray;")

    expander = Expander()
    expander.setStyleSheet("background-color:gray;")
    QVBoxLayout(expander)
    expander.layout().setContentsMargins(0,0,0,0)
    expander.layout().addWidget(QLabel('Expandable'))
    # expander.setAnimateHeight(False)

    window.layout().addWidget(label)
    window.layout().addWidget(expander)

    window.show()
    sys.exit(app.exec())
