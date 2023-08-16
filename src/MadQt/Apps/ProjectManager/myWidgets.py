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
        self.marginsAnim = QPropertyAnimation(self, b"geometry")
        self.marginsAnim.setDuration(300)
        self.marginsAnim.setEasingCurve(QEasingCurve.Type.OutElastic)

    def enterEvent(self, event):
        self.marginsAnim.setDirection(self.marginsAnim.Direction.Forward)
        if self.marginsAnim.state() == self.marginsAnim.State.Stopped:
            rect = self.geometry()
            self.marginsAnim.setStartValue(rect)
            rect += QMargins(0, 10, 0, 0)
            self.marginsAnim.setEndValue(rect)
            if self.isEnabled():
                self.marginsAnim.start()
        QPushButton.enterEvent(self, event)

    def leaveEvent(self, event):
        self.marginsAnim.setDirection(self.marginsAnim.Direction.Backward)
        if (
            self.marginsAnim.state() == self.marginsAnim.State.Stopped
            and self.isEnabled()
        ):
            self.marginsAnim.start()
        QPushButton.leaveEvent(self, event)


class ToolButton(QToolButton):
    def __init__(self, *args, **kwargs):
        QToolButton.__init__(self, *args, **kwargs)
        self.tip = QLabel(getMainWindow())
        self.tip.setStyleSheet(
            " ".join(
                f"""
            color: rgb(219, 203, 189);
            background-color: rgb(135, 67, 29);
            padding: 10px;
            border: 2px solid #c87941;
            border-radius: 5px;
        """.split()
            )
        )

        self.opacityFx = QGraphicsOpacityEffect(self.tip)
        self.opacityFx.setOpacity(0)
        self.tip.setGraphicsEffect(self.opacityFx)
        self.opacityAnim = QPropertyAnimation(self.opacityFx, b"opacity")
        self.opacityAnim.setDuration(250)
        self.opacityAnim.setStartValue(0)
        self.opacityAnim.setEndValue(1)

        self.posAnim = QPropertyAnimation(self.tip, b"pos")
        self.posAnim.setDuration(400)
        self.posAnim.setEasingCurve(QEasingCurve.Type.OutElastic)

        self.animGroup = QParallelAnimationGroup(self.tip)
        self.animGroup.addAnimation(self.opacityAnim)
        self.animGroup.addAnimation(self.posAnim)

    def event(self, event):
        t = event.type()
        if t == QEvent.Type.ToolTip:
            return True
        elif t == QEvent.Type.Show or t == QEvent.Type.Leave:
            self.tip.hide()
        elif t == QEvent.Type.Enter:
            self.tip.setText(self.toolTip())
            self.tip.adjustSize()
            self.tip.show()
            gw = self.geometry().width()
            gh = self.geometry().height()
            x = self.pos().x()  # +gw+15
            y = self.pos().y()  # +gh*1.9

            if self.group().objectName() == "mainPageGroup":
                x = (x + gw * 0.8) - self.tip.geometry().width() * 0.5
                y += gh + 7
                self.posAnim.setStartValue(QPoint(x, y * 2))
            else:
                x += gw + 15
                y += gh * 1.9
                self.posAnim.setStartValue(QPoint(x * 2, y))
            self.posAnim.setEndValue(QPoint(x, y))

            if self.isEnabled():
                self.animGroup.start()
        return QToolButton.event(self, event)


class DragDrop(QAbstractItemView):
    dropped = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            mData = QMimeData()
            urls = []
            for item in self.selectedItems():
                if hasattr(item, "file"):
                    urls.append(QUrl.fromLocalFile(item.file))
            if len(urls):
                mData.setUrls(urls)
                drag = QDrag(self)
                drag.setMimeData(mData)
                drag.setHotSpot(
                    event.position().toPoint() - self.rect().topLeft()
                )
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


