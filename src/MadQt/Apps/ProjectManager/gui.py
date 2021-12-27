# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QComboBox,
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidgetItem, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QStatusBar, QTextEdit,
    QToolButton, QTreeWidgetItem, QVBoxLayout, QWidget)

from myWidgets import (JumpButton, ListView, PathsList, ToolButton,
    TreeView)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(611, 640)
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/images/img/mpi_logo_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	font: 600 14pt \"Dosis SemiBold\";\n"
"	color: rgb(219, 203, 189);\n"
"	background:transparent;\n"
"outline: none; \n"
"}\n"
"QAbstractScrollArea{\n"
"	background-color: transparent;\n"
"}\n"
"*[isTitle=\"true\"]{\n"
"	border-bottom:2px solid;\n"
"	color: rgb(41, 0, 1);\n"
"	font: 800 24pt \"Dosis ExtraBold\";\n"
"	padding-bottom:5px;\n"
"}\n"
"QMainWindow,QWidget#centralwidget,QStatusBar{\n"
"	background-color: qlineargradient(spread:pad, x1:0.42, y1:0, x2:0.528, y2:1, stop:0 rgba(135, 67, 29, 255), stop:1 rgba(41, 0, 1, 255));\n"
"	border-radius:10px;\n"
"}\n"
"QStatusBar{\n"
"	background-color: rgb(41, 0, 1);\n"
"}\n"
"QStatusBar::item {\n"
"    border: none;\n"
"}\n"
"QStatusBar QLabel#extraMsg {\n"
"	background-color: rgb(135, 67, 29);\n"
"}\n"
"QSizeGrip {\n"
"	image: url(:/icons/img/cil-size-grip.png);\n"
"     width: 16px;\n"
"     height: 16px;\n"
"	margin:0px 10px 10px 0px;\n"
"}\n"
"\n"
"QMenu {	\n"
"    border: 2px solid rgb(200, 121, 65);\n"
"	border-radius:3px;\n"
"	padding:5px;\n"
""
                        "}\n"
"\n"
"QMenu::item {\n"
"    /* sets background of menu item. set this to something non-transparent\n"
"        if you want menu color and menu item color to be different */\n"
"    background-color: transparent;\n"
"}\n"
"QMenu::item:selected {\n"
"	background-color: rgb(135, 67, 29);	\n"
"	color: rgb(219, 203, 189);\n"
"}\n"
"QMenu::item:disabled {\n"
"	background-color: rgb(219, 203, 189);\n"
"   	color: rgb(135, 67, 29);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.476864, y2:0, stop:0 rgba(41, 0, 1, 255), stop:0.670455 rgba(135, 67, 29, 255));\n"
"padding:4px;\n"
"border-radius:4px;\n"
"}\n"
"QAbstractButton:hover,QAbstractButton:pressed, QAbstractButton:checked {\n"
"	background-color: qlineargradient(spread:pad, x1:0.46, y1:1, x2:0.454136, y2:0.017, stop:0.420455 rgba(135, 67, 29, 255), stop:0.920455 rgba(200, 121, 65, 255));\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked{\n"
"border:2px solid rgb(200, 121, 65);\n"
"}\n"
"\n"
"QAbstract"
                        "Button:disabled{\n"
"	background-color: rgb(135, 67, 29);\n"
"	color: rgb(41, 0, 1);\n"
"}\n"
"QToolButton:disabled{\n"
"	background-color: rgb(135, 67, 29);\n"
"}\n"
"\n"
"QToolButton{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QToolButton:checked,QToolButton:pressed{\n"
"border-bottom:2px solid rgb(200, 121, 65);\n"
"}\n"
"QHeaderView::section {	\n"
"	color: rgb(200, 121, 65);\n"
"    border:none;\n"
" background:transparent;\n"
"}\n"
"\n"
"\n"
"QAbstractItemView::item{\n"
"padding:8px;\n"
"	color: rgb(219, 203, 189);\n"
"border-radius:8px;\n"
"margin-right:5px;\n"
"}\n"
"\n"
"QAbstractItemView::item:hover{\n"
"	border:1px solid rgb(219, 203, 189);\n"
"}\n"
"\n"
"QAbstractItemView::item:selected, QAbstractItemView::item:selected:active,QAbstractItemView::item:selected:!active{\n"
"	background-color: qlineargradient(spread:repeat, x1:0, y1:1, x2:0, y2:0, stop:0.0959821 rgba(135, 67, 29, 255), stop:0.151786 rgba(200, 121, 65, 255), stop:0.928571 rgba(174, 99, 51, 255), stop:1 rgba(135, 67, 29,"
                        " 255));\n"
"	color: rgb(41, 0, 1);\n"
"}\n"
"QListView::item{\n"
"border-bottom:1px solid #000;	\n"
"}\n"
"\n"
"QListView#designerPathsList::item{\n"
"padding:0px;\n"
"border:none;\n"
"margin:0px;\n"
"font-size:9pt;\n"
"}\n"
"\n"
"QComboBox, QLineEdit {\n"
"border:1px solid rgb(200, 121, 65);\n"
"}\n"
"QTextEdit,QLineEdit:focus, QComboBox::on, QComboBox QListView::item{\n"
"	background-color: rgb(41, 0, 1);\n"
"}\n"
"\n"
"\n"
"\n"
"QToolTip { 		\n"
"	font: 600 14pt \"Dosis SemiBold\";\n"
"    color: rgb(219, 203, 189);\n"
"    background-color: rgb(135, 67, 29);\n"
"    padding: 10px;\n"
"    border: 2px solid #c87941;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QAbstractSlider {	\n"
"	background-color: rgb(41, 0, 1);\n"
"}\n"
"QAbstractSlider::handle{\n"
"	background-color: rgb(135, 67, 29);\n"
"}\n"
"\n"
"QAbstractSlider:horizontal {\n"
"    border: none;\n"
"    height: 12px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QAbstractSlider::handle:horizontal {\n"
"    min-width: "
                        "25px;\n"
