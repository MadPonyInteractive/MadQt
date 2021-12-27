from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import os

def getMainWindow():
    # for widget in QApplication.allWidgets():
    #     print(widget)
    for widget in QApplication.topLevelWidgets():
        if isinstance(widget, QMainWindow):
            return widget
    return None

class JumpButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.marginsAnim = QPropertyAnimation(self, b'geometry')
        self.marginsAnim.setDuration(300)
        self.marginsAnim.setEasingCurve(QEasingCurve.OutElastic)

    def enterEvent(self,event):
        self.marginsAnim.setDirection(self.marginsAnim.Forward)
        if self.marginsAnim.state() == self.marginsAnim.State.Stopped:
            rect = self.geometry()
            self.marginsAnim.setStartValue(rect)
            rect+=QMargins(0,10,0,0)
            self.marginsAnim.setEndValue(rect)
            if self.isEnabled():self.marginsAnim.start()
        QPushButton.enterEvent(self, event)

    def leaveEvent(self,event):
        self.marginsAnim.setDirection(self.marginsAnim.Backward)
        if self.marginsAnim.state() == self.marginsAnim.State.Stopped and self.isEnabled(): self.marginsAnim.start()
        QPushButton.leaveEvent(self, event)

class ToolButton(QToolButton):
    def __init__(self, *args, **kwargs):
        QToolButton.__init__(self, *args, **kwargs)
        self.tip = QLabel(getMainWindow())
        self.tip.setStyleSheet(" ".join(F"""
            color: rgb(219, 203, 189);
            background-color: rgb(135, 67, 29);
            padding: 10px;
            border: 2px solid #c87941;
            border-radius: 5px;
        """.split()))


        self.opacityFx = QGraphicsOpacityEffect(self.tip)
        self.opacityFx.setOpacity(0)
        self.tip.setGraphicsEffect(self.opacityFx)
        self.opacityAnim = QPropertyAnimation(self.opacityFx, b'opacity')
        self.opacityAnim.setDuration(250)
        self.opacityAnim.setStartValue(0)
        self.opacityAnim.setEndValue(1)

        self.posAnim = QPropertyAnimation(self.tip, b'pos')
        self.posAnim.setDuration(400)
        self.posAnim.setEasingCurve(QEasingCurve.OutElastic)

        self.animGroup = QParallelAnimationGroup(self.tip)
        self.animGroup.addAnimation(self.opacityAnim)
        self.animGroup.addAnimation(self.posAnim)

    def event(self,event):
        t=event.type()
        if t == QEvent.ToolTip:
            return True
        elif t == QEvent.Show or t == QEvent.Leave:
            self.tip.hide()
        elif t == QEvent.Enter:
            self.tip.setText(self.toolTip())
            self.tip.adjustSize()
            self.tip.show()
            gw=self.geometry().width()
            gh=self.geometry().height()
            x=self.pos().x()#+gw+15
            y=self.pos().y()#+gh*1.9

            if self.group().objectName() == 'mainPageGroup':
                x=(x+gw*.8)-self.tip.geometry().width()*.5
                y+=gh+7
                self.posAnim.setStartValue(QPoint(x,y*2))
            else:
                x+=gw+15
                y+=gh*1.9
                self.posAnim.setStartValue(QPoint(x*2,y))
            self.posAnim.setEndValue(QPoint(x,y))

            if self.isEnabled():self.animGroup.start()
        return QToolButton.event(self, event)

class DragDrop(QAbstractItemView):
    dropped = Signal(list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            mData = QMimeData()
            urls=[]
            for item in self.selectedItems():
                if hasattr(item,'file'):
                    urls.append(QUrl.fromLocalFile(item.file))
            if len(urls):
                mData.setUrls(urls)
                drag = QDrag(self)
                drag.setMimeData(mData)
                drag.setHotSpot(event.position().toPoint() - self.rect().topLeft())
                Qt.DropAction = drag.exec(Qt.CopyAction)
        return super().mousePressEvent(event)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls() and event.source() is None:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.dropped.emit(links)
        else:
            event.ignore()

class ListView(QListWidget,DragDrop):
    def __init__(self, parent=None):
        super().__init__(parent)

    def getItems(self):
        return (self.item(i) for i in range(self.count()))

    def removeItem(self,file):
        for i, item in enumerate(self.getItems()):
            if item.file == file:
                self.takeItem(i)
                break

    def dragEnterEvent(self, event):DragDrop.dragEnterEvent(self, event)
    def dragMoveEvent(self, event):DragDrop.dragMoveEvent(self, event)
    def dropEvent(self, event):DragDrop.dropEvent(self, event)

class PathsList(ListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainWindow = getMainWindow()
        self.menu = QMenu('Paths Menu',self)
        self.menu.setCursor(Qt.PointingHandCursor)
        self.menu.addAction('Add',self.mainWindow.addProperty)
        self.menu.addAction('Remove',self.mainWindow.removeProperty)

    def removeCurrentItem(self):
        for i, item in enumerate(self.getItems()):
            if item == self.currentItem():
                self.takeItem(i)
                return item

    def contextMenuEvent(self,event):
        underMouse = self.itemAt(event.pos())
        if underMouse is None:# Empty area
            [action.setVisible(action.text() == 'Add') for action in self.menu.actions()]
        else:# Item
            [action.setVisible(action.text() == 'Remove') for action in self.menu.actions()]
        self.menu.popup(event.globalPos())
        event.accept()