class ListView(QListWidget, DragDrop):
    def __init__(self, parent=None):
        super().__init__(parent)

    def getItems(self):
        return (self.item(i) for i in range(self.count()))

    def removeItem(self, file):
        for i, item in enumerate(self.getItems()):
            if item.file == file:
                self.takeItem(i)
                break

    def dragEnterEvent(self, event):
        DragDrop.dragEnterEvent(self, event)

    def dragMoveEvent(self, event):
        DragDrop.dragMoveEvent(self, event)

    def dropEvent(self, event):
        DragDrop.dropEvent(self, event)


class PathsList(ListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainWindow = getMainWindow()
        self.menu = QMenu("Paths Menu", self)
        self.menu.setCursor(Qt.PointingHandCursor)
        self.menu.addAction("Add", self.mainWindow.addPluginPath)
        self.menu.addAction("Delete", self.mainWindow.removePluginPath)

    def removeCurrentItem(self):
        for i, item in enumerate(self.getItems()):
            if item == self.currentItem():
                self.takeItem(i)
                return item

    def contextMenuEvent(self, event):
        underMouse = self.itemAt(event.pos())
        if underMouse is None:  # Empty area
            [
                action.setVisible(action.text() == "Add")
                for action in self.menu.actions()
            ]
        else:  # Item
            [
                action.setVisible(action.text() == "Delete")
                for action in self.menu.actions()
            ]
        self.menu.popup(event.globalPos())
        event.accept()


class TreeView(QTreeWidget, DragDrop):
    droppedQrc = Signal(list)
    droppedImg = Signal(dict)
    droppedModule = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.imgTypes = [".png", ".ico", ".jpg", ".gif", ".svg"]
        self.qrcParent = None
        self.prefixParent = None
        self.mainWindow = getMainWindow()

        # icons
        fileIcon = QIcon(":/icons/img/cil-file.png")
        folderIcon = QIcon(":/icons/img/cil-folder-open.png")
        pencilIcon = QIcon(":/icons/img/cil-pencil.png")
        refreshIcon = QIcon(":/icons/img/cil-loop-circular.png")
        imageIcon = QIcon(":/icons/img/cil-satelite.png")
        plusIcon = QIcon(":/icons/img/cil-plus.png")

        # menus
        self.popup = None
        self.tinted = False
        self.menu = QMenu("Menu", self)
        self.menu.setCursor(Qt.PointingHandCursor)

        self.menu.addAction(pencilIcon, "Open", self.open)
        self.menu.addAction(fileIcon, "New Module", self.mainWindow.newModule)
        self.menu.addAction(
            folderIcon, "Add Module", self.mainWindow.addModuleDialogue
        )
        self.menu.addAction(plusIcon, "Add Class", self.mainWindow.addClass)
        self.menu.addAction(
            folderIcon, "Add Images", self.mainWindow.addImagesDialogue
        )
        self.menu.addAction(
            folderIcon, "Add Prefix", self.mainWindow.addPrefix
        )
        self.menu.addAction(folderIcon, "Add Qrc", self.mainWindow.addQrc)
        self.menu.addAction(
            folderIcon, "Create Qrc", self.mainWindow.createQrc
        )
        self.menu.addAction(pencilIcon, "Tint", self.tint)
        self.menu.addAction(pencilIcon, "Multiply", self.multiply)
        self.menu.addAction(refreshIcon, "Restore", self.restore)
        self.menu.addAction(imageIcon, "Make ICO", self.makeIco)
        self.menu.addAction(imageIcon, "Set as project icon", self.setIcon)
        self.menu.addAction(fileIcon, "Rename", self.rename)
        self.menu.addAction(fileIcon, "Delete", self.delete)

    def mousePressEvent(self, event):
        QTreeWidget.mousePressEvent(self, event)
        si = self.selectedImages()
        sm = self.selectedModules()
        if si:
            selectedItems = si
        elif sm:
            selectedItems = sm
        else:
            return True
        if event.buttons() == Qt.LeftButton:
            mData = QMimeData()
            urls = []
            for item in selectedItems:
                if hasattr(item, "file"):
                    urls.append(QUrl.fromLocalFile(item.file))
            if len(urls):
                mData.setUrls(urls)
                drag = QDrag(self)
                drag.setMimeData(mData)
                drag.setHotSpot(
                    event.position().toPoint() - self.rect().topLeft()
                )
                Qt.DropAction = drag.exec(Qt.CopyAction)

    def removeTopLevelItem(self, item, col=0):
        self.takeTopLevelItem(self.indexOfTopLevelItem(item))

    def makeIco(self):
        self.mainWindow.makeIco(self.selectedImages())

    def tint(self):
        self.mainWindow.tintImagesDlg(self.selectedImages(), 0)

    def multiply(self):
        self.mainWindow.tintImagesDlg(self.selectedImages(), 1)

    def restore(self):
        self.mainWindow.restoreImages(self.selectedImages())

    def setIcon(self):
        self.mainWindow.setIcon(self.currentItem())

    def open(self):
        if self.popup == "module":
            self.mainWindow.openModule(self.currentItem())
        if self.popup == "class":
            self.mainWindow.openClass(self.currentItem())

    def delete(self):
        if self.popup == "qrc":
            self.mainWindow.deleteQrcs(self.selectedQrcs())
        if self.popup == "prefix":
            self.mainWindow.deletePrefixes(self.selectedPrefixes())
        if self.popup == "image":
            self.mainWindow.deleteImages(self.selectedImages())
        if self.popup == "module":
            self.mainWindow.deleteModules()

    def rename(self):
        if self.popup == "qrc":
            self.mainWindow.renameQrc(self.currentItem())  # rename prefix
        if self.popup == "prefix":
            self.mainWindow.addPrefix(add=False)  # rename prefix
        if self.popup == "image":
            self.mainWindow.renameImage(self.currentItem())  # rename prefix
        if self.popup == "module":
            self.mainWindow.renameModule(self.currentItem())  # rename prefix

    def enableActions(self, actions=None, state=True):
        for action in self.menu.actions():
            if actions:
                if action.text() not in actions:
                    continue
            action.setEnabled(state)

    def visibleActions(self, actions=None, state=True):
        for action in self.menu.actions():
            if actions:
                if action.text() not in actions:
                    continue
            action.setVisible(state)

    def selectedQrcs(self):
        """returns selected qrc files"""
        if self.objectName() == "qrcTree":
            return [i for i in self.selectedItems() if i.type() == 0]

    def selectedPrefixes(self):
        """returns selected prefixes"""
        if self.objectName() == "qrcTree":
            return [i for i in self.selectedItems() if i.type() == 1]

    def selectedImages(self):
        """returns selected images"""
        if self.objectName() == "qrcTree":
            return [si for si in self.selectedItems() if si.type() == 2]

    def selectedModules(self):
        """returns selected modules"""
        if self.objectName() == "moduleTree":
            return [i for i in self.selectedItems() if i.type() == 0]

    def selectedClasses(self):
        """returns selected classes"""
        if self.objectName() == "moduleTree":
            return [i for i in self.selectedItems() if i.type() == 1]

    def contextMenuEvent(self, event):
        underMouse = self.itemAt(event.pos())
        self.visibleActions(state=0)
        if self.objectName() == "qrcTree":
            if underMouse:
                if underMouse.type() == 2:  # image
                    self.popup = "image"
                    self.visibleActions(
                        [
                            "Restore",
                            "Rename",
                            "Delete",
                        ]
                    )
                    # if any image is tinted enable undo tint
                    self.enableActions(["Restore"], 0)
                    for img in self.selectedImages():
                        if ".ico" in img.file:
                            self.visibleActions(["Set as project icon"])
                        else:
                            self.visibleActions(
                                ["Tint", "Multiply", "Make ICO"]
                            )
                        if img.tinted:
                            self.enableActions(["Restore"])
                elif underMouse.type() == 1:  # prefix
                    self.popup = "prefix"
                    self.visibleActions(["Add Images", "Rename", "Delete"])
                elif underMouse.type() == 0:  # qrc
                    self.popup = "qrc"
                    self.visibleActions(["Add Prefix", "Rename", "Delete"])
            else:  # empty
                self.popup = None
                self.visibleActions(["Add Qrc", "Create Qrc"])
        else:  # moduleTree
            if underMouse:
                if underMouse.type() == 1:  # class
                    self.popup = "class"
                    if self.mainWindow.hasSublime():
                        self.visibleActions(["Open"])
                    else:
                        event.ignore()
                        return
                elif underMouse.type() == 0:  # module
                    self.popup = "module"
                    self.visibleActions(["Add Class", "Rename", "Delete"])
                    if self.mainWindow.hasSublime():
                        self.visibleActions(["Open"])
            else:  # empty
                self.popup = None
                self.visibleActions(["New Module", "Add Module"])
        self.menu.popup(event.globalPos())
        event.accept()

    def getUrls(self, event):
        return [str(url.toLocalFile()) for url in event.mimeData().urls()]

    def urlType(self, event):
        if not event.mimeData().hasUrls():
            return None
        extList = []
        for url in self.getUrls(event):
            ext = os.path.splitext(url)[1]
            if (
                ext not in extList
                and ext not in self.imgTypes
                and len(extList)
            ):
                return "multiple"
            extList.append(ext)
        if all([e == ".py" for e in extList]):
            return "module"
        if all([e == ".qrc" for e in extList]):
            return "qrc"
        if all([e in self.imgTypes for e in extList]):
            return "img"
        # if all([not len(e) for e in extList]):return 'folder'
        print(extList)
        return None

    def dragEnterEvent(self, event):
        DragDrop.dragEnterEvent(self, event)

    def dragMoveEvent(self, event):
        urlType = self.urlType(event)
        if not urlType or event.source():
            event.ignore()
            return
        elif (
            urlType == "img" or urlType == "qrc"
        ) and self.objectName() != "qrcTree":
            event.ignore()
            return
        elif urlType == "module" and self.objectName() != "moduleTree":
            event.ignore()
            return
        else:
            event.setDropAction(Qt.CopyAction)
            event.accept()

        hovered = self.itemAt(event.position().toPoint())
        # De-Select items
        for item in self.selectedItems():
            item.setSelected(0)
        shouldSelect = []

        if hovered:
            if self.objectName() == "qrcTree":
                self.mainWindow.ui.statusbar.showMessage("")
                self.prefixParent = None
                if hovered.type() == 2:  # hovered image
                    self.prefixParent = hovered.parent()
                    self.qrcParent = hovered.parent().parent()
                elif hovered.type() == 1:  # hovered prefix
                    self.prefixParent = hovered
                    self.qrcParent = hovered.parent()
                else:  # hovered qrc
                    self.qrcParent = hovered

                shouldSelect.append(self.qrcParent)
                if self.prefixParent:
                    shouldSelect.append(self.prefixParent)
                else:
                    self.mainWindow.ui.statusbar.showMessage(
                        "A new prefix will be created!"
                    )
        else:  # hovering empty area
            if self.topLevelItem(0):  # not empty
                if self.objectName() == "moduleTree":
                    shouldSelect.append(self.topLevelItem(0))
                elif self.objectName() == "qrcTree":
                    if urlType == "img":
                        qrc_file = self.topLevelItem(0)
                        shouldSelect.append(qrc_file)
                        self.qrcParent = qrc_file

                        first_prefix = qrc_file.child(0)
                        if first_prefix:
                            shouldSelect.append(first_prefix)
                            self.prefixParent = first_prefix
                        else:
                            self.prefixParent = None
                            self.mainWindow.ui.statusbar.showMessage(
                                "A new prefix will be created!"
                            )

        [si.setSelected(1) for si in shouldSelect]
        # DragDrop.dragMoveEvent(self, event)

    def dropEvent(self, event):
        urlType = self.urlType(event)
        if urlType and event.source() is None:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            if urlType == "img":
                self.droppedImg.emit(
                    {
                        "qrc": self.qrcParent,
                        "prefix": self.prefixParent,  # if None we need to create a 'newPrefix'
                        "imgs": self.getUrls(event),
                    }
                )
            if urlType == "qrc":
                self.droppedQrc.emit(self.getUrls(event))
            if urlType == "module":
                self.droppedModule.emit(self.getUrls(event))
        else:
            event.ignore()
