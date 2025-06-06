# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SaadStudio_Torg_alpha_1NJSmVv.ui'
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
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QTextEdit,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 636)
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
        self.scrollArea = QScrollArea(self.tab1)
        self.scrollArea.setObjectName(u"scrollArea")
        font = QFont()
        font.setHintingPreference(QFont.PreferFullHinting)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 754, 343))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.edit_task = QPushButton(self.groupBox)
        self.edit_task.setObjectName(u"edit_task")
        self.edit_task.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_5.addWidget(self.edit_task, 2, 0, 1, 1)

        self.set_work_task = QPushButton(self.groupBox)
        self.set_work_task.setObjectName(u"set_work_task")
        self.set_work_task.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_5.addWidget(self.set_work_task, 1, 0, 1, 1)

        self.nw_task = QPushButton(self.groupBox)
        self.nw_task.setObjectName(u"nw_task")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(12)
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.nw_task.setFont(font1)
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

        self.gridLayout_5.addWidget(self.nw_task, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_13 = QGridLayout(self.tab_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_2, 7, 0, 1, 1)

        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(10, 0))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(97, 100, 132);\n"
"	padding:10px;\n"
"	font: 18pt \"Poppins\";\n"
"	padding-left:50px;\n"
"	padding-right:50px;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(196, 186, 216);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.startpomo = QPushButton(self.frame)
        self.startpomo.setObjectName(u"startpomo")
        sizePolicy.setHeightForWidth(self.startpomo.sizePolicy().hasHeightForWidth())
        self.startpomo.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(28)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.startpomo.setFont(font3)
        self.startpomo.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(97, 100, 132);\n"
"	padding:10px;\n"
"	font: 28pt \"Poppins\";\n"
"	padding-left:50px;\n"
"	padding-right:50px;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(196, 186, 216);\n"
"\n"
"}\n"
"QPushButton::checked{\n"
"	background-color: rgb(40, 51, 112);\n"
"}")
        self.startpomo.setCheckable(True)

        self.horizontalLayout.addWidget(self.startpomo)

        self.settingpomo = QPushButton(self.frame)
        self.settingpomo.setObjectName(u"settingpomo")
        sizePolicy.setHeightForWidth(self.settingpomo.sizePolicy().hasHeightForWidth())
        self.settingpomo.setSizePolicy(sizePolicy)
        self.settingpomo.setMinimumSize(QSize(189, 54))
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setPointSize(18)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferAntialias)
        self.settingpomo.setFont(font4)
        self.settingpomo.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(97, 100, 132);\n"
"	padding:10px;\n"
"	font: 18pt \"Poppins\";\n"
"	padding-left:50px;\n"
"	padding-right:50px;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(196, 186, 216);\n"
"\n"
"}")
        self.settingpomo.setIconSize(QSize(32, 32))
        self.settingpomo.setCheckable(False)

        self.horizontalLayout.addWidget(self.settingpomo)


        self.gridLayout_7.addWidget(self.frame, 2, 0, 1, 1)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(700, 200))
        font5 = QFont()
        font5.setFamilies([u"Poppins"])
        font5.setPointSize(72)
        font5.setWeight(QFont.Light)
        font5.setItalic(False)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font5)
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
        font6 = QFont()
        font6.setFamilies([u"Poppins"])
        font6.setPointSize(16)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.worktask_pomo.setFont(font6)
        self.worktask_pomo.setStyleSheet(u"font: 16pt \"Poppins\";")
        self.worktask_pomo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.worktask_pomo, 8, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_11 = QGridLayout(self.tab_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.treeWidget = QTreeWidget(self.tab_3)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout_10.addWidget(self.treeWidget, 0, 1, 1, 1)

        self.tasklist = QListWidget(self.tab_3)
        self.tasklist.setObjectName(u"tasklist")

        self.gridLayout_10.addWidget(self.tasklist, 0, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
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
        self.youtube = QPushButton(self.tab_4)
        self.youtube.setObjectName(u"youtube")
        self.youtube.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_14.addWidget(self.youtube, 2, 0, 1, 1)

        self.tabnw = QPushButton(self.tab_4)
        self.tabnw.setObjectName(u"tabnw")
        self.tabnw.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_14.addWidget(self.tabnw, 0, 0, 1, 1)

        self.gemini = QPushButton(self.tab_4)
        self.gemini.setObjectName(u"gemini")
        self.gemini.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_14.addWidget(self.gemini, 3, 0, 1, 1)

        self.ggoogle = QPushButton(self.tab_4)
        self.ggoogle.setObjectName(u"ggoogle")
        self.ggoogle.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_14.addWidget(self.ggoogle, 1, 0, 1, 1)

        self.settings = QPushButton(self.tab_4)
        self.settings.setObjectName(u"settings")
        self.settings.setStyleSheet(u"QPushButton{\n"
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
        self.settings.setCheckable(True)

        self.gridLayout_14.addWidget(self.settings, 4, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_17 = QGridLayout(self.tab_5)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.tasklist_2 = QListWidget(self.tab_5)
        self.tasklist_2.setObjectName(u"tasklist_2")

        self.gridLayout_16.addWidget(self.tasklist_2, 0, 0, 1, 1)

        self.note = QTextEdit(self.tab_5)
        self.note.setObjectName(u"note")

        self.gridLayout_16.addWidget(self.note, 0, 1, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")

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

        self.addtask = QPushButton(self.groupBox_2)
        self.addtask.setObjectName(u"addtask")
        self.addtask.setFont(font1)
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

        self.gridLayout_20.addWidget(self.addtask, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_20.addWidget(self.label_3, 3, 0, 1, 1)

        self.sswebsite = QCommandLinkButton(self.groupBox_2)
        self.sswebsite.setObjectName(u"sswebsite")

        self.gridLayout_20.addWidget(self.sswebsite, 4, 0, 1, 1)


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
        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.edit_task.setText(QCoreApplication.translate("MainWindow", u"Edit Task", None))
        self.set_work_task.setText(QCoreApplication.translate("MainWindow", u"Set Working Task", None))
        self.nw_task.setText(QCoreApplication.translate("MainWindow", u"New Task", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Task Managment", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"#0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.startpomo.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.settingpomo.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.worktask_pomo.setText(QCoreApplication.translate("MainWindow", u"Current Working Task : Unknow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Pomodoro Timer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Task Orginazer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.youtube.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.tabnw.setText(QCoreApplication.translate("MainWindow", u"+ Tab", None))
        self.gemini.setText(QCoreApplication.translate("MainWindow", u"ChatGPT", None))
        self.ggoogle.setText(QCoreApplication.translate("MainWindow", u"Google", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"New", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Note", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"New Task", None))
        self.taskname_add.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.addtask.setText(QCoreApplication.translate("MainWindow", u"add New Task", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Simplicity is our goal if you want many features Create your app Now by Visiting Our Website", None))
        self.sswebsite.setText(QCoreApplication.translate("MainWindow", u"Saad Studios Website", None))
    # retranslateUi