"}\n"
"QAbstractSlider::add-line:horizontal {\n"
"    border: none;\n"
"	border-left:2px solid rgba(255,255,255,120);\n"
"    background: rgba(0,0,0,80);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QAbstractSlider::sub-line:horizontal {\n"
"    border: none;\n"
"	border-right:2px solid rgba(255,255,255,120);\n"
"    background: rgba(0,0,0,80);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QAbstractSlider::up-arrow:horizontal, QAbstractSlider::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QAbstractSlider::add-page:horizontal, QAbstractSlider::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QAbstractSlider:vertical {\n"
"	border: none;	\n"
"    width: 12px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px"
                        ";\n"
" }\n"
" QAbstractSlider::handle:vertical {	\n"
"    min-height: 25px;\n"
" }\n"
" QAbstractSlider::add-line:vertical {\n"
"     border: none;\n"
"	border-top:2px solid rgba(255,255,255,120);\n"
"    background: rgba(0,0,0,80);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QAbstractSlider::sub-line:vertical {\n"
"	border: none;\n"
"	border-bottom:2px solid rgba(255,255,255,120);\n"
"    background:  rgba(0,0,0,80);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QAbstractSlider::up-arrow:vertical, QAbstractSlider::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QAbstractSlider::add-page:vertical, QAbstractSlider::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"QSlider::handle::horizontal{\n"
"width:25px;\n"
"}\n"
""
                        "QSlider::groove{\n"
"	background-color: rgb(41, 0, 1);\n"
"	border:1px solid rgb(135, 67, 29);\n"
"}\n"
"\n"
"")
        self.actionPotatoes = QAction(MainWindow)
        self.actionPotatoes.setObjectName(u"actionPotatoes")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setCursor(QCursor(Qt.SizeAllCursor))
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.TitleLyt = QVBoxLayout()
        self.TitleLyt.setSpacing(0)
        self.TitleLyt.setObjectName(u"TitleLyt")
        self.TitleLyt.setContentsMargins(-1, -1, -1, 0)
        self.mainTitle = QLabel(self.header)
        self.mainTitle.setObjectName(u"mainTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainTitle.sizePolicy().hasHeightForWidth())
        self.mainTitle.setSizePolicy(sizePolicy)
        self.mainTitle.setStyleSheet(u"font-size:22pt;")

        self.TitleLyt.addWidget(self.mainTitle)

        self.secTitle = QLabel(self.header)
        self.secTitle.setObjectName(u"secTitle")
        sizePolicy.setHeightForWidth(self.secTitle.sizePolicy().hasHeightForWidth())
        self.secTitle.setSizePolicy(sizePolicy)
        self.secTitle.setStyleSheet(u"font-size:12pt;")

        self.TitleLyt.addWidget(self.secTitle)


        self.horizontalLayout_3.addLayout(self.TitleLyt)

        self.startPageBtn = ToolButton(self.header)
        self.mainPageGroup = QButtonGroup(MainWindow)
        self.mainPageGroup.setObjectName(u"mainPageGroup")
        self.mainPageGroup.addButton(self.startPageBtn)
        self.startPageBtn.setObjectName(u"startPageBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.startPageBtn.sizePolicy().hasHeightForWidth())
        self.startPageBtn.setSizePolicy(sizePolicy1)
        self.startPageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startPageBtn.setIcon(icon1)
        self.startPageBtn.setIconSize(QSize(32, 32))
        self.startPageBtn.setCheckable(True)
        self.startPageBtn.setChecked(True)

        self.horizontalLayout_3.addWidget(self.startPageBtn)

        self.settBtn = ToolButton(self.header)
        self.mainPageGroup.addButton(self.settBtn)
        self.settBtn.setObjectName(u"settBtn")
        sizePolicy1.setHeightForWidth(self.settBtn.sizePolicy().hasHeightForWidth())
        self.settBtn.setSizePolicy(sizePolicy1)
        self.settBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/img/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settBtn.setIcon(icon2)
        self.settBtn.setIconSize(QSize(32, 32))
        self.settBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.settBtn)

        self.PpageBtn = ToolButton(self.header)
        self.mainPageGroup.addButton(self.PpageBtn)
        self.PpageBtn.setObjectName(u"PpageBtn")
        self.PpageBtn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.PpageBtn.sizePolicy().hasHeightForWidth())
        self.PpageBtn.setSizePolicy(sizePolicy1)
        self.PpageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/img/cil-clipboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PpageBtn.setIcon(icon3)
        self.PpageBtn.setIconSize(QSize(32, 32))
        self.PpageBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.PpageBtn)

        self.sublimePBtn = ToolButton(self.header)
        self.mainPageGroup.addButton(self.sublimePBtn)
        self.sublimePBtn.setObjectName(u"sublimePBtn")
        self.sublimePBtn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.sublimePBtn.sizePolicy().hasHeightForWidth())
        self.sublimePBtn.setSizePolicy(sizePolicy1)
        self.sublimePBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sublimePBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/img/sublime-text-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sublimePBtn.setIcon(icon4)
        self.sublimePBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.sublimePBtn)

        self.horizontalSpacer_7 = QSpacerItem(337, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.logo = QLabel(self.header)
        self.logo.setObjectName(u"logo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy2)
        self.logo.setMaximumSize(QSize(1000, 1000))
        self.logo.setCursor(QCursor(Qt.PointingHandCursor))
        self.logo.setPixmap(QPixmap(u":/images/img/mpi_logo_small.png"))

        self.horizontalLayout_3.addWidget(self.logo)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 4, -1, -1)
        self.closeBtn = QToolButton(self.header)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy2.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy2)
        self.closeBtn.setMaximumSize(QSize(16777215, 24))
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeBtn.setIconSize(QSize(8, 8))

        self.verticalLayout_2.addWidget(self.closeBtn)

        self.verticalSpacer_6 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.minimizeBtn = QToolButton(self.header)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        sizePolicy2.setHeightForWidth(self.minimizeBtn.sizePolicy().hasHeightForWidth())
        self.minimizeBtn.setSizePolicy(sizePolicy2)
        self.minimizeBtn.setMaximumSize(QSize(16777215, 24))
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeBtn.setIconSize(QSize(8, 8))

        self.verticalLayout_2.addWidget(self.minimizeBtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.header)

        self.mainPage = QStackedWidget(self.centralwidget)
        self.mainPage.setObjectName(u"mainPage")
        self.startPg = QWidget()
        self.startPg.setObjectName(u"startPg")
        self.verticalLayout_3 = QVBoxLayout(self.startPg)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ProjectsList = ListView(self.startPg)
        self.ProjectsList.setObjectName(u"ProjectsList")
        self.ProjectsList.setFocusPolicy(Qt.NoFocus)
        self.ProjectsList.setFrameShape(QFrame.NoFrame)
        self.ProjectsList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ProjectsList.setTabKeyNavigation(True)
        self.ProjectsList.setProperty("showDropIndicator", False)
        self.ProjectsList.setDragDropMode(QAbstractItemView.DropOnly)
        self.ProjectsList.setDefaultDropAction(Qt.IgnoreAction)
        self.ProjectsList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ProjectsList.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.ProjectsList)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.newP = JumpButton(self.startPg)
        self.newP.setObjectName(u"newP")
        self.newP.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/img/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newP.setIcon(icon5)
        self.newP.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.newP)

        self.addP = JumpButton(self.startPg)
        self.addP.setObjectName(u"addP")
        sizePolicy1.setHeightForWidth(self.addP.sizePolicy().hasHeightForWidth())
        self.addP.setSizePolicy(sizePolicy1)
        self.addP.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/img/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addP.setIcon(icon6)
        self.addP.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.addP)

        self.delSelectedP = JumpButton(self.startPg)
        self.delSelectedP.setObjectName(u"delSelectedP")
        sizePolicy1.setHeightForWidth(self.delSelectedP.sizePolicy().hasHeightForWidth())
        self.delSelectedP.setSizePolicy(sizePolicy1)
        self.delSelectedP.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/img/trash-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delSelectedP.setIcon(icon7)
        self.delSelectedP.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.delSelectedP)

        self.horizontalLayout_4.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.mainPage.addWidget(self.startPg)
        self.newProjectPg = QWidget()
        self.newProjectPg.setObjectName(u"newProjectPg")
        self.verticalLayout_5 = QVBoxLayout(self.newProjectPg)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.newProjectPg)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setProperty("isTitle", True)

        self.verticalLayout_5.addWidget(self.label_7)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(17)
        self.label = QLabel(self.newProjectPg)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.projectNameInput = QLineEdit(self.newProjectPg)
        self.projectNameInput.setObjectName(u"projectNameInput")
        self.projectNameInput.setFrame(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.projectNameInput)

        self.label_2 = QLabel(self.newProjectPg)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.NewPFolderName = QLineEdit(self.newProjectPg)
        self.NewPFolderName.setObjectName(u"NewPFolderName")
        self.NewPFolderName.setFrame(True)

        self.horizontalLayout.addWidget(self.NewPFolderName)

        self.newPFolder = QPushButton(self.newProjectPg)
        self.newPFolder.setObjectName(u"newPFolder")
        self.newPFolder.setMinimumSize(QSize(24, 0))
        self.newPFolder.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.newPFolder)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(8)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.newPIcon = QLabel(self.newProjectPg)
        self.newPIcon.setObjectName(u"newPIcon")
        self.newPIcon.setPixmap(QPixmap(u":/images/img/mpi_logo.ico"))

        self.horizontalLayout_20.addWidget(self.newPIcon)

        self.newPIconBrowse = QPushButton(self.newProjectPg)
        self.newPIconBrowse.setObjectName(u"newPIconBrowse")
        self.newPIconBrowse.setMinimumSize(QSize(24, 0))
        self.newPIconBrowse.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_20.addWidget(self.newPIconBrowse)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_20)

        self.label_29 = QLabel(self.newProjectPg)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_29)


        self.verticalLayout_5.addLayout(self.formLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.createP = JumpButton(self.newProjectPg)
        self.createP.setObjectName(u"createP")
        self.createP.setCursor(QCursor(Qt.PointingHandCursor))
        self.createP.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.createP)

        self.cancelCreateP = JumpButton(self.newProjectPg)
        self.cancelCreateP.setObjectName(u"cancelCreateP")
        self.cancelCreateP.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/img/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelCreateP.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.cancelCreateP)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.mainPage.addWidget(self.newProjectPg)
        self.projectPg = QWidget()
        self.projectPg.setObjectName(u"projectPg")
        self.verticalLayout_4 = QVBoxLayout(self.projectPg)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.PrjName = QLabel(self.projectPg)
        self.PrjName.setObjectName(u"PrjName")
        self.PrjName.setStyleSheet(u"")
        self.PrjName.setAlignment(Qt.AlignCenter)
        self.PrjName.setProperty("isTitle", True)

        self.verticalLayout_4.addWidget(self.PrjName)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.menu = QVBoxLayout()
        self.menu.setSpacing(0)
        self.menu.setObjectName(u"menu")
        self.menu.setContentsMargins(-1, 0, -1, 0)
        self.qrcPBtn = ToolButton(self.projectPg)
        self.ProjectPageBtnGroup = QButtonGroup(MainWindow)
        self.ProjectPageBtnGroup.setObjectName(u"ProjectPageBtnGroup")
        self.ProjectPageBtnGroup.addButton(self.qrcPBtn)
        self.qrcPBtn.setObjectName(u"qrcPBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.qrcPBtn.sizePolicy().hasHeightForWidth())
        self.qrcPBtn.setSizePolicy(sizePolicy3)
        self.qrcPBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.qrcPBtn.setStyleSheet(u"[checked=\"false\"]{\n"
"border:none;\n"
"}\n"
"\n"
":pressed,:checked{\n"
"border:none;\n"
"border-left:2px solid rgb(200, 121, 65);\\n\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/img/cil-satelite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.qrcPBtn.setIcon(icon9)
        self.qrcPBtn.setIconSize(QSize(32, 32))
        self.qrcPBtn.setCheckable(True)
        self.qrcPBtn.setChecked(True)

        self.menu.addWidget(self.qrcPBtn)

        self.uiFilesBtn = ToolButton(self.projectPg)
        self.ProjectPageBtnGroup.addButton(self.uiFilesBtn)
        self.uiFilesBtn.setObjectName(u"uiFilesBtn")
        sizePolicy3.setHeightForWidth(self.uiFilesBtn.sizePolicy().hasHeightForWidth())
        self.uiFilesBtn.setSizePolicy(sizePolicy3)
        self.uiFilesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.uiFilesBtn.setStyleSheet(u"[checked=\"false\"]{\n"
"border:none;\n"
"}\n"
"\n"
":pressed,:checked{\n"
"border:none;\n"
"border-left:2px solid rgb(200, 121, 65);\\n\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/img/cil-view-quilt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.uiFilesBtn.setIcon(icon10)
        self.uiFilesBtn.setIconSize(QSize(32, 32))
        self.uiFilesBtn.setCheckable(True)

        self.menu.addWidget(self.uiFilesBtn)

        self.custWidgetsBtn = ToolButton(self.projectPg)
        self.ProjectPageBtnGroup.addButton(self.custWidgetsBtn)
        self.custWidgetsBtn.setObjectName(u"custWidgetsBtn")
        sizePolicy3.setHeightForWidth(self.custWidgetsBtn.sizePolicy().hasHeightForWidth())
        self.custWidgetsBtn.setSizePolicy(sizePolicy3)
        self.custWidgetsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.custWidgetsBtn.setStyleSheet(u"[checked=\"false\"]{\n"
"border:none;\n"
"}\n"
"\n"
":pressed,:checked{\n"
"border:none;\n"
"border-left:2px solid rgb(200, 121, 65);\\n\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/img/widgets-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.custWidgetsBtn.setIcon(icon11)
        self.custWidgetsBtn.setIconSize(QSize(24, 32))
        self.custWidgetsBtn.setCheckable(True)

        self.menu.addWidget(self.custWidgetsBtn)

        self.execPBtn = ToolButton(self.projectPg)
        self.ProjectPageBtnGroup.addButton(self.execPBtn)
        self.execPBtn.setObjectName(u"execPBtn")
        self.execPBtn.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.execPBtn.sizePolicy().hasHeightForWidth())
        self.execPBtn.setSizePolicy(sizePolicy3)
        self.execPBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.execPBtn.setStyleSheet(u"[checked=\"false\"]{\n"
"border:none;\n"
"}\n"
"\n"
":pressed,:checked{\n"
"border:none;\n"
"border-left:2px solid rgb(200, 121, 65);\\n\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/img/cil-share.png", QSize(), QIcon.Normal, QIcon.Off)
        self.execPBtn.setIcon(icon12)
        self.execPBtn.setIconSize(QSize(32, 32))
        self.execPBtn.setCheckable(True)

        self.menu.addWidget(self.execPBtn)

        self.refreshBtn = ToolButton(self.projectPg)
        self.ProjectPageBtnGroup.addButton(self.refreshBtn)
        self.refreshBtn.setObjectName(u"refreshBtn")
        sizePolicy3.setHeightForWidth(self.refreshBtn.sizePolicy().hasHeightForWidth())
        self.refreshBtn.setSizePolicy(sizePolicy3)
        self.refreshBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshBtn.setStyleSheet(u"[checked=\"false\"]{\n"
"border:none;\n"
"}\n"
"\n"
":pressed,:checked{\n"
"border:none;\n"
"border-left:2px solid rgb(200, 121, 65);\\n\n"
"}\n"
"[checked=\"false\"]{\n"
"border-top:3px solid rgb(200, 121, 65);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/img/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshBtn.setIcon(icon13)
        self.refreshBtn.setIconSize(QSize(32, 32))

        self.menu.addWidget(self.refreshBtn)

        self.runBtn = ToolButton(self.projectPg)
        self.ProjectPageBtnGroup.addButton(self.runBtn)
        self.runBtn.setObjectName(u"runBtn")
        self.runBtn.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.runBtn.sizePolicy().hasHeightForWidth())
        self.runBtn.setSizePolicy(sizePolicy3)
        self.runBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.runBtn.setStyleSheet(u"[checked=\"false\"]{\n"
"border:none;\n"
"}\n"
"\n"
":pressed,:checked{\n"
"border:none;\n"
"border-left:2px solid rgb(200, 121, 65);\\n\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/img/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.runBtn.setIcon(icon14)
        self.runBtn.setIconSize(QSize(32, 32))
        self.runBtn.setCheckable(False)

        self.menu.addWidget(self.runBtn)

        self.openPFolder = ToolButton(self.projectPg)
        self.ProjectPageBtnGroup.addButton(self.openPFolder)
        self.openPFolder.setObjectName(u"openPFolder")
        sizePolicy3.setHeightForWidth(self.openPFolder.sizePolicy().hasHeightForWidth())
        self.openPFolder.setSizePolicy(sizePolicy3)
        self.openPFolder.setCursor(QCursor(Qt.PointingHandCursor))
        self.openPFolder.setStyleSheet(u"[checked=\"true\"]{\n"
"border:none;\n"
"}\n"
":pressed,:checked{\n"
"border-left:2px solid rgb(200, 121, 65);\\n\n"
"}\n"
"[checked=\"false\"]{\n"
"border-top:3px solid rgb(200, 121, 65);\n"
"}")
        self.openPFolder.setIcon(icon6)
        self.openPFolder.setIconSize(QSize(32, 32))

        self.menu.addWidget(self.openPFolder)

        self.saveAsBtn = ToolButton(self.projectPg)
        self.ProjectPageBtnGroup.addButton(self.saveAsBtn)
        self.saveAsBtn.setObjectName(u"saveAsBtn")
        sizePolicy3.setHeightForWidth(self.saveAsBtn.sizePolicy().hasHeightForWidth())
        self.saveAsBtn.setSizePolicy(sizePolicy3)
        self.saveAsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveAsBtn.setStyleSheet(u"[checked=\"false\"]{\n"
"border:none;\n"
"}\n"
"\n"
":pressed,:checked{\n"
"border:none;\n"
"border-left:2px solid rgb(200, 121, 65);\\n\n"
"}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/img/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveAsBtn.setIcon(icon15)
        self.saveAsBtn.setIconSize(QSize(32, 32))

        self.menu.addWidget(self.saveAsBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.menu.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.menu)

        self.PStackedWidget = QStackedWidget(self.projectPg)
        self.PStackedWidget.setObjectName(u"PStackedWidget")
        self.PPUi = QWidget()
        self.PPUi.setObjectName(u"PPUi")
        self.verticalLayout_6 = QVBoxLayout(self.PPUi)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.uiList = ListView(self.PPUi)
        self.uiList.setObjectName(u"uiList")
        self.uiList.setFocusPolicy(Qt.NoFocus)
        self.uiList.setFrameShape(QFrame.NoFrame)
        self.uiList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.uiList.setTabKeyNavigation(True)
        self.uiList.setProperty("showDropIndicator", False)
        self.uiList.setDragDropMode(QAbstractItemView.DropOnly)
        self.uiList.setDefaultDropAction(Qt.IgnoreAction)
        self.uiList.setSelectionMode(QAbstractItemView.MultiSelection)
        self.uiList.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.uiList)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.newUiBtn = JumpButton(self.PPUi)
        self.newUiBtn.setObjectName(u"newUiBtn")
        self.newUiBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newUiBtn.setIcon(icon5)
        self.newUiBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_14.addWidget(self.newUiBtn)

        self.addUiBtn = JumpButton(self.PPUi)
        self.addUiBtn.setObjectName(u"addUiBtn")
        self.addUiBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addUiBtn.setIcon(icon6)
        self.addUiBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_14.addWidget(self.addUiBtn)

        self.delSelectedUiBtn = JumpButton(self.PPUi)
        self.delSelectedUiBtn.setObjectName(u"delSelectedUiBtn")
        sizePolicy1.setHeightForWidth(self.delSelectedUiBtn.sizePolicy().hasHeightForWidth())
        self.delSelectedUiBtn.setSizePolicy(sizePolicy1)
        self.delSelectedUiBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delSelectedUiBtn.setIcon(icon7)
        self.delSelectedUiBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.delSelectedUiBtn)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.PStackedWidget.addWidget(self.PPUi)
        self.PPWgt = QWidget()
        self.PPWgt.setObjectName(u"PPWgt")
        self.verticalLayout_7 = QVBoxLayout(self.PPWgt)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.moduleTree = TreeView(self.PPWgt)
        self.moduleTree.setObjectName(u"moduleTree")
        self.moduleTree.setFocusPolicy(Qt.NoFocus)
        self.moduleTree.setFrameShape(QFrame.NoFrame)
        self.moduleTree.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.moduleTree.setTabKeyNavigation(True)
        self.moduleTree.setDragDropMode(QAbstractItemView.DropOnly)
        self.moduleTree.setDefaultDropAction(Qt.CopyAction)
        self.moduleTree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.moduleTree.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.moduleTree.setIconSize(QSize(32, 32))
        self.moduleTree.setAnimated(True)
        self.moduleTree.setHeaderHidden(True)
        self.moduleTree.header().setVisible(False)

        self.verticalLayout_7.addWidget(self.moduleTree)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.newModuleBtn = JumpButton(self.PPWgt)
        self.newModuleBtn.setObjectName(u"newModuleBtn")
        self.newModuleBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.newModuleBtn.setIcon(icon5)
        self.newModuleBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_16.addWidget(self.newModuleBtn)

        self.addModuleBtn = JumpButton(self.PPWgt)
        self.addModuleBtn.setObjectName(u"addModuleBtn")
        self.addModuleBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addModuleBtn.setIcon(icon6)
        self.addModuleBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_16.addWidget(self.addModuleBtn)

        self.delSelectedMods = JumpButton(self.PPWgt)
        self.delSelectedMods.setObjectName(u"delSelectedMods")
        sizePolicy1.setHeightForWidth(self.delSelectedMods.sizePolicy().hasHeightForWidth())
        self.delSelectedMods.setSizePolicy(sizePolicy1)
        self.delSelectedMods.setCursor(QCursor(Qt.PointingHandCursor))
        self.delSelectedMods.setIcon(icon7)
        self.delSelectedMods.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.delSelectedMods)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.PStackedWidget.addWidget(self.PPWgt)
        self.PPQrc = QWidget()
        self.PPQrc.setObjectName(u"PPQrc")
        self.verticalLayout_8 = QVBoxLayout(self.PPQrc)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.qrcTree = TreeView(self.PPQrc)
        self.qrcTree.setObjectName(u"qrcTree")
        self.qrcTree.setStyleSheet(u"")
        self.qrcTree.setFrameShape(QFrame.NoFrame)
        self.qrcTree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.qrcTree.setTabKeyNavigation(True)
        self.qrcTree.setDragDropMode(QAbstractItemView.DropOnly)
        self.qrcTree.setDefaultDropAction(Qt.CopyAction)
        self.qrcTree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.qrcTree.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.qrcTree.setIconSize(QSize(64, 64))
        self.qrcTree.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.qrcTree.setAnimated(True)
        self.qrcTree.setHeaderHidden(True)
        self.qrcTree.header().setVisible(False)

        self.verticalLayout_8.addWidget(self.qrcTree)

        self.imgSizeSlider = QSlider(self.PPQrc)
        self.imgSizeSlider.setObjectName(u"imgSizeSlider")
        self.imgSizeSlider.setMinimum(16)
        self.imgSizeSlider.setMaximum(256)
        self.imgSizeSlider.setValue(64)
        self.imgSizeSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.imgSizeSlider)

        self.PStackedWidget.addWidget(self.PPQrc)
        self.PPExec = QWidget()
        self.PPExec.setObjectName(u"PPExec")
        self.verticalLayout_10 = QVBoxLayout(self.PPExec)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.PPExec)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.execArgs = QLineEdit(self.PPExec)
        self.execArgs.setObjectName(u"execArgs")

        self.horizontalLayout_5.addWidget(self.execArgs)

        self.pyinstallerHelp = QPushButton(self.PPExec)
        self.pyinstallerHelp.setObjectName(u"pyinstallerHelp")
        sizePolicy.setHeightForWidth(self.pyinstallerHelp.sizePolicy().hasHeightForWidth())
        self.pyinstallerHelp.setSizePolicy(sizePolicy)
        self.pyinstallerHelp.setMinimumSize(QSize(25, 0))
        self.pyinstallerHelp.setCursor(QCursor(Qt.PointingHandCursor))
        self.pyinstallerHelp.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pyinstallerHelp)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.execOutput = QTextEdit(self.PPExec)
        self.execOutput.setObjectName(u"execOutput")
        self.execOutput.setStyleSheet(u"")
        self.execOutput.setFrameShape(QFrame.NoFrame)
        self.execOutput.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.execOutput)

        self.createExecBtn = JumpButton(self.PPExec)
        self.createExecBtn.setObjectName(u"createExecBtn")
        self.createExecBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.createExecBtn.setIcon(icon5)
        self.createExecBtn.setIconSize(QSize(16, 16))

        self.verticalLayout_10.addWidget(self.createExecBtn)

        self.PStackedWidget.addWidget(self.PPExec)

        self.horizontalLayout_6.addWidget(self.PStackedWidget)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.mainPage.addWidget(self.projectPg)
        self.settPg = QWidget()
        self.settPg.setObjectName(u"settPg")
        self.verticalLayout_11 = QVBoxLayout(self.settPg)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.settPg)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setProperty("isTitle", True)

        self.verticalLayout_11.addWidget(self.label_6)

        self.scrollArea = QScrollArea(self.settPg)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 575, 422))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setVerticalSpacing(17)
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.QtDesignerPathInput = QLineEdit(self.scrollAreaWidgetContents)
        self.QtDesignerPathInput.setObjectName(u"QtDesignerPathInput")

        self.horizontalLayout_7.addWidget(self.QtDesignerPathInput)

        self.QtDesignerPathBtn = QPushButton(self.scrollAreaWidgetContents)
        self.QtDesignerPathBtn.setObjectName(u"QtDesignerPathBtn")
        self.QtDesignerPathBtn.setMinimumSize(QSize(24, 0))
        self.QtDesignerPathBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.QtDesignerPathBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.QtDesignerPathBtn)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.designerPathsList = PathsList(self.scrollAreaWidgetContents)
        self.designerPathsList.setObjectName(u"designerPathsList")
        self.designerPathsList.setStyleSheet(u"border:1px solid rgb(200, 121, 65);\n"
"")
        self.designerPathsList.setFrameShape(QFrame.NoFrame)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.designerPathsList)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.sublimePathInput = QLineEdit(self.scrollAreaWidgetContents)
        self.sublimePathInput.setObjectName(u"sublimePathInput")

        self.horizontalLayout_10.addWidget(self.sublimePathInput)

        self.sublimePathBtn = QPushButton(self.scrollAreaWidgetContents)
        self.sublimePathBtn.setObjectName(u"sublimePathBtn")
        self.sublimePathBtn.setMinimumSize(QSize(24, 0))
        self.sublimePathBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sublimePathBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_10.addWidget(self.sublimePathBtn)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_10)

        self.icoSizeCb = QComboBox(self.scrollAreaWidgetContents)
        self.icoSizeCb.addItem("")
        self.icoSizeCb.addItem("")
        self.icoSizeCb.addItem("")
        self.icoSizeCb.addItem("")
        self.icoSizeCb.addItem("")
        self.icoSizeCb.addItem("")
        self.icoSizeCb.addItem("")
        self.icoSizeCb.setObjectName(u"icoSizeCb")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.icoSizeCb)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)


        self.verticalLayout_9.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.createMQEXEC = QPushButton(self.scrollAreaWidgetContents)
        self.createMQEXEC.setObjectName(u"createMQEXEC")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.createMQEXEC.sizePolicy().hasHeightForWidth())
        self.createMQEXEC.setSizePolicy(sizePolicy4)
        icon16 = QIcon()
        icon16.addFile(u":/icons/img/cil-external-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.createMQEXEC.setIcon(icon16)

        self.verticalLayout_9.addWidget(self.createMQEXEC)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.saveSett = JumpButton(self.settPg)
        self.saveSett.setObjectName(u"saveSett")
        self.saveSett.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveSett.setIcon(icon5)

        self.horizontalLayout_19.addWidget(self.saveSett)

        self.SettDoneBtn = JumpButton(self.settPg)
        self.SettDoneBtn.setObjectName(u"SettDoneBtn")
        self.SettDoneBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.SettDoneBtn.setIcon(icon8)

        self.horizontalLayout_19.addWidget(self.SettDoneBtn)


        self.verticalLayout_11.addLayout(self.horizontalLayout_19)

        self.mainPage.addWidget(self.settPg)
        self.newModulePg = QWidget()
        self.newModulePg.setObjectName(u"newModulePg")
        self.verticalLayout_13 = QVBoxLayout(self.newModulePg)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_20 = QLabel(self.newModulePg)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setProperty("isTitle", True)

        self.verticalLayout_13.addWidget(self.label_20)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_3.setVerticalSpacing(17)
        self.label_24 = QLabel(self.newModulePg)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_24)

        self.cwQtClass = QComboBox(self.newModulePg)
        self.cwQtClass.setObjectName(u"cwQtClass")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.cwQtClass)

        self.label_19 = QLabel(self.newModulePg)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.cwClass = QLineEdit(self.newModulePg)
        self.cwClass.setObjectName(u"cwClass")
        self.cwClass.setFrame(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.cwClass)

        self.cwMod = QLineEdit(self.newModulePg)
        self.cwMod.setObjectName(u"cwMod")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.cwMod)

        self.cwModLbl = QLabel(self.newModulePg)
        self.cwModLbl.setObjectName(u"cwModLbl")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.cwModLbl)


        self.verticalLayout_13.addLayout(self.formLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 252, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.createWidget = JumpButton(self.newModulePg)
        self.createWidget.setObjectName(u"createWidget")
        self.createWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.createWidget.setIcon(icon5)

        self.horizontalLayout_15.addWidget(self.createWidget)

        self.cancelCreateW = JumpButton(self.newModulePg)
        self.cancelCreateW.setObjectName(u"cancelCreateW")
        self.cancelCreateW.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelCreateW.setIcon(icon8)

        self.horizontalLayout_15.addWidget(self.cancelCreateW)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.mainPage.addWidget(self.newModulePg)
        self.newUiPg = QWidget()
        self.newUiPg.setObjectName(u"newUiPg")
        self.verticalLayout_17 = QVBoxLayout(self.newUiPg)
        self.verticalLayout_17.setSpacing(20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_30 = QLabel(self.newUiPg)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"")
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_30.setProperty("isTitle", True)

        self.verticalLayout_17.addWidget(self.label_30)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_18 = QLabel(self.newUiPg)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.newUiType = QComboBox(self.newUiPg)
        self.newUiType.addItem("")
        self.newUiType.addItem("")
        self.newUiType.setObjectName(u"newUiType")
        self.newUiType.setCursor(QCursor(Qt.PointingHandCursor))
        self.newUiType.setFocusPolicy(Qt.NoFocus)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.newUiType)

        self.label_28 = QLabel(self.newUiPg)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_28)

        self.newUiInput = QLineEdit(self.newUiPg)
        self.newUiInput.setObjectName(u"newUiInput")
        self.newUiInput.setStyleSheet(u"")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.newUiInput)


        self.verticalLayout_17.addLayout(self.formLayout_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.createNewUi = JumpButton(self.newUiPg)
        self.createNewUi.setObjectName(u"createNewUi")
        self.createNewUi.setCursor(QCursor(Qt.PointingHandCursor))
        self.createNewUi.setIcon(icon5)

        self.horizontalLayout_18.addWidget(self.createNewUi)

        self.cancelCreateUi = JumpButton(self.newUiPg)
        self.cancelCreateUi.setObjectName(u"cancelCreateUi")
        self.cancelCreateUi.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelCreateUi.setIcon(icon8)

        self.horizontalLayout_18.addWidget(self.cancelCreateUi)


        self.verticalLayout_17.addLayout(self.horizontalLayout_18)

        self.mainPage.addWidget(self.newUiPg)

        self.verticalLayout.addWidget(self.mainPage)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"font-size:12pt;")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.closeBtn.clicked.connect(MainWindow.close)
        self.minimizeBtn.clicked.connect(MainWindow.showMinimized)

        self.mainPage.setCurrentIndex(0)
        self.PStackedWidget.setCurrentIndex(2)
        self.icoSizeCb.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MadQt Project Manager", None))
        self.actionPotatoes.setText(QCoreApplication.translate("MainWindow", u"Potatoes", None))
