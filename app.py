# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SaadStudio_Torg_alpha_1nvHfeY.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTabWidget, QTextBrowser, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 794)
        MainWindow.setMinimumSize(QSize(1100, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.gridLayout_4 = QGridLayout(self.tab1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.nw_task = QPushButton(self.tab1)
        self.nw_task.setObjectName(u"nw_task")
        self.nw_task.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(83, 54, 252);\n"
"	padding:10px;\n"
"	font: 600 12pt \"Poppins\";\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(82, 106, 226);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.nw_task, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 2, 1)

        self.scrollArea = QScrollArea(self.tab1)
        self.scrollArea.setObjectName(u"scrollArea")
        font = QFont()
        font.setHintingPreference(QFont.PreferFullHinting)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1038, 621))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.watermark = QLabel(self.tab1)
        self.watermark.setObjectName(u"watermark")
        self.watermark.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.watermark, 4, 0, 1, 1)

        self.frame = QFrame(self.tab1)
        self.frame.setObjectName(u"frame")
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(7, -1, -1, -1)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(10, -1, -1, -1)

        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_13 = QGridLayout(self.tab_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_2, 7, 0, 1, 1)

        self.frame1 = QFrame(self.tab_2)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"")
        self.frame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame1)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(10, 0))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(41, 44, 109);\n"
"	padding:10px;\n"
"	font: 18pt \"Poppins\";\n"
"	border:1px solid rgb(250, 237, 240);\n"
"	padding-left:50px;\n"
"	padding-right:50px;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"		border-color:rgb(240, 84, 84);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.startpomo = QPushButton(self.frame1)
        self.startpomo.setObjectName(u"startpomo")
        sizePolicy.setHeightForWidth(self.startpomo.sizePolicy().hasHeightForWidth())
        self.startpomo.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(28)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.startpomo.setFont(font2)
        self.startpomo.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(41, 44, 109);\n"
"	border:1px solid rgb(250, 237, 240);\n"
"	padding:10px;\n"
"	font: 28pt \"Poppins\";\n"
"	padding-left:50px;\n"
"	padding-right:50px;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	border-color:rgb(240, 84, 84);\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"	background-color: rgb(40, 51, 112);\n"
"}")
        self.startpomo.setCheckable(True)

        self.horizontalLayout.addWidget(self.startpomo)

        self.settingpomo = QPushButton(self.frame1)
        self.settingpomo.setObjectName(u"settingpomo")
        sizePolicy.setHeightForWidth(self.settingpomo.sizePolicy().hasHeightForWidth())
        self.settingpomo.setSizePolicy(sizePolicy)
        self.settingpomo.setMinimumSize(QSize(189, 54))
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.settingpomo.setFont(font3)
        self.settingpomo.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(41, 44, 109);\n"
"	padding:10px;\n"
"	font: 18pt \"Poppins\";\n"
"	border:1px solid rgb(250, 237, 240);\n"
"	padding-left:50px;\n"
"	padding-right:50px;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"		border-color:rgb(240, 84, 84);\n"
"}")
        self.settingpomo.setIconSize(QSize(32, 32))
        self.settingpomo.setCheckable(False)

        self.horizontalLayout.addWidget(self.settingpomo)


        self.gridLayout_7.addWidget(self.frame1, 2, 0, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(700, 200))
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setPointSize(72)
        font4.setWeight(QFont.Light)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"QLabel{\n"
"	border:1px solid rgb(198, 198, 198);\n"
"	border-radius:10px;\n"
"	background-color: rgb(176, 45, 40);\n"
"	font: 300 72pt \"Poppins\";\n"
"\n"
"\n"
"}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.worktask_pomo = QLabel(self.tab_2)
        self.worktask_pomo.setObjectName(u"worktask_pomo")
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setPointSize(16)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.worktask_pomo.setFont(font5)
        self.worktask_pomo.setStyleSheet(u"font: 16pt \"Poppins\";")
        self.worktask_pomo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.worktask_pomo, 8, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_10 = QGridLayout(self.tab_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.note = QTextEdit(self.tab_5)
        self.note.setObjectName(u"note")

        self.gridLayout_10.addWidget(self.note, 0, 3, 1, 1)

        self.tasklist_2 = QListWidget(self.tab_5)
        self.tasklist_2.setObjectName(u"tasklist_2")

        self.gridLayout_10.addWidget(self.tasklist_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_12 = QGridLayout(self.tab)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.webEngineView = QWebEngineView(self.tab)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"https://www.youtube.com/"))

        self.gridLayout_12.addWidget(self.webEngineView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_15 = QGridLayout(self.tab_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")

        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_19 = QGridLayout(self.page_2)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_21 = QGridLayout(self.groupBox_2)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.taskname_add = QLineEdit(self.groupBox_2)
        self.taskname_add.setObjectName(u"taskname_add")
        self.taskname_add.setStyleSheet(u"font: 16pt \"Poppins\";\n"
"padding:20px;")

        self.gridLayout_20.addWidget(self.taskname_add, 0, 0, 1, 1)

        self.sswebsite = QCommandLinkButton(self.groupBox_2)
        self.sswebsite.setObjectName(u"sswebsite")

        self.gridLayout_20.addWidget(self.sswebsite, 5, 0, 1, 1)

        self.checkbuttontext = QLineEdit(self.groupBox_2)
        self.checkbuttontext.setObjectName(u"checkbuttontext")

        self.gridLayout_20.addWidget(self.checkbuttontext, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_20.addWidget(self.label_3, 4, 0, 1, 1)

        self.addtask = QPushButton(self.groupBox_2)
        self.addtask.setObjectName(u"addtask")
        font6 = QFont()
        font6.setFamilies([u"Poppins"])
        font6.setPointSize(12)
        font6.setWeight(QFont.DemiBold)
        font6.setItalic(False)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.addtask.setFont(font6)
        self.addtask.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(83, 54, 252);\n"
"	padding:10px;\n"
"	font: 600 12pt \"Poppins\";\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(82, 106, 226);\n"
"\n"
"}")

        self.gridLayout_20.addWidget(self.addtask, 3, 0, 1, 1)

        self.task_description = QTextBrowser(self.groupBox_2)
        self.task_description.setObjectName(u"task_description")
        self.task_description.setReadOnly(False)

        self.gridLayout_20.addWidget(self.task_description, 1, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nw_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.watermark.setText(QCoreApplication.translate("MainWindow", u"Saad Studios Corporation Co, LTD / Saad Studios Torg V1.2 Alpha", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Task Managment", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"#0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.startpomo.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.settingpomo.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.worktask_pomo.setText(QCoreApplication.translate("MainWindow", u"Current Working Task : Unknow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Pomodoro Timer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Note", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"New Task", None))
        self.taskname_add.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.sswebsite.setText(QCoreApplication.translate("MainWindow", u"Saad Studios Website", None))
        self.checkbuttontext.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom Check Button text", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Simplicity is our goal if you want many features Create your app Now by Visiting Our Website", None))
        self.addtask.setText(QCoreApplication.translate("MainWindow", u"Add New Task", None))
        self.task_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Decription for your task Mr.", None))
    # retranslateUi

