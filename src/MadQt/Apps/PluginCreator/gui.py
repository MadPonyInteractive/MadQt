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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QListWidgetItem,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)

from myWidgets import (JumpButton, PathsList)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(593, 662)
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
"QLineEdit:disabled{\n"
"	background-color: rgb(219, 203, 189);\n"
"	color: rgb(41, 0, 1);\n"
"}\n"
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
"    margin: 0px 21px 0 21"
                        "px;\n"
"	border-radius: 0px;\n"
"}\n"
"QAbstractSlider::handle:horizontal {\n"
"    min-width: 25px;\n"
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
""
                        "	border: none;	\n"
"    width: 12px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
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
" QAbstractSlider::add-page:vertical, QAbstractSlider::sub-page:vertical {"
                        "\n"
"     background: none;\n"
" }\n"
"QSlider::handle::horizontal{\n"
"width:25px;\n"
"}\n"
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
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
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

        self.horizontalSpacer_7 = QSpacerItem(337, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.logo = QLabel(self.header)
        self.logo.setObjectName(u"logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy1)
        self.closeBtn.setMaximumSize(QSize(16777215, 24))
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeBtn.setIconSize(QSize(8, 8))

        self.verticalLayout_2.addWidget(self.closeBtn)

        self.verticalSpacer_6 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.minimizeBtn = QToolButton(self.header)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        sizePolicy1.setHeightForWidth(self.minimizeBtn.sizePolicy().hasHeightForWidth())
        self.minimizeBtn.setSizePolicy(sizePolicy1)
        self.minimizeBtn.setMaximumSize(QSize(16777215, 24))
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeBtn.setIconSize(QSize(8, 8))

        self.verticalLayout_2.addWidget(self.minimizeBtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.header)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 575, 517))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.pluginName = QLineEdit(self.scrollAreaWidgetContents)
        self.pluginName.setObjectName(u"pluginName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pluginName)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.QtClass = QLineEdit(self.scrollAreaWidgetContents)
        self.QtClass.setObjectName(u"QtClass")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.QtClass)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.geoW = QSpinBox(self.scrollAreaWidgetContents)
        self.geoW.setObjectName(u"geoW")
        self.geoW.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.geoW.setMaximum(8000)
        self.geoW.setValue(100)

        self.horizontalLayout.addWidget(self.geoW)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout.addWidget(self.label_10)

        self.geoH = QSpinBox(self.scrollAreaWidgetContents)
        self.geoH.setObjectName(u"geoH")
        self.geoH.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.geoH.setMaximum(8000)
        self.geoH.setValue(100)

        self.horizontalLayout.addWidget(self.geoH)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.propList = PathsList(self.scrollAreaWidgetContents)
        self.propList.setObjectName(u"propList")
        self.propList.setStyleSheet(u"border:1px solid rgb(200, 121, 65);\n"
"")
        self.propList.setFrameShape(QFrame.NoFrame)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.propList)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.tooltipIn = QLineEdit(self.scrollAreaWidgetContents)
        self.tooltipIn.setObjectName(u"tooltipIn")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.tooltipIn)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(8)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.newPIcon = QLabel(self.scrollAreaWidgetContents)
        self.newPIcon.setObjectName(u"newPIcon")
        self.newPIcon.setPixmap(QPixmap(u":/images/img/mpi_logo_icon.ico"))
        self.newPIcon.setScaledContents(False)

        self.horizontalLayout_20.addWidget(self.newPIcon)

        self.newPIconBrowse = QPushButton(self.scrollAreaWidgetContents)
        self.newPIconBrowse.setObjectName(u"newPIconBrowse")
        self.newPIconBrowse.setMinimumSize(QSize(24, 0))
        self.newPIconBrowse.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_20.addWidget(self.newPIconBrowse)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_20)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.widgetGroup = QLineEdit(self.scrollAreaWidgetContents)
        self.widgetGroup.setObjectName(u"widgetGroup")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.widgetGroup)

        self.isContainerCb = QCheckBox(self.scrollAreaWidgetContents)
        self.isContainerCb.setObjectName(u"isContainerCb")
        self.isContainerCb.setIconSize(QSize(32, 32))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.isContainerCb)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(8)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.regPath = QLineEdit(self.scrollAreaWidgetContents)
        self.regPath.setObjectName(u"regPath")

        self.horizontalLayout_21.addWidget(self.regPath)

        self.regOpen = QPushButton(self.scrollAreaWidgetContents)
        self.regOpen.setObjectName(u"regOpen")
        self.regOpen.setMinimumSize(QSize(24, 0))
        self.regOpen.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_21.addWidget(self.regOpen)

        self.addToExistingCb = QCheckBox(self.scrollAreaWidgetContents)
        self.addToExistingCb.setObjectName(u"addToExistingCb")
        self.addToExistingCb.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.addToExistingCb)


        self.formLayout.setLayout(10, QFormLayout.FieldRole, self.horizontalLayout_21)

        self.addMenuCb = QCheckBox(self.scrollAreaWidgetContents)
        self.addMenuCb.setObjectName(u"addMenuCb")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.addMenuCb)

        self.isMultiCb = QCheckBox(self.scrollAreaWidgetContents)
        self.isMultiCb.setObjectName(u"isMultiCb")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.isMultiCb)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.createPluginBtn = JumpButton(self.centralwidget)
        self.createPluginBtn.setObjectName(u"createPluginBtn")
        self.createPluginBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.createPluginBtn.setIcon(icon1)
        self.createPluginBtn.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.createPluginBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"font-size:12pt;")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.closeBtn.clicked.connect(MainWindow.close)
        self.minimizeBtn.clicked.connect(MainWindow.showMinimized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MadQt Plugin Creator", None))
        self.actionPotatoes.setText(QCoreApplication.translate("MainWindow", u"Potatoes", None))
#if QT_CONFIG(statustip)
        self.header.setStatusTip(QCoreApplication.translate("MainWindow", u"Double click for full screen", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.mainTitle.setStatusTip(QCoreApplication.translate("MainWindow", u"Start page", None))
#endif // QT_CONFIG(statustip)
        self.mainTitle.setText(QCoreApplication.translate("MainWindow", u"MadQt", None))
        self.secTitle.setText(QCoreApplication.translate("MainWindow", u"    Plugin Creator", None))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Class Name", None))
#if QT_CONFIG(statustip)
        self.pluginName.setStatusTip(QCoreApplication.translate("MainWindow", u"Your plugin name", None))
#endif // QT_CONFIG(statustip)
        self.pluginName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MyAwesomePlugin", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Qt Class", None))
#if QT_CONFIG(statustip)
        self.QtClass.setStatusTip(QCoreApplication.translate("MainWindow", u"Qt Class your plugin inherits from", None))
#endif // QT_CONFIG(statustip)
        self.QtClass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"QWidget", None))