#if QT_CONFIG(statustip)
        self.header.setStatusTip(QCoreApplication.translate("MainWindow", u"Double click for full screen", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.mainTitle.setStatusTip(QCoreApplication.translate("MainWindow", u"Start page", None))
#endif // QT_CONFIG(statustip)
        self.mainTitle.setText(QCoreApplication.translate("MainWindow", u"MadQt", None))
        self.secTitle.setText(QCoreApplication.translate("MainWindow", u"  Project Manager", None))
#if QT_CONFIG(tooltip)
        self.startPageBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Start", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.startPageBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Start Page", None))
#endif // QT_CONFIG(statustip)
        self.startPageBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.settBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.settBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(statustip)
        self.settBtn.setText("")
#if QT_CONFIG(tooltip)
        self.PpageBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Project", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.PpageBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Project page", None))
#endif // QT_CONFIG(statustip)
        self.PpageBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.sublimePBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Open Sublime Project", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.sublimePBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Open sublime text project", None))
#endif // QT_CONFIG(statustip)
        self.sublimePBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.logo.setStatusTip(QCoreApplication.translate("MainWindow", u"Documentation", None))
#endif // QT_CONFIG(statustip)
        self.logo.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.closeBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(statustip)
        self.closeBtn.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.minimizeBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(statustip)
        self.minimizeBtn.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(statustip)
        self.newP.setStatusTip(QCoreApplication.translate("MainWindow", u"Create a new project", None))
