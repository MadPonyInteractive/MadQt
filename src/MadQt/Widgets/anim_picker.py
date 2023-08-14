#############################################################################
    ##
    ## Copyright (C) 2010 Riverbank Computing Limited.
    ## Copyright (C) 2021 The Qt Company Ltd.
    ## Contact: http://www.qt.io/licensing/
    ##
    ## This file is based of the Qt for Python examples of the Qt Toolkit.
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
Widget: AnimPicker
Version: 1.0.0

Contributors: Fabio Goncalves
Email: fabiogoncalves@live.co.uk

Description: 
AnimPicker is a QDialog based on the PySide6 QEasing animation example
that allows for a user to pick animation parameters.

You can find the original example here:
Python\\Lib\\site-packages\\PySide6\\examples\\widgets\\animation\\easing

"""
from PySide6.QtCore import (Property, QEasingCurve, QObject, QPropertyAnimation,
                            QPoint, QPointF, QRect, QRectF, QSize, Qt)
from PySide6.QtGui import (QBrush, QColor, QIcon, QLinearGradient, QPainter,
                           QPainterPath, QPen, QPixmap, QGradient)
from PySide6.QtWidgets import *

# PySide6 doesn't support deriving from more than one wrapped class so we use
# composition and delegate the property.
class Ellipse(QObject):
    def __init__(self):
        super().__init__()

        self._item = QGraphicsEllipseItem(0,0,32,32)
        self._item.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
        self._item.setBrush(QBrush(QGradient.SaintPetersburg))

    def set_pos(self, pos):
        self._item.setPos(pos)

    def get_pos(self):
        return self._item.pos()

    pos = Property(QPointF, get_pos, set_pos)

class AnimPicker(QDialog):
    """This is the pop up dialog"""
    def __init__(self,
        curve=35,
        loop=True,
        duration=2000,
        period=None,
        amplitude=None,
        overshoot=None,
        parent=None):
        super().__init__(parent)
        self.setWindowTitle('Animation Picker')
        self._curve = curve
        self._loop = loop
        self._duration = duration
        self._period = period
        self._amplitude = amplitude
        self._overshoot = overshoot
        self._iconSize = QSize(88, 88)
        l = QVBoxLayout(self)

        controlsLayout = QHBoxLayout()
        l.addLayout(controlsLayout,1)

        self.periodSpinBox = QDoubleSpinBox(self)
        self.periodSpinBox.setMinimum(-1.0)
        self.periodSpinBox.setSingleStep(0.1)
        self.periodSpinBox.setEnabled(False)

        self.amplitudeSpinBox = QDoubleSpinBox(self)
        self.amplitudeSpinBox.setMinimum(-1.0)
        self.amplitudeSpinBox.setSingleStep(0.1)
        self.amplitudeSpinBox.setEnabled(False)

        self.overshootSpinBox = QDoubleSpinBox(self)
        self.overshootSpinBox.setMinimum(-1.0)
        self.overshootSpinBox.setSingleStep(0.1)
        self.overshootSpinBox.setEnabled(False)

        dummy = QEasingCurve()
        self._period = self._period or dummy.period()
        self._amplitude = self._amplitude or dummy.amplitude()
        self._overshoot = self._overshoot or dummy.overshoot()
        self.periodSpinBox.setValue(self._period)
        self.amplitudeSpinBox.setValue(self._amplitude)
        self.overshootSpinBox.setValue(self._overshoot)

        self.durationSpinBox = QSpinBox(self)
        self.durationSpinBox.setMaximum(100000)
        self.durationSpinBox.setValue(self._duration)
        self.durationSpinBox.setSingleStep(100)

        self.loopAnim = QPushButton('Loop')
        self.loopAnim.setCheckable(True)
        self.loopAnim.setChecked(self._loop)

        spinBoxLayout = QFormLayout()
        spinBoxLayout.insertRow(0,'Period',self.periodSpinBox)
        spinBoxLayout.insertRow(1,'Amplitude',self.amplitudeSpinBox)
        spinBoxLayout.insertRow(2,'Overshoot',self.overshootSpinBox)
        spinBoxLayout.insertRow(3,'Duration',self.durationSpinBox)
        spinBoxLayout.insertRow(4,self.loopAnim)
        controlsLayout.addLayout(spinBoxLayout)


        self.easingCurvePicker = QListWidget()
        self.easingCurvePicker.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.easingCurvePicker.setMovement(QListView.Static)
        self.easingCurvePicker.setWrapping(False)
        self.easingCurvePicker.setViewMode(QListView.IconMode)
        self.easingCurvePicker.setSelectionRectVisible(False)
        self.easingCurvePicker.setIconSize(self._iconSize)
        self.easingCurvePicker.setMinimumHeight(self._iconSize.height())
        controlsLayout.addWidget(self.easingCurvePicker)

        self.create_curve_icons()

        self._item = Ellipse()
        scene=QGraphicsScene(self)
        scene.addItem(self._item._item)
        left_line = QGraphicsLineItem(80,0,80,34)
        right_line = QGraphicsLineItem(432,0,432,34)
        scene.addItem(left_line)
        scene.addItem(right_line)

        self.graphicsView = QGraphicsView(scene,self)
        self.graphicsView.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.setFrameShape(QFrame.NoFrame)
        self.graphicsView.setFixedSize(560,36)
        self.graphicsView.setLayoutDirection(Qt.RightToLeft)
        self.graphicsView.setBackgroundBrush(Qt.gray)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        l.addWidget(self.graphicsView)

        self._anim = QPropertyAnimation(self._item, b'pos')
        self._anim.setEasingCurve(QEasingCurve.Type(self._curve))
        self.easingCurvePicker.setCurrentRow(self._curve)

        self.easingCurvePicker.currentRowChanged.connect(self.curve_changed)
        self.easingCurvePicker.itemClicked.connect(self._anim.start)
        self.easingCurvePicker.itemDoubleClicked.connect(self.accept)
        self.periodSpinBox.valueChanged.connect(self.period_changed)
        self.amplitudeSpinBox.valueChanged.connect(self.amplitude_changed)
        self.overshootSpinBox.valueChanged.connect(self.overshoot_changed)
        self.durationSpinBox.valueChanged.connect(self.duration_changed)
        self.loopAnim.clicked.connect(self.loop_changed)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        l.addWidget(button_box)

        self.start_animation()

    def sizeHint(self):
        return QSize(580, 200)

    def create_curve_icons(self):
        pix = QPixmap(self._iconSize)
        painter = QPainter()

        gradient = QLinearGradient(0, 0, 0, self._iconSize.height())
        gradient.setColorAt(0.0, QColor(240, 240, 240))
        gradient.setColorAt(1.0, QColor(224, 224, 224))

        brush = QBrush(gradient)
        curve_types = [(f"QEasingCurve.{e.name}", e) for e in QEasingCurve.Type if e.value <= 40]

        with QPainter(pix) as painter:

            for curve_name, curve_type in curve_types:
                painter.fillRect(QRect(QPoint(0, 0), self._iconSize), brush)
                curve = QEasingCurve(curve_type)

                painter.setPen(QColor(0, 0, 255, 64))
                x_axis = self._iconSize.height() / 1.5
                y_axis = self._iconSize.width() / 3.0
                painter.drawLine(0, x_axis, self._iconSize.width(), x_axis)
                painter.drawLine(y_axis, 0, y_axis, self._iconSize.height())

                curve_scale = self._iconSize.height() / 2.0

                painter.setPen(Qt.NoPen)

                # Start point.
                painter.setBrush(Qt.red)
                start = QPoint(y_axis,
                        x_axis - curve_scale * curve.valueForProgress(0))
                painter.drawRect(start.x() - 1, start.y() - 1, 3, 3)

                # End point.
                painter.setBrush(Qt.blue)
                end = QPoint(y_axis + curve_scale,
                        x_axis - curve_scale * curve.valueForProgress(1))
                painter.drawRect(end.x() - 1, end.y() - 1, 3, 3)

                curve_path = QPainterPath()
                curve_path.moveTo(QPointF(start))
                t = 0.0
                while t <= 1.0:
                    to = QPointF(y_axis + curve_scale * t,
                            x_axis - curve_scale * curve.valueForProgress(t))
                    curve_path.lineTo(to)
                    t += 1.0 / curve_scale

                painter.setRenderHint(QPainter.Antialiasing, True)
                painter.strokePath(curve_path, QColor(32, 32, 32))
                painter.setRenderHint(QPainter.Antialiasing, False)

                item = QListWidgetItem()
                item.setIcon(QIcon(pix))
                item.setText(curve_name)
                self.easingCurvePicker.addItem(item)



    def start_animation(self):
        self._anim.setStartValue(QPointF(80, 2))
        self._anim.setEndValue(QPointF(400, 2))
        self._anim.setDuration(self._duration)
        loop = 1
        if self._loop:loop = -1
        self._anim.setLoopCount(loop)
        self._anim.start()

    def curve_changed(self, row):
        curve_type = QEasingCurve.Type(row)
        self._curve = row
        self._anim.setEasingCurve(curve_type)
        self._anim.setCurrentTime(0)

        is_elastic = (curve_type >= QEasingCurve.InElastic
                    and curve_type <= QEasingCurve.OutInElastic)
        is_bounce = (curve_type >= QEasingCurve.InBounce
                    and curve_type <= QEasingCurve.OutInBounce)

        self.periodSpinBox.setEnabled(is_elastic)
        self.amplitudeSpinBox.setEnabled(is_elastic or is_bounce)
        self.overshootSpinBox.setEnabled(curve_type >= QEasingCurve.InBack
                                          and curve_type <= QEasingCurve.OutInBack)

    def period_changed(self, value):
        curve = self._anim.easingCurve()
        curve.setPeriod(value)
        self._period = value
        self._anim.setEasingCurve(curve)

    def amplitude_changed(self, value):
        curve = self._anim.easingCurve()
        curve.setAmplitude(value)
        self._amplitude = value
        self._anim.setEasingCurve(curve)

    def overshoot_changed(self, value):
        curve = self._anim.easingCurve()
        curve.setOvershoot(value)
        self._overshoot = value
        self._anim.setEasingCurve(curve)

    def duration_changed(self, value):
        self._duration = value
        self._anim.setDuration(value)

    def loop_changed(self, value):
        self._anim.stop()
        self._loop = value
        if value:
            self._anim.setLoopCount(-1)
        else:
            self._anim.setLoopCount(1)
        self._anim.start()

    def setCurve(self,curve):
        self._curve = curve
        self.curve_changed(curve)

    def curve(self):
        return self._curve

    def loop(self):
        return self._loop

    def duration(self):
        return self._duration

    def period(self):
        if self.periodSpinBox.isEnabled():
            return self._period

    def amplitude(self):
        if self.amplitudeSpinBox.isEnabled():
            return self._amplitude

    def overshoot(self):
        if self.overshootSpinBox.isEnabled():
            return self._overshoot

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = QWidget()
    QHBoxLayout(w)

    def openDialog():
        dialog = AnimPicker(parent=w)
        if dialog.exec() == QDialog.Accepted:
            print(" ".join(F"""
                curve: {dialog.curve()} |
                loop: {dialog.loop()} |
                duration: {dialog.duration()} |
                period: {dialog.period()} |
                amplitude: {dialog.amplitude()} |
                overshoot: {dialog.overshoot()}
            """.split()))

    b=QPushButton('Open Animation Picker Dialog')
    b.clicked.connect(openDialog)
    w.layout().addWidget(b)
    w.show()
    sys.exit(app.exec())