#if QT_CONFIG(statustip)
        self.label_9.setStatusTip(QCoreApplication.translate("MainWindow", u"Paths to QtDesigner Plugins", None))
#endif // QT_CONFIG(statustip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Size Hint", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Width", None))
#if QT_CONFIG(statustip)
        self.geoW.setStatusTip(QCoreApplication.translate("MainWindow", u"Width", None))
#endif // QT_CONFIG(statustip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Height", None))
#if QT_CONFIG(statustip)
        self.geoH.setStatusTip(QCoreApplication.translate("MainWindow", u"Height", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.label_8.setStatusTip(QCoreApplication.translate("MainWindow", u"Paths to QtDesigner Plugins", None))
#endif // QT_CONFIG(statustip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Properties", None))
#if QT_CONFIG(statustip)
        self.propList.setStatusTip(QCoreApplication.translate("MainWindow", u"Right click to add/remove properties", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tooltip", None))
#if QT_CONFIG(statustip)
        self.tooltipIn.setStatusTip(QCoreApplication.translate("MainWindow", u"QtDesigner tooltip", None))
#endif // QT_CONFIG(statustip)
        self.tooltipIn.setText("")
        self.tooltipIn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"My plugin is...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Icon", None))
        self.newPIcon.setText("")
#if QT_CONFIG(statustip)
        self.newPIconBrowse.setStatusTip(QCoreApplication.translate("MainWindow", u"Select image file -> will be converted to .ico", None))
#endif // QT_CONFIG(statustip)
        self.newPIconBrowse.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Group", None))
#if QT_CONFIG(statustip)
        self.widgetGroup.setStatusTip(QCoreApplication.translate("MainWindow", u"Group name in QtDesigner Widget box", None))
#endif // QT_CONFIG(statustip)
        self.widgetGroup.setText("")
        self.widgetGroup.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom Widgets", None))
#if QT_CONFIG(statustip)
        self.isContainerCb.setStatusTip(QCoreApplication.translate("MainWindow", u"Will it contain other widgets?", None))
#endif // QT_CONFIG(statustip)
        self.isContainerCb.setText(QCoreApplication.translate("MainWindow", u"Is Container", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Registry", None))
#if QT_CONFIG(statustip)
        self.regPath.setStatusTip(QCoreApplication.translate("MainWindow", u"Files path", None))
#endif // QT_CONFIG(statustip)
        self.regPath.setText("")
        self.regPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\path\\to\\plugin\\registration", None))
#if QT_CONFIG(statustip)
        self.regOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Open path/file", None))
#endif // QT_CONFIG(statustip)
        self.regOpen.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(statustip)
        self.addToExistingCb.setStatusTip(QCoreApplication.translate("MainWindow", u"Add to an existing register ", None))
#endif // QT_CONFIG(statustip)
        self.addToExistingCb.setText(QCoreApplication.translate("MainWindow", u"Add to Existing", None))
        self.addMenuCb.setText(QCoreApplication.translate("MainWindow", u"Add Menu", None))
        self.isMultiCb.setText(QCoreApplication.translate("MainWindow", u"Is Multi Page", None))
#if QT_CONFIG(statustip)
        self.createPluginBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Create Plugin", None))
#endif // QT_CONFIG(statustip)
        self.createPluginBtn.setText(QCoreApplication.translate("MainWindow", u"Create Plugin", None))
#if QT_CONFIG(shortcut)
        self.createPluginBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