#endif // QT_CONFIG(statustip)
        self.newP.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
#if QT_CONFIG(shortcut)
        self.newP.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.addP.setStatusTip(QCoreApplication.translate("MainWindow", u"Open existing project not in list", None))
#endif // QT_CONFIG(statustip)
        self.addP.setText("")
#if QT_CONFIG(statustip)
        self.delSelectedP.setStatusTip(QCoreApplication.translate("MainWindow", u"Remove selected from list -> Does not delete files in disk", None))
#endif // QT_CONFIG(statustip)
        self.delSelectedP.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.projectNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New MadQt project", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Folder", None))
        self.NewPFolderName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\...", None))
#if QT_CONFIG(statustip)
        self.newPFolder.setStatusTip(QCoreApplication.translate("MainWindow", u"Select folder", None))
#endif // QT_CONFIG(statustip)
        self.newPFolder.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.newPIcon.setText("")
#if QT_CONFIG(statustip)
        self.newPIconBrowse.setStatusTip(QCoreApplication.translate("MainWindow", u"Select image file -> will be converted to .ico", None))
#endif // QT_CONFIG(statustip)
        self.newPIconBrowse.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.createP.setText(QCoreApplication.translate("MainWindow", u"Create Project", None))
        self.cancelCreateP.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
#if QT_CONFIG(statustip)
        self.PrjName.setStatusTip(QCoreApplication.translate("MainWindow", u"Your project name", None))
#endif // QT_CONFIG(statustip)
        self.PrjName.setText(QCoreApplication.translate("MainWindow", u"Project Name", None))
#if QT_CONFIG(tooltip)
        self.qrcPBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Images", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.qrcPBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Project images", None))
#endif // QT_CONFIG(statustip)
        self.qrcPBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.uiFilesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Ui Files", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.uiFilesBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"User interface files", None))
#endif // QT_CONFIG(statustip)
        self.uiFilesBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.custWidgetsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Widgets", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.custWidgetsBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Custom widgets", None))
#endif // QT_CONFIG(statustip)
        self.custWidgetsBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.execPBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Executable", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.execPBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Create executable", None))
#endif // QT_CONFIG(statustip)
        self.execPBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.refreshBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.refreshBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Refresh file structure", None))
#endif // QT_CONFIG(statustip)
        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.runBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Run ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.runBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Launch with python", None))
#endif // QT_CONFIG(statustip)
        self.runBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.openPFolder.setToolTip(QCoreApplication.translate("MainWindow", u"Open Folder", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.openPFolder.setStatusTip(QCoreApplication.translate("MainWindow", u"Open project folder", None))
#endif // QT_CONFIG(statustip)
        self.openPFolder.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.saveAsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Save As", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.saveAsBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Save project to new folder", None))
#endif // QT_CONFIG(statustip)
        self.saveAsBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.newUiBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Create new .ui widget or window", None))
#endif // QT_CONFIG(statustip)
        self.newUiBtn.setText(QCoreApplication.translate("MainWindow", u"New Ui", None))
#if QT_CONFIG(shortcut)
        self.newUiBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.addUiBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Add .ui files -> Drag & Drop also available", None))
#endif // QT_CONFIG(statustip)
        self.addUiBtn.setText(QCoreApplication.translate("MainWindow", u"Add Ui", None))
#if QT_CONFIG(shortcut)
        self.addUiBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.delSelectedUiBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete selected", None))
#endif // QT_CONFIG(statustip)
        self.delSelectedUiBtn.setText("")
        ___qtreewidgetitem = self.moduleTree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"2", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"1", None));
#if QT_CONFIG(statustip)
        self.newModuleBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Create new Custom Widget based on a template", None))
#endif // QT_CONFIG(statustip)
        self.newModuleBtn.setText(QCoreApplication.translate("MainWindow", u"New Module", None))
#if QT_CONFIG(shortcut)
        self.newModuleBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.addModuleBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Add module -> Drag & Drop also available", None))
#endif // QT_CONFIG(statustip)
        self.addModuleBtn.setText(QCoreApplication.translate("MainWindow", u"Add Module", None))
#if QT_CONFIG(shortcut)
        self.addModuleBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.delSelectedMods.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete selected", None))
#endif // QT_CONFIG(statustip)
        self.delSelectedMods.setText("")
        ___qtreewidgetitem1 = self.qrcTree.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"1", None));
#if QT_CONFIG(statustip)
        self.imgSizeSlider.setStatusTip(QCoreApplication.translate("MainWindow", u"Icon size", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Arguments:", None))
        self.execArgs.setText(QCoreApplication.translate("MainWindow", u"--onefile --windowed", None))
#if QT_CONFIG(statustip)
        self.pyinstallerHelp.setStatusTip(QCoreApplication.translate("MainWindow", u"View pyinstaller help", None))
#endif // QT_CONFIG(statustip)
        self.pyinstallerHelp.setText(QCoreApplication.translate("MainWindow", u"?", None))
#if QT_CONFIG(statustip)
        self.createExecBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Create executable", None))
#endif // QT_CONFIG(statustip)
        self.createExecBtn.setText(QCoreApplication.translate("MainWindow", u"Create Executable", None))
#if QT_CONFIG(shortcut)
        self.createExecBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Qt Designer location", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"QtDesigner Path", None))
#if QT_CONFIG(statustip)
        self.QtDesignerPathInput.setStatusTip(QCoreApplication.translate("MainWindow", u"Qt Designer location", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.QtDesignerPathBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Select file", None))
#endif // QT_CONFIG(statustip)
        self.QtDesignerPathBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.label_5.setStatusTip(QCoreApplication.translate("MainWindow", u"Paths to QtDesigner Plugins", None))
#endif // QT_CONFIG(statustip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Plugin Paths", None))
#if QT_CONFIG(statustip)
        self.designerPathsList.setStatusTip(QCoreApplication.translate("MainWindow", u"Right click to add/remove paths", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.label_10.setStatusTip(QCoreApplication.translate("MainWindow", u"Sublime text location", None))
#endif // QT_CONFIG(statustip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sublime Text Path", None))
#if QT_CONFIG(statustip)
        self.sublimePathInput.setStatusTip(QCoreApplication.translate("MainWindow", u"Sublime text location", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.sublimePathBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Select file", None))
#endif // QT_CONFIG(statustip)
        self.sublimePathBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.icoSizeCb.setItemText(0, QCoreApplication.translate("MainWindow", u"16", None))
        self.icoSizeCb.setItemText(1, QCoreApplication.translate("MainWindow", u"24", None))
        self.icoSizeCb.setItemText(2, QCoreApplication.translate("MainWindow", u"32", None))
        self.icoSizeCb.setItemText(3, QCoreApplication.translate("MainWindow", u"48", None))
        self.icoSizeCb.setItemText(4, QCoreApplication.translate("MainWindow", u"64", None))
        self.icoSizeCb.setItemText(5, QCoreApplication.translate("MainWindow", u"128", None))
        self.icoSizeCb.setItemText(6, QCoreApplication.translate("MainWindow", u"256", None))

        self.icoSizeCb.setCurrentText(QCoreApplication.translate("MainWindow", u"64", None))
#if QT_CONFIG(statustip)
        self.label_8.setStatusTip(QCoreApplication.translate("MainWindow", u"When converting images to .ico this is their new size", None))
#endif // QT_CONFIG(statustip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Default ICO Size", None))
#if QT_CONFIG(statustip)
        self.createMQEXEC.setStatusTip(QCoreApplication.translate("MainWindow", u"Opens web page with instruction on creating a shortcut", None))
#endif // QT_CONFIG(statustip)
        self.createMQEXEC.setText(QCoreApplication.translate("MainWindow", u"Create Shortcut", None))
        self.saveSett.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.SettDoneBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"New Custom Widget", None))
#if QT_CONFIG(statustip)
        self.label_24.setStatusTip(QCoreApplication.translate("MainWindow", u"The Qt class your widgets inherits from", None))
#endif // QT_CONFIG(statustip)
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Qt Base Class", None))
#if QT_CONFIG(statustip)
        self.label_19.setStatusTip(QCoreApplication.translate("MainWindow", u"Your custom widget class name", None))
#endif // QT_CONFIG(statustip)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Custom Class", None))
#if QT_CONFIG(statustip)
        self.cwClass.setStatusTip(QCoreApplication.translate("MainWindow", u"Your custom widget class name", None))
#endif // QT_CONFIG(statustip)
        self.cwClass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Button", None))
        self.cwMod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"button", None))
        self.cwModLbl.setText(QCoreApplication.translate("MainWindow", u"Module", None))
        self.createWidget.setText(QCoreApplication.translate("MainWindow", u"Create Widget", None))
        self.cancelCreateW.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"New Ui", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.newUiType.setItemText(0, QCoreApplication.translate("MainWindow", u"QMainWindow", None))
        self.newUiType.setItemText(1, QCoreApplication.translate("MainWindow", u"QWidget", None))

#if QT_CONFIG(statustip)
        self.label_28.setStatusTip(QCoreApplication.translate("MainWindow", u"The Qt class your widgets inherits from", None))
#endif // QT_CONFIG(statustip)
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Name", None))
#if QT_CONFIG(statustip)
        self.newUiInput.setStatusTip(QCoreApplication.translate("MainWindow", u"The name of the new Ui", None))
#endif // QT_CONFIG(statustip)
        self.newUiInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.createNewUi.setText(QCoreApplication.translate("MainWindow", u"Create Ui", None))
        self.cancelCreateUi.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

