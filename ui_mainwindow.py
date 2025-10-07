# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableView, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"")
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"/* General Font and Color */\n"
"QWidget{\n"
"	color: #333;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Tooltips */\n"
"QToolTip {\n"
"	color: #333;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* Main Background */\n"
"#bgApp {	\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"    color: #44475a;\n"
"}\n"
"\n"
"/* SIDE BAR */\n"
"#sideBar {\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"#topLogoInfo {\n"
"	border:none;\n"
"	border-bottom: 3px solid #6a7cb1;\n"
"}\n"
"\n"
"#topLogo {\n"
"	background-color: #6272a4;\n"
"	background-image: url(:/resources/images/ef-icon.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"#topName { font: 700 13pt; color: #f8f8f2; }\n"
"#topInfo { font: 8pt"
                        " \"Segoe UI\"; color: #bd93f9; }\n"
"\n"
"#sideBar .QPushButton {	\n"
"	background-position: left center; /* when adding icon to button */\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 5px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 10 px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	padding-right: 20px;\n"
"    color: #f8f8f2;\n"
"	font: 700;\n"
"}\n"
"#sideBar .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#sideBar .QPushButton:checked {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* TOP BAR */\n"
"#page_title_label {	font: 700 14pt}\n"
"\n"
"#startbar_frame{	\n"
"	background-color: #ffffff;\n"
"	border: 1px solid #e1e1e1;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#startbar_frame .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	/*border: none;*/\n"
"    /*color: #333;*/\n"
"}\n"
"\n"
"#workpath_lineedit {\n"
"	border"
                        ": 1px solid #e1e1e1;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* STATUS BAR */\n"
"\n"
"#statusBar{	\n"
"	background-color: #ffffff;\n"
"	border: 1px solid #e1e1e1;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QProgressBar{\n"
"	font: 700;\n"
"	text-align:center;\n"
"}\n"
"\n"
"/* ----------------\n"
"	QPushButton \n"
"-------------------*/\n"
"#mainFrame QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"	padding: 0.1em 0.5em;\n"
"}\n"
"\n"
"#mainFrame QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"\n"
"#mainFrame QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"#mainFrame QPushButton:checked {	\n"
"	border: 2px solid #6272a4;\n"
"}\n"
"\n"
"/* -------------\n"
"	ComboBox \n"
"---------------*/\n"
"QComboBox{\n"
"	background-color: #ffffff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"    color: #333;\n"
"	padding-l"
                        "eft: 4px;\n"
"	padding-right: 4px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 1px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px;\n"
"	border-left-width: 1px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/resources/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"\n"
"QComboBox::drop-down:pressed {\n"
"	background-color: #ff79c6;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: #f8f8f2;	\n"
"	background-color: #7082b6;\n"
"	selection-background-color: #6272a4;\n"
"	padding: 5px 0px;\n"
"	outline: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: #bd93f9;\n"
"	outline: none;\n"
"}\n"
"\n"
"/* -------------\n"
"	SpinBox\n"
"---------"
                        "---- */\n"
"\n"
"QSpinBox {\n"
"	background-color: #ffffff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"    color: #333;\n"
"	padding-left: 1px;\n"
"	padding-right: 50px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	border-left-width: 1px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	background-image: url(:/resources/icons/cil-arrow-top.png);\n"
"	background-position: center;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	border-left-width: 1px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	background-image: url(:/resources/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"	background-color: #bd93f9;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"	background-color: #ff79c6;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"	background-color: #f"
                        "f79c6;\n"
"}\n"
"\n"
"/* -------------\n"
"	LineEdit\n"
"------------- */\n"
"QLineEdit {\n"
"	background-color: #f8f8f2;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #333;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* -------------\n"
"	CheckBox\n"
"------------- */\n"
"QCheckBox::indicator {\n"
"    border: 1px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"    background: #6272a4;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: 1px solid #bd93f9;\n"
"	background-image: url(:/resources/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* -------------\n"
"	RadioButton\n"
"------------- */\n"
"QRadioButton::indicator {\n"
"    border: 1px solid #6272a4;\n"
"	width: 16px;\n"
"	height: 16px;\n"
"	border-radius:8px;\n"
"    background: #6272a4;\n"
"}\n"
""
                        "QRadioButton::indicator:hover {\n"
"    border: 1px solid rgb(119, 136, 187);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 1px solid #bd93f9;\n"
"	background-image: url(:/resources/icons/cil-x-circle.png);\n"
"	border: 1px solid #bd93f9;	\n"
"}\n"
"\n"
"/* -------------\n"
"	TableWidget\n"
"------------- */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #6272a4;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"	background-color: #6272a4;\n"
""
                        "	padding: 3px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"    color: #f8f8f2;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"/* -------------\n"
"	TableView\n"
"------------- */\n"
"QTableView {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableView::item {\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableView::item:selected {\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section {\n"
"	background-color: #6272a4;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableView::horizontalHeader {	\n"
"	background-color: #6272a4;\n"
"}\n"
"\n"
"/* -------------\n"
"	ListWidget\n"
"------------- */\n"
"\n"
"QListWidget {\n"
"	background-color: #f8f8f2;\n"
"	padding: 6px;\n"
"	border: 2px solid #6272a4;\n"
"	outline: none;\n"
"	border-radius"
                        ": 5px;\n"
"	show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	padding-bottom: 0.15em;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background-color:#7082b6;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"	background-color: #bd93f9;\n"
"	border: 2px solid #bd93f9;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"QListWidget::item:selected:!active {\n"
"    /* keep same style when window not focused */\n"
"    background: #bd93f9;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* ---------------\n"
"	QProgressBar\n"
"------------------ */\n"
"\n"
"QProgressBar {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;\n"
"	font: 700 10pt;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #bd93f9;\n"
"	width: 10px;\n"
"}\n"
"\n"
"/* ---------------\n"
"	QTabWidget\n"
"------------------ */\n"
"\n"
"QTabWidget::pane {\n"
"	border: 1px solid #6272a4;\n"
"	border-radius: 5px;\n"
"	border-top-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	min-width: 10ex;\n"
"    padding: 2px 10px"
                        ";\n"
"	border: 1px solid #6272a4;\n"
"	border-bottom: none;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: #6272a4;\n"
"	font-weight:bold;\n"
"	color: #f8f8f2;\n"
"}\n"
"\n"
"/* -------------------------------\n"
"	INDIVIDUAL PAGE DETAILING\n"
"----------------------------------*/\n"
"\n"
"/* HOME PAGE */\n"
"\n"
"#homeLogo {\n"
"	background-image: url(:/resources/images/edfoil.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#label_6 {font: 700 16pt}\n"
"\n"
"#descriptionMsg {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"/* AIRFOIL PAGE */\n"
"\n"
"#label_14 {font: 700 12pt}\n"
"#label_8 {font: 700 12pt}\n"
"\n"
"#frame_17 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"#frame_18 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"/* S"
                        "TATION PAGE */\n"
"\n"
"#label_15 {font: 700 12pt}\n"
"#label_18 {font: 700 12pt}\n"
"\n"
"#frame_2 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"#frame {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"#frame_6 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"#frame_10 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"#frame_8 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"#frame_9 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"/* BLADE PAGE */\n"
"\n"
"#label_37 {font: 700 12pt}\n"
"#label_3 {font: 700 12pt}\n"
"\n"
"#frame_skin_loc {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"#frame_skin_len {\n"
"	background-color: #fff;\n"
"	"
                        "border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"#frame_skin_graphs {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"#frame_ilp_values {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"#frame_ilp_order {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"/* SECTION PAGE */\n"
"#label_29 {font: 700 12pt}\n"
"\n"
"#frame_11 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"#skin_maingraph_frame {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"\n"
"/* EXPORT PAGE */\n"
"#label_42 {font: 700 12pt}\n"
"\n"
"#frame_12 {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #e1e1e1;\n"
"}\n"
"")
        self.appMargins = QGridLayout(self.stylesheet)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setHorizontalSpacing(0)
        self.appMargins.setContentsMargins(4, 4, 4, 4)
        self.bgApp = QFrame(self.stylesheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Plain)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.sideBar = QFrame(self.bgApp)
        self.sideBar.setObjectName(u"sideBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sideBar.sizePolicy().hasHeightForWidth())
        self.sideBar.setSizePolicy(sizePolicy)
        self.sideBar.setMinimumSize(QSize(0, 0))
        self.sideBar.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.sideBar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.sideBar)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(42, 47))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 42))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 0, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.topName = QLabel(self.topLogoInfo)
        self.topName.setObjectName(u"topName")
        self.topName.setGeometry(QRect(50, 3, 81, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.topName.sizePolicy().hasHeightForWidth())
        self.topName.setSizePolicy(sizePolicy1)
        self.topName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.topInfo = QLabel(self.topLogoInfo)
        self.topInfo.setObjectName(u"topInfo")
        self.topInfo.setGeometry(QRect(50, 21, 81, 16))
        self.topInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.topLogoInfo)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.home_page_button = QPushButton(self.sideBar)
        self.home_page_button.setObjectName(u"home_page_button")
        sizePolicy1.setHeightForWidth(self.home_page_button.sizePolicy().hasHeightForWidth())
        self.home_page_button.setSizePolicy(sizePolicy1)
        self.home_page_button.setMinimumSize(QSize(0, 0))
        self.home_page_button.setMaximumSize(QSize(16777215, 16777215))
        self.home_page_button.setStyleSheet(u"")
        self.home_page_button.setCheckable(True)
        self.home_page_button.setChecked(True)
        self.home_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_page_button)

        self.airfoil_page_button = QPushButton(self.sideBar)
        self.airfoil_page_button.setObjectName(u"airfoil_page_button")
        sizePolicy1.setHeightForWidth(self.airfoil_page_button.sizePolicy().hasHeightForWidth())
        self.airfoil_page_button.setSizePolicy(sizePolicy1)
        self.airfoil_page_button.setMinimumSize(QSize(0, 0))
        self.airfoil_page_button.setMaximumSize(QSize(16777215, 16777215))
        self.airfoil_page_button.setStyleSheet(u"")
        self.airfoil_page_button.setCheckable(True)
        self.airfoil_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.airfoil_page_button)

        self.station_page_button = QPushButton(self.sideBar)
        self.station_page_button.setObjectName(u"station_page_button")
        sizePolicy1.setHeightForWidth(self.station_page_button.sizePolicy().hasHeightForWidth())
        self.station_page_button.setSizePolicy(sizePolicy1)
        self.station_page_button.setMinimumSize(QSize(0, 0))
        self.station_page_button.setMaximumSize(QSize(16777215, 16777215))
        self.station_page_button.setStyleSheet(u"")
        self.station_page_button.setCheckable(True)
        self.station_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.station_page_button)

        self.blade_page_button = QPushButton(self.sideBar)
        self.blade_page_button.setObjectName(u"blade_page_button")
        sizePolicy1.setHeightForWidth(self.blade_page_button.sizePolicy().hasHeightForWidth())
        self.blade_page_button.setSizePolicy(sizePolicy1)
        self.blade_page_button.setMinimumSize(QSize(0, 0))
        self.blade_page_button.setMaximumSize(QSize(16777215, 16777215))
        self.blade_page_button.setStyleSheet(u"")
        self.blade_page_button.setCheckable(True)
        self.blade_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.blade_page_button)

        self.skin_page_button = QPushButton(self.sideBar)
        self.skin_page_button.setObjectName(u"skin_page_button")
        sizePolicy1.setHeightForWidth(self.skin_page_button.sizePolicy().hasHeightForWidth())
        self.skin_page_button.setSizePolicy(sizePolicy1)
        self.skin_page_button.setMinimumSize(QSize(0, 0))
        self.skin_page_button.setMaximumSize(QSize(16777215, 16777215))
        self.skin_page_button.setStyleSheet(u"")
        self.skin_page_button.setCheckable(True)
        self.skin_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.skin_page_button)

        self.export_page_button = QPushButton(self.sideBar)
        self.export_page_button.setObjectName(u"export_page_button")
        sizePolicy1.setHeightForWidth(self.export_page_button.sizePolicy().hasHeightForWidth())
        self.export_page_button.setSizePolicy(sizePolicy1)
        self.export_page_button.setMinimumSize(QSize(0, 0))
        self.export_page_button.setMaximumSize(QSize(16777215, 16777215))
        self.export_page_button.setStyleSheet(u"")
        self.export_page_button.setCheckable(True)
        self.export_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.export_page_button)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.settings_button = QPushButton(self.sideBar)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy1.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy1)
        self.settings_button.setMinimumSize(QSize(0, 0))
        self.settings_button.setMaximumSize(QSize(16777215, 16777215))
        self.settings_button.setCheckable(False)
        self.settings_button.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.settings_button)

        self.info_button = QPushButton(self.sideBar)
        self.info_button.setObjectName(u"info_button")
        sizePolicy1.setHeightForWidth(self.info_button.sizePolicy().hasHeightForWidth())
        self.info_button.setSizePolicy(sizePolicy1)
        self.info_button.setMinimumSize(QSize(0, 0))
        self.info_button.setMaximumSize(QSize(16777215, 16777215))
        self.info_button.setCheckable(False)
        self.info_button.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.info_button)

        self.quit_button = QPushButton(self.sideBar)
        self.quit_button.setObjectName(u"quit_button")
        sizePolicy1.setHeightForWidth(self.quit_button.sizePolicy().hasHeightForWidth())
        self.quit_button.setSizePolicy(sizePolicy1)
        self.quit_button.setMinimumSize(QSize(0, 0))
        self.quit_button.setMaximumSize(QSize(16777215, 16777215))
        self.quit_button.setCheckable(False)
        self.quit_button.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.quit_button)


        self.appLayout.addWidget(self.sideBar)

        self.mainFrame = QFrame(self.bgApp)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 6, 6, 6)
        self.startbar_frame = QFrame(self.mainFrame)
        self.startbar_frame.setObjectName(u"startbar_frame")
        self.startbar_frame.setMaximumSize(QSize(16777215, 50))
        self.startbar_frame.setStyleSheet(u"")
        self.startbar_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.startbar_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.startbar_frame.setLineWidth(1)
        self.startbar_frame.setMidLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.startbar_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 9, 9, 9)
        self.page_title_label = QLabel(self.startbar_frame)
        self.page_title_label.setObjectName(u"page_title_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_title_label.sizePolicy().hasHeightForWidth())
        self.page_title_label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.page_title_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.page_title_label)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.startbar_frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.workpath_lineedit = QLineEdit(self.startbar_frame)
        self.workpath_lineedit.setObjectName(u"workpath_lineedit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.workpath_lineedit.sizePolicy().hasHeightForWidth())
        self.workpath_lineedit.setSizePolicy(sizePolicy3)
        self.workpath_lineedit.setStyleSheet(u"")
        self.workpath_lineedit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.workpath_lineedit)

        self.changedir_button = QPushButton(self.startbar_frame)
        self.changedir_button.setObjectName(u"changedir_button")
        sizePolicy1.setHeightForWidth(self.changedir_button.sizePolicy().hasHeightForWidth())
        self.changedir_button.setSizePolicy(sizePolicy1)
        self.changedir_button.setMinimumSize(QSize(0, 0))
        self.changedir_button.setMaximumSize(QSize(16777215, 16777215))
        self.changedir_button.setStyleSheet(u"")
        self.changedir_button.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.changedir_button)


        self.verticalLayout_2.addWidget(self.startbar_frame)

        self.display_widget = QWidget(self.mainFrame)
        self.display_widget.setObjectName(u"display_widget")
        self.display_widget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.display_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.display_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.horizontalLayout_15 = QHBoxLayout(self.home_page)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.home_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(421, 16777215))
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_14)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_4 = QSpacerItem(128, 173, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)

        self.homeLogo = QFrame(self.frame_14)
        self.homeLogo.setObjectName(u"homeLogo")
        self.homeLogo.setMinimumSize(QSize(421, 142))
        self.homeLogo.setMaximumSize(QSize(421, 16777215))
        self.homeLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.homeLogo.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout_19.addWidget(self.homeLogo)

        self.frame_welcome = QFrame(self.frame_14)
        self.frame_welcome.setObjectName(u"frame_welcome")
        self.frame_welcome.setMaximumSize(QSize(421, 16777215))
        self.frame_welcome.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_welcome.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_welcome)
        self.formLayout.setObjectName(u"formLayout")
        self.newproject_button = QPushButton(self.frame_welcome)
        self.newproject_button.setObjectName(u"newproject_button")
        sizePolicy1.setHeightForWidth(self.newproject_button.sizePolicy().hasHeightForWidth())
        self.newproject_button.setSizePolicy(sizePolicy1)
        self.newproject_button.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.newproject_button)

        self.label_6 = QLabel(self.frame_welcome)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_6)

        self.loadproject_button = QPushButton(self.frame_welcome)
        self.loadproject_button.setObjectName(u"loadproject_button")
        sizePolicy1.setHeightForWidth(self.loadproject_button.sizePolicy().hasHeightForWidth())
        self.loadproject_button.setSizePolicy(sizePolicy1)
        self.loadproject_button.setMinimumSize(QSize(0, 0))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.loadproject_button)

        self.label_7 = QLabel(self.frame_welcome)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_7)


        self.verticalLayout_19.addWidget(self.frame_welcome)

        self.verticalSpacer_3 = QSpacerItem(148, 173, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_3)


        self.horizontalLayout_15.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.home_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, -1)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)

        self.descriptionMsg = QLabel(self.frame_15)
        self.descriptionMsg.setObjectName(u"descriptionMsg")
        sizePolicy1.setHeightForWidth(self.descriptionMsg.sizePolicy().hasHeightForWidth())
        self.descriptionMsg.setSizePolicy(sizePolicy1)
        self.descriptionMsg.setFrameShape(QFrame.Shape.NoFrame)
        self.descriptionMsg.setWordWrap(True)
        self.descriptionMsg.setMargin(10)

        self.verticalLayout_11.addWidget(self.descriptionMsg)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_9)


        self.horizontalLayout_15.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.home_page)
        self.airfoil_page = QWidget()
        self.airfoil_page.setObjectName(u"airfoil_page")
        self.airfoil_page.setStyleSheet(u"")
        self.horizontalLayout_17 = QHBoxLayout(self.airfoil_page)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.airfoil_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_17)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_8)

        self.airfoil_parameters_frame = QFrame(self.frame_17)
        self.airfoil_parameters_frame.setObjectName(u"airfoil_parameters_frame")
        self.airfoil_parameters_frame.setStyleSheet(u"")
        self.gridLayout_18 = QGridLayout(self.airfoil_parameters_frame)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setVerticalSpacing(9)
        self.label_9 = QLabel(self.airfoil_parameters_frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(150, 16777215))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_9, 0, 0, 1, 1)

        self.airfoil_nacaseries_input = QComboBox(self.airfoil_parameters_frame)
        self.airfoil_nacaseries_input.addItem("")
        self.airfoil_nacaseries_input.addItem("")
        self.airfoil_nacaseries_input.addItem("")
        self.airfoil_nacaseries_input.setObjectName(u"airfoil_nacaseries_input")
        sizePolicy1.setHeightForWidth(self.airfoil_nacaseries_input.sizePolicy().hasHeightForWidth())
        self.airfoil_nacaseries_input.setSizePolicy(sizePolicy1)
        self.airfoil_nacaseries_input.setStyleSheet(u"")
        self.airfoil_nacaseries_input.setEditable(False)

        self.gridLayout_18.addWidget(self.airfoil_nacaseries_input, 0, 1, 1, 1)

        self.label_10 = QLabel(self.airfoil_parameters_frame)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setMaximumSize(QSize(150, 16777215))
        self.label_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_10, 1, 0, 1, 1)

        self.airfoil_seconddigit_input = QSpinBox(self.airfoil_parameters_frame)
        self.airfoil_seconddigit_input.setObjectName(u"airfoil_seconddigit_input")
        sizePolicy1.setHeightForWidth(self.airfoil_seconddigit_input.sizePolicy().hasHeightForWidth())
        self.airfoil_seconddigit_input.setSizePolicy(sizePolicy1)
        self.airfoil_seconddigit_input.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.airfoil_seconddigit_input.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.airfoil_seconddigit_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.airfoil_seconddigit_input.setProperty(u"showGroupSeparator", False)
        self.airfoil_seconddigit_input.setMaximum(9)
        self.airfoil_seconddigit_input.setValue(3)

        self.gridLayout_18.addWidget(self.airfoil_seconddigit_input, 1, 1, 1, 1)

        self.label_11 = QLabel(self.airfoil_parameters_frame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setMaximumSize(QSize(16777215, 16777215))
        self.label_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_11, 2, 0, 1, 1)

        self.airfoil_thirddigit_input = QSpinBox(self.airfoil_parameters_frame)
        self.airfoil_thirddigit_input.setObjectName(u"airfoil_thirddigit_input")
        sizePolicy1.setHeightForWidth(self.airfoil_thirddigit_input.sizePolicy().hasHeightForWidth())
        self.airfoil_thirddigit_input.setSizePolicy(sizePolicy1)
        self.airfoil_thirddigit_input.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.airfoil_thirddigit_input.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.airfoil_thirddigit_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.airfoil_thirddigit_input.setProperty(u"showGroupSeparator", False)
        self.airfoil_thirddigit_input.setValue(4)

        self.gridLayout_18.addWidget(self.airfoil_thirddigit_input, 2, 1, 1, 1)

        self.label_12 = QLabel(self.airfoil_parameters_frame)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setMaximumSize(QSize(150, 16777215))
        self.label_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_18.addWidget(self.label_12, 3, 0, 1, 1)

        self.airfoil_lasttwodigits_input = QSpinBox(self.airfoil_parameters_frame)
        self.airfoil_lasttwodigits_input.setObjectName(u"airfoil_lasttwodigits_input")
        sizePolicy1.setHeightForWidth(self.airfoil_lasttwodigits_input.sizePolicy().hasHeightForWidth())
        self.airfoil_lasttwodigits_input.setSizePolicy(sizePolicy1)
        self.airfoil_lasttwodigits_input.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.airfoil_lasttwodigits_input.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.airfoil_lasttwodigits_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.airfoil_lasttwodigits_input.setProperty(u"showGroupSeparator", False)
        self.airfoil_lasttwodigits_input.setValue(30)

        self.gridLayout_18.addWidget(self.airfoil_lasttwodigits_input, 3, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.airfoil_parameters_frame)

        self.horizontalFrame_2 = QFrame(self.frame_17)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.airfoil_calculateairfoil_button = QPushButton(self.horizontalFrame_2)
        self.airfoil_calculateairfoil_button.setObjectName(u"airfoil_calculateairfoil_button")
        sizePolicy1.setHeightForWidth(self.airfoil_calculateairfoil_button.sizePolicy().hasHeightForWidth())
        self.airfoil_calculateairfoil_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.airfoil_calculateairfoil_button)

        self.airfoil_saveairfoil_button = QPushButton(self.horizontalFrame_2)
        self.airfoil_saveairfoil_button.setObjectName(u"airfoil_saveairfoil_button")
        sizePolicy1.setHeightForWidth(self.airfoil_saveairfoil_button.sizePolicy().hasHeightForWidth())
        self.airfoil_saveairfoil_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.airfoil_saveairfoil_button)


        self.verticalLayout_20.addWidget(self.horizontalFrame_2)

        self.line = QFrame(self.frame_17)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.line)

        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_14)

        self.airfoil_listairfoils_widget = QListWidget(self.frame_17)
        self.airfoil_listairfoils_widget.setObjectName(u"airfoil_listairfoils_widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.airfoil_listairfoils_widget.sizePolicy().hasHeightForWidth())
        self.airfoil_listairfoils_widget.setSizePolicy(sizePolicy4)
        self.airfoil_listairfoils_widget.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.airfoil_listairfoils_widget.setStyleSheet(u"")
        self.airfoil_listairfoils_widget.setFrameShape(QFrame.Shape.NoFrame)
        self.airfoil_listairfoils_widget.setFrameShadow(QFrame.Shadow.Plain)
        self.airfoil_listairfoils_widget.setSpacing(0)
        self.airfoil_listairfoils_widget.setSelectionRectVisible(False)

        self.verticalLayout_20.addWidget(self.airfoil_listairfoils_widget)

        self.airfoil_delAirfoil_button = QPushButton(self.frame_17)
        self.airfoil_delAirfoil_button.setObjectName(u"airfoil_delAirfoil_button")
        sizePolicy2.setHeightForWidth(self.airfoil_delAirfoil_button.sizePolicy().hasHeightForWidth())
        self.airfoil_delAirfoil_button.setSizePolicy(sizePolicy2)
        self.airfoil_delAirfoil_button.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.airfoil_delAirfoil_button)


        self.horizontalLayout_17.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.airfoil_page)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_2 = QLabel(self.frame_18)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_21.addWidget(self.label_2)

        self.airfoil_graph_widget = QWidget(self.frame_18)
        self.airfoil_graph_widget.setObjectName(u"airfoil_graph_widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.airfoil_graph_widget.sizePolicy().hasHeightForWidth())
        self.airfoil_graph_widget.setSizePolicy(sizePolicy5)
        self.airfoil_graph_widget.setMinimumSize(QSize(0, 0))
        self.airfoil_graph_widget.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.airfoil_graph_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_21.addWidget(self.airfoil_graph_widget)


        self.horizontalLayout_17.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.airfoil_page)
        self.station_page = QWidget()
        self.station_page.setObjectName(u"station_page")
        self.station_page.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.station_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.station_tab_widget = QTabWidget(self.station_page)
        self.station_tab_widget.setObjectName(u"station_tab_widget")
        self.station_tab1 = QWidget()
        self.station_tab1.setObjectName(u"station_tab1")
        self.station_tab1.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.station_tab1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_2 = QFrame(self.station_tab1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_15)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.formLayout_3 = QFormLayout(self.frame_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_3.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_16)

        self.station_uploadairfoil_button = QPushButton(self.frame_3)
        self.station_uploadairfoil_button.setObjectName(u"station_uploadairfoil_button")
        sizePolicy1.setHeightForWidth(self.station_uploadairfoil_button.sizePolicy().hasHeightForWidth())
        self.station_uploadairfoil_button.setSizePolicy(sizePolicy1)
        self.station_uploadairfoil_button.setStyleSheet(u"")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.station_uploadairfoil_button)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_17)

        self.station_listairfoils_box = QComboBox(self.frame_3)
        self.station_listairfoils_box.setObjectName(u"station_listairfoils_box")
        sizePolicy1.setHeightForWidth(self.station_listairfoils_box.sizePolicy().hasHeightForWidth())
        self.station_listairfoils_box.setSizePolicy(sizePolicy1)
        self.station_listairfoils_box.setStyleSheet(u"")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.station_listairfoils_box)


        self.verticalLayout_12.addWidget(self.frame_3)

        self.verticalSpacer_6 = QSpacerItem(20, 55, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_18)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 0))
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_22, 3, 0, 1, 1)

        self.station_mirrory_input = QCheckBox(self.frame_4)
        self.station_mirrory_input.setObjectName(u"station_mirrory_input")
        sizePolicy1.setHeightForWidth(self.station_mirrory_input.sizePolicy().hasHeightForWidth())
        self.station_mirrory_input.setSizePolicy(sizePolicy1)
        self.station_mirrory_input.setChecked(True)

        self.gridLayout_9.addWidget(self.station_mirrory_input, 9, 2, 1, 1)

        self.label_24 = QLabel(self.frame_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 0))
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_24, 5, 0, 1, 1)

        self.label_25 = QLabel(self.frame_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 0))
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_25, 6, 0, 1, 1)

        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 0))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_21, 2, 0, 1, 1)

        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 0))
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_23, 4, 0, 1, 1)

        self.station_mirrorx_input = QCheckBox(self.frame_4)
        self.station_mirrorx_input.setObjectName(u"station_mirrorx_input")
        sizePolicy1.setHeightForWidth(self.station_mirrorx_input.sizePolicy().hasHeightForWidth())
        self.station_mirrorx_input.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.station_mirrorx_input, 8, 2, 1, 1)

        self.label_28 = QLabel(self.frame_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 0))
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_28, 9, 0, 1, 1)

        self.label_27 = QLabel(self.frame_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 0))
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_27, 8, 0, 1, 1)

        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 0))
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_26, 7, 0, 1, 1)

        self.station_multz_input = QLineEdit(self.frame_4)
        self.station_multz_input.setObjectName(u"station_multz_input")
        sizePolicy1.setHeightForWidth(self.station_multz_input.sizePolicy().hasHeightForWidth())
        self.station_multz_input.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.station_multz_input, 7, 1, 1, 3)

        self.station_multy_input = QLineEdit(self.frame_4)
        self.station_multy_input.setObjectName(u"station_multy_input")
        sizePolicy1.setHeightForWidth(self.station_multy_input.sizePolicy().hasHeightForWidth())
        self.station_multy_input.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.station_multy_input, 6, 1, 1, 3)

        self.station_multx_input = QLineEdit(self.frame_4)
        self.station_multx_input.setObjectName(u"station_multx_input")
        sizePolicy1.setHeightForWidth(self.station_multx_input.sizePolicy().hasHeightForWidth())
        self.station_multx_input.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.station_multx_input, 5, 1, 1, 3)

        self.station_offsetz_input = QLineEdit(self.frame_4)
        self.station_offsetz_input.setObjectName(u"station_offsetz_input")
        sizePolicy1.setHeightForWidth(self.station_offsetz_input.sizePolicy().hasHeightForWidth())
        self.station_offsetz_input.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.station_offsetz_input, 4, 1, 1, 3)

        self.station_offsety_input = QLineEdit(self.frame_4)
        self.station_offsety_input.setObjectName(u"station_offsety_input")
        sizePolicy1.setHeightForWidth(self.station_offsety_input.sizePolicy().hasHeightForWidth())
        self.station_offsety_input.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.station_offsety_input, 3, 1, 1, 3)

        self.station_offsetx_input = QLineEdit(self.frame_4)
        self.station_offsetx_input.setObjectName(u"station_offsetx_input")
        sizePolicy1.setHeightForWidth(self.station_offsetx_input.sizePolicy().hasHeightForWidth())
        self.station_offsetx_input.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.station_offsetx_input, 2, 1, 1, 3)

        self.station_twistangle_input = QLineEdit(self.frame_4)
        self.station_twistangle_input.setObjectName(u"station_twistangle_input")
        sizePolicy1.setHeightForWidth(self.station_twistangle_input.sizePolicy().hasHeightForWidth())
        self.station_twistangle_input.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.station_twistangle_input, 1, 1, 1, 3)

        self.station_chordlength_input = QLineEdit(self.frame_4)
        self.station_chordlength_input.setObjectName(u"station_chordlength_input")
        sizePolicy1.setHeightForWidth(self.station_chordlength_input.sizePolicy().hasHeightForWidth())
        self.station_chordlength_input.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.station_chordlength_input, 0, 1, 1, 3)

        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 0))
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_19, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.station_savestation_button = QPushButton(self.frame_5)
        self.station_savestation_button.setObjectName(u"station_savestation_button")
        sizePolicy1.setHeightForWidth(self.station_savestation_button.sizePolicy().hasHeightForWidth())
        self.station_savestation_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.station_savestation_button)

        self.station_delstation_button = QPushButton(self.frame_5)
        self.station_delstation_button.setObjectName(u"station_delstation_button")
        sizePolicy1.setHeightForWidth(self.station_delstation_button.sizePolicy().hasHeightForWidth())
        self.station_delstation_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.station_delstation_button)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_8)


        self.horizontalLayout_9.addWidget(self.frame_2)

        self.station_graph_frame = QFrame(self.station_tab1)
        self.station_graph_frame.setObjectName(u"station_graph_frame")
        sizePolicy5.setHeightForWidth(self.station_graph_frame.sizePolicy().hasHeightForWidth())
        self.station_graph_frame.setSizePolicy(sizePolicy5)
        self.station_graph_frame.setMinimumSize(QSize(0, 0))
        self.station_graph_frame.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.station_graph_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.station_graph_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.station_xy_current = QLabel(self.frame_6)
        self.station_xy_current.setObjectName(u"station_xy_current")

        self.horizontalLayout_7.addWidget(self.station_xy_current)


        self.verticalLayout_13.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.station_graph_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_7 = QFrame(self.frame_10)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_61 = QLabel(self.frame_7)
        self.label_61.setObjectName(u"label_61")
        sizePolicy1.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.label_61)

        self.station_chartview = QQuickWidget(self.frame_7)
        self.station_chartview.setObjectName(u"station_chartview")
        sizePolicy5.setHeightForWidth(self.station_chartview.sizePolicy().hasHeightForWidth())
        self.station_chartview.setSizePolicy(sizePolicy5)
        self.station_chartview.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)

        self.horizontalLayout_8.addWidget(self.station_chartview)


        self.verticalLayout_15.addWidget(self.frame_7)

        self.label_60 = QLabel(self.frame_10)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFrameShape(QFrame.Shape.NoFrame)
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_60)


        self.verticalLayout_13.addWidget(self.frame_10)

        self.frame = QFrame(self.station_graph_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 9, -1, -1)
        self.horizontalSpacer_11 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.label_35 = QLabel(self.frame)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_6.addWidget(self.label_35)

        self.station_liststation_box = QComboBox(self.frame)
        self.station_liststation_box.setObjectName(u"station_liststation_box")
        sizePolicy1.setHeightForWidth(self.station_liststation_box.sizePolicy().hasHeightForWidth())
        self.station_liststation_box.setSizePolicy(sizePolicy1)
        self.station_liststation_box.setMinimumSize(QSize(0, 0))
        self.station_liststation_box.setStyleSheet(u"")
        self.station_liststation_box.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.horizontalLayout_6.addWidget(self.station_liststation_box)

        self.horizontalSpacer_20 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_20)


        self.verticalLayout_13.addWidget(self.frame)


        self.horizontalLayout_9.addWidget(self.station_graph_frame)

        self.station_tab_widget.addTab(self.station_tab1, "")
        self.station_tab2 = QWidget()
        self.station_tab2.setObjectName(u"station_tab2")
        self.station_tab2.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.station_tab2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_8 = QFrame(self.station_tab2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_44 = QLabel(self.frame_8)
        self.label_44.setObjectName(u"label_44")
        sizePolicy1.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.label_44)

        self.station_nStationsAdv_input = QSpinBox(self.frame_8)
        self.station_nStationsAdv_input.setObjectName(u"station_nStationsAdv_input")
        sizePolicy1.setHeightForWidth(self.station_nStationsAdv_input.sizePolicy().hasHeightForWidth())
        self.station_nStationsAdv_input.setSizePolicy(sizePolicy1)
        self.station_nStationsAdv_input.setMinimumSize(QSize(100, 0))
        self.station_nStationsAdv_input.setMouseTracking(False)
        self.station_nStationsAdv_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.station_nStationsAdv_input.setProperty(u"showGroupSeparator", False)
        self.station_nStationsAdv_input.setMinimum(1)

        self.horizontalLayout_10.addWidget(self.station_nStationsAdv_input)

        self.horizontalSpacer_12 = QSpacerItem(875, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)


        self.verticalLayout_14.addWidget(self.frame_8)

        self.station_tableStations_input = QTableWidget(self.station_tab2)
        if (self.station_tableStations_input.columnCount() < 11):
            self.station_tableStations_input.setColumnCount(11)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        self.station_tableStations_input.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.station_tableStations_input.setObjectName(u"station_tableStations_input")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.station_tableStations_input.setFont(font3)
        self.station_tableStations_input.setStyleSheet(u"")
        self.station_tableStations_input.setFrameShape(QFrame.Shape.StyledPanel)
        self.station_tableStations_input.setFrameShadow(QFrame.Shadow.Raised)
        self.station_tableStations_input.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.station_tableStations_input.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)
        self.station_tableStations_input.setAlternatingRowColors(True)
        self.station_tableStations_input.setGridStyle(Qt.PenStyle.SolidLine)
        self.station_tableStations_input.setSortingEnabled(True)
        self.station_tableStations_input.setWordWrap(True)
        self.station_tableStations_input.setRowCount(0)
        self.station_tableStations_input.horizontalHeader().setCascadingSectionResizes(False)
        self.station_tableStations_input.horizontalHeader().setMinimumSectionSize(50)
        self.station_tableStations_input.horizontalHeader().setDefaultSectionSize(90)
        self.station_tableStations_input.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.station_tableStations_input.horizontalHeader().setStretchLastSection(False)
        self.station_tableStations_input.verticalHeader().setCascadingSectionResizes(False)
        self.station_tableStations_input.verticalHeader().setProperty(u"showSortIndicator", False)
        self.station_tableStations_input.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_14.addWidget(self.station_tableStations_input)

        self.frame_9 = QFrame(self.station_tab2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.station_impTable_button = QPushButton(self.frame_9)
        self.station_impTable_button.setObjectName(u"station_impTable_button")
        sizePolicy1.setHeightForWidth(self.station_impTable_button.sizePolicy().hasHeightForWidth())
        self.station_impTable_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.station_impTable_button)

        self.station_sortTable_button = QPushButton(self.frame_9)
        self.station_sortTable_button.setObjectName(u"station_sortTable_button")
        sizePolicy1.setHeightForWidth(self.station_sortTable_button.sizePolicy().hasHeightForWidth())
        self.station_sortTable_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.station_sortTable_button)

        self.station_saveTable_button = QPushButton(self.frame_9)
        self.station_saveTable_button.setObjectName(u"station_saveTable_button")
        sizePolicy1.setHeightForWidth(self.station_saveTable_button.sizePolicy().hasHeightForWidth())
        self.station_saveTable_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.station_saveTable_button)

        self.horizontalSpacer_4 = QSpacerItem(796, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)


        self.verticalLayout_14.addWidget(self.frame_9)

        self.station_tab_widget.addTab(self.station_tab2, "")

        self.gridLayout_8.addWidget(self.station_tab_widget, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.station_page)
        self.blade_page = QWidget()
        self.blade_page.setObjectName(u"blade_page")
        self.blade_page.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.blade_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_skin_loc = QFrame(self.blade_page)
        self.frame_skin_loc.setObjectName(u"frame_skin_loc")
        sizePolicy1.setHeightForWidth(self.frame_skin_loc.sizePolicy().hasHeightForWidth())
        self.frame_skin_loc.setSizePolicy(sizePolicy1)
        self.frame_skin_loc.setMaximumSize(QSize(16777215, 16777215))
        self.frame_skin_loc.setStyleSheet(u"")
        self.frame_skin_loc.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_4 = QVBoxLayout(self.frame_skin_loc)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_skin_loc)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.line_5 = QFrame(self.frame_skin_loc)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_5)

        self.skin_loc_radio1 = QRadioButton(self.frame_skin_loc)
        self.skin_loc_radio1.setObjectName(u"skin_loc_radio1")
        sizePolicy1.setHeightForWidth(self.skin_loc_radio1.sizePolicy().hasHeightForWidth())
        self.skin_loc_radio1.setSizePolicy(sizePolicy1)
        self.skin_loc_radio1.setChecked(True)

        self.verticalLayout_4.addWidget(self.skin_loc_radio1)

        self.skin_loc_radio2 = QRadioButton(self.frame_skin_loc)
        self.skin_loc_radio2.setObjectName(u"skin_loc_radio2")
        sizePolicy1.setHeightForWidth(self.skin_loc_radio2.sizePolicy().hasHeightForWidth())
        self.skin_loc_radio2.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.skin_loc_radio2)

        self.label_43 = QLabel(self.frame_skin_loc)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_43)

        self.blade_skinolpsta_table = QTableWidget(self.frame_skin_loc)
        if (self.blade_skinolpsta_table.columnCount() < 2):
            self.blade_skinolpsta_table.setColumnCount(2)
        font4 = QFont()
        font4.setBold(True)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font4);
        self.blade_skinolpsta_table.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font4);
        self.blade_skinolpsta_table.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        if (self.blade_skinolpsta_table.rowCount() < 2):
            self.blade_skinolpsta_table.setRowCount(2)
        self.blade_skinolpsta_table.setObjectName(u"blade_skinolpsta_table")
        sizePolicy1.setHeightForWidth(self.blade_skinolpsta_table.sizePolicy().hasHeightForWidth())
        self.blade_skinolpsta_table.setSizePolicy(sizePolicy1)
        self.blade_skinolpsta_table.setStyleSheet(u"")
        self.blade_skinolpsta_table.setAlternatingRowColors(True)
        self.blade_skinolpsta_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.blade_skinolpsta_table.setShowGrid(True)
        self.blade_skinolpsta_table.setGridStyle(Qt.PenStyle.SolidLine)
        self.blade_skinolpsta_table.setRowCount(2)
        self.blade_skinolpsta_table.setColumnCount(2)
        self.blade_skinolpsta_table.horizontalHeader().setVisible(True)
        self.blade_skinolpsta_table.horizontalHeader().setCascadingSectionResizes(False)
        self.blade_skinolpsta_table.horizontalHeader().setMinimumSectionSize(10)
        self.blade_skinolpsta_table.horizontalHeader().setDefaultSectionSize(100)
        self.blade_skinolpsta_table.horizontalHeader().setHighlightSections(True)
        self.blade_skinolpsta_table.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.blade_skinolpsta_table)

        self.loc_frame = QFrame(self.frame_skin_loc)
        self.loc_frame.setObjectName(u"loc_frame")
        sizePolicy1.setHeightForWidth(self.loc_frame.sizePolicy().hasHeightForWidth())
        self.loc_frame.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.loc_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_56 = QLabel(self.loc_frame)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_3.addWidget(self.label_56, 0, 0, 1, 1)

        self.skin_olp_loc_const = QLineEdit(self.loc_frame)
        self.skin_olp_loc_const.setObjectName(u"skin_olp_loc_const")
        sizePolicy1.setHeightForWidth(self.skin_olp_loc_const.sizePolicy().hasHeightForWidth())
        self.skin_olp_loc_const.setSizePolicy(sizePolicy1)
        self.skin_olp_loc_const.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.skin_olp_loc_const, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.loc_frame)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)


        self.gridLayout_2.addWidget(self.frame_skin_loc, 0, 0, 1, 1)

        self.frame_skin_len = QFrame(self.blade_page)
        self.frame_skin_len.setObjectName(u"frame_skin_len")
        sizePolicy1.setHeightForWidth(self.frame_skin_len.sizePolicy().hasHeightForWidth())
        self.frame_skin_len.setSizePolicy(sizePolicy1)
        self.frame_skin_len.setMaximumSize(QSize(16777215, 16777215))
        self.frame_skin_len.setStyleSheet(u"")
        self.frame_skin_len.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_5 = QVBoxLayout(self.frame_skin_len)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_37 = QLabel(self.frame_skin_len)
        self.label_37.setObjectName(u"label_37")
        sizePolicy1.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy1)
        self.label_37.setStyleSheet(u"")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_37)

        self.line_6 = QFrame(self.frame_skin_len)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_6)

        self.skin_len_radio1 = QRadioButton(self.frame_skin_len)
        self.skin_len_radio1.setObjectName(u"skin_len_radio1")
        sizePolicy1.setHeightForWidth(self.skin_len_radio1.sizePolicy().hasHeightForWidth())
        self.skin_len_radio1.setSizePolicy(sizePolicy1)
        self.skin_len_radio1.setChecked(True)

        self.verticalLayout_5.addWidget(self.skin_len_radio1)

        self.skin_len_radio2 = QRadioButton(self.frame_skin_len)
        self.skin_len_radio2.setObjectName(u"skin_len_radio2")
        sizePolicy1.setHeightForWidth(self.skin_len_radio2.sizePolicy().hasHeightForWidth())
        self.skin_len_radio2.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.skin_len_radio2)

        self.label_55 = QLabel(self.frame_skin_len)
        self.label_55.setObjectName(u"label_55")
        sizePolicy1.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy1)
        self.label_55.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_55)

        self.blade_skinolplen_table = QTableWidget(self.frame_skin_len)
        if (self.blade_skinolplen_table.columnCount() < 2):
            self.blade_skinolplen_table.setColumnCount(2)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font4);
        self.blade_skinolplen_table.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font4);
        self.blade_skinolplen_table.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        if (self.blade_skinolplen_table.rowCount() < 2):
            self.blade_skinolplen_table.setRowCount(2)
        self.blade_skinolplen_table.setObjectName(u"blade_skinolplen_table")
        sizePolicy1.setHeightForWidth(self.blade_skinolplen_table.sizePolicy().hasHeightForWidth())
        self.blade_skinolplen_table.setSizePolicy(sizePolicy1)
        self.blade_skinolplen_table.setStyleSheet(u"")
        self.blade_skinolplen_table.setAlternatingRowColors(True)
        self.blade_skinolplen_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.blade_skinolplen_table.setRowCount(2)
        self.blade_skinolplen_table.setColumnCount(2)
        self.blade_skinolplen_table.horizontalHeader().setMinimumSectionSize(10)

        self.verticalLayout_5.addWidget(self.blade_skinolplen_table)

        self.len_frame = QFrame(self.frame_skin_len)
        self.len_frame.setObjectName(u"len_frame")
        sizePolicy1.setHeightForWidth(self.len_frame.sizePolicy().hasHeightForWidth())
        self.len_frame.setSizePolicy(sizePolicy1)
        self.formLayout_6 = QFormLayout(self.len_frame)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_57 = QLabel(self.len_frame)
        self.label_57.setObjectName(u"label_57")
        sizePolicy1.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy1)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_57)

        self.skin_olp_len_const = QLineEdit(self.len_frame)
        self.skin_olp_len_const.setObjectName(u"skin_olp_len_const")
        sizePolicy1.setHeightForWidth(self.skin_olp_len_const.sizePolicy().hasHeightForWidth())
        self.skin_olp_len_const.setSizePolicy(sizePolicy1)
        self.skin_olp_len_const.setStyleSheet(u"")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.skin_olp_len_const)


        self.verticalLayout_5.addWidget(self.len_frame)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_11)


        self.gridLayout_2.addWidget(self.frame_skin_len, 0, 1, 1, 1)

        self.frame_ilp_order = QFrame(self.blade_page)
        self.frame_ilp_order.setObjectName(u"frame_ilp_order")
        self.frame_ilp_order.setStyleSheet(u"")
        self.frame_ilp_order.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_6 = QVBoxLayout(self.frame_ilp_order)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_16 = QFrame(self.frame_ilp_order)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_16)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_41 = QLabel(self.frame_16)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_5.addWidget(self.label_41, 0, 0, 1, 1)

        self.blade_order_input = QSpinBox(self.frame_16)
        self.blade_order_input.setObjectName(u"blade_order_input")
        sizePolicy1.setHeightForWidth(self.blade_order_input.sizePolicy().hasHeightForWidth())
        self.blade_order_input.setSizePolicy(sizePolicy1)
        self.blade_order_input.setStyleSheet(u"")
        self.blade_order_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.blade_order_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.blade_order_input.setMinimum(1)
        self.blade_order_input.setMaximum(3)
        self.blade_order_input.setValue(1)

        self.gridLayout_5.addWidget(self.blade_order_input, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.blade_interpolate_button = QPushButton(self.frame_ilp_order)
        self.blade_interpolate_button.setObjectName(u"blade_interpolate_button")
        sizePolicy1.setHeightForWidth(self.blade_interpolate_button.sizePolicy().hasHeightForWidth())
        self.blade_interpolate_button.setSizePolicy(sizePolicy1)
        self.blade_interpolate_button.setStyleSheet(u"")
        self.blade_interpolate_button.setCheckable(False)

        self.verticalLayout_6.addWidget(self.blade_interpolate_button)

        self.line_3 = QFrame(self.frame_ilp_order)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.label_40 = QLabel(self.frame_ilp_order)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_40)

        self.frame_19 = QFrame(self.frame_ilp_order)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_19)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_38 = QLabel(self.frame_19)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout.addWidget(self.label_38, 0, 0, 1, 1)

        self.blade_skinolpsta_selected = QComboBox(self.frame_19)
        self.blade_skinolpsta_selected.setObjectName(u"blade_skinolpsta_selected")
        sizePolicy1.setHeightForWidth(self.blade_skinolpsta_selected.sizePolicy().hasHeightForWidth())
        self.blade_skinolpsta_selected.setSizePolicy(sizePolicy1)
        self.blade_skinolpsta_selected.setEditable(False)

        self.gridLayout.addWidget(self.blade_skinolpsta_selected, 0, 1, 1, 1)

        self.label_39 = QLabel(self.frame_19)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout.addWidget(self.label_39, 1, 0, 1, 1)

        self.blade_skinolplen_selected = QComboBox(self.frame_19)
        self.blade_skinolplen_selected.setObjectName(u"blade_skinolplen_selected")
        sizePolicy1.setHeightForWidth(self.blade_skinolplen_selected.sizePolicy().hasHeightForWidth())
        self.blade_skinolplen_selected.setSizePolicy(sizePolicy1)
        self.blade_skinolplen_selected.setEditable(False)

        self.gridLayout.addWidget(self.blade_skinolplen_selected, 1, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_19)

        self.blade_saveparams_button = QPushButton(self.frame_ilp_order)
        self.blade_saveparams_button.setObjectName(u"blade_saveparams_button")
        sizePolicy1.setHeightForWidth(self.blade_saveparams_button.sizePolicy().hasHeightForWidth())
        self.blade_saveparams_button.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.blade_saveparams_button)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_16)


        self.gridLayout_2.addWidget(self.frame_ilp_order, 1, 0, 1, 1)

        self.frame_ilp_values = QFrame(self.blade_page)
        self.frame_ilp_values.setObjectName(u"frame_ilp_values")
        sizePolicy1.setHeightForWidth(self.frame_ilp_values.sizePolicy().hasHeightForWidth())
        self.frame_ilp_values.setSizePolicy(sizePolicy1)
        self.frame_ilp_values.setStyleSheet(u"")
        self.frame_ilp_values.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_7 = QVBoxLayout(self.frame_ilp_values)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_52 = QLabel(self.frame_ilp_values)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_7.addWidget(self.label_52)

        self.tableView = QTableView(self.frame_ilp_values)
        self.tableView.setObjectName(u"tableView")
        sizePolicy4.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy4)
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(10)
        self.tableView.horizontalHeader().setDefaultSectionSize(80)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_7.addWidget(self.tableView)


        self.gridLayout_2.addWidget(self.frame_ilp_values, 1, 1, 1, 1)

        self.frame_skin_graphs = QFrame(self.blade_page)
        self.frame_skin_graphs.setObjectName(u"frame_skin_graphs")
        self.frame_skin_graphs.setStyleSheet(u"")
        self.frame_skin_graphs.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_3 = QVBoxLayout(self.frame_skin_graphs)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_49 = QLabel(self.frame_skin_graphs)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_3.addWidget(self.label_49)

        self.blade_olplen_chartview = QQuickWidget(self.frame_skin_graphs)
        self.blade_olplen_chartview.setObjectName(u"blade_olplen_chartview")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.blade_olplen_chartview.sizePolicy().hasHeightForWidth())
        self.blade_olplen_chartview.setSizePolicy(sizePolicy6)
        self.blade_olplen_chartview.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)

        self.verticalLayout_3.addWidget(self.blade_olplen_chartview)

        self.label_48 = QLabel(self.frame_skin_graphs)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_3.addWidget(self.label_48)

        self.blade_olpsta_chartview = QQuickWidget(self.frame_skin_graphs)
        self.blade_olpsta_chartview.setObjectName(u"blade_olpsta_chartview")
        sizePolicy6.setHeightForWidth(self.blade_olpsta_chartview.sizePolicy().hasHeightForWidth())
        self.blade_olpsta_chartview.setSizePolicy(sizePolicy6)
        self.blade_olpsta_chartview.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)

        self.verticalLayout_3.addWidget(self.blade_olpsta_chartview)


        self.gridLayout_2.addWidget(self.frame_skin_graphs, 0, 3, 2, 1)

        self.stackedWidget.addWidget(self.blade_page)
        self.skin_page = QWidget()
        self.skin_page.setObjectName(u"skin_page")
        self.skin_page.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.skin_page)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.skin_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_29 = QLabel(self.frame_11)
        self.label_29.setObjectName(u"label_29")
        sizePolicy1.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy1)
        self.label_29.setFont(font1)
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_29)

        self.frame_sec_params = QFrame(self.frame_11)
        self.frame_sec_params.setObjectName(u"frame_sec_params")
        sizePolicy1.setHeightForWidth(self.frame_sec_params.sizePolicy().hasHeightForWidth())
        self.frame_sec_params.setSizePolicy(sizePolicy1)
        self.frame_sec_params.setStyleSheet(u"")
        self.formLayout_4 = QFormLayout(self.frame_sec_params)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_30 = QLabel(self.frame_sec_params)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_30)

        self.skin_liststations = QComboBox(self.frame_sec_params)
        self.skin_liststations.setObjectName(u"skin_liststations")
        sizePolicy1.setHeightForWidth(self.skin_liststations.sizePolicy().hasHeightForWidth())
        self.skin_liststations.setSizePolicy(sizePolicy1)
        self.skin_liststations.setStyleSheet(u"")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.skin_liststations)

        self.label_31 = QLabel(self.frame_sec_params)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_31)

        self.skin_nplies_input = QLineEdit(self.frame_sec_params)
        self.skin_nplies_input.setObjectName(u"skin_nplies_input")
        sizePolicy1.setHeightForWidth(self.skin_nplies_input.sizePolicy().hasHeightForWidth())
        self.skin_nplies_input.setSizePolicy(sizePolicy1)

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.skin_nplies_input)

        self.label_32 = QLabel(self.frame_sec_params)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_32)

        self.skin_plythickness_input = QLineEdit(self.frame_sec_params)
        self.skin_plythickness_input.setObjectName(u"skin_plythickness_input")
        sizePolicy1.setHeightForWidth(self.skin_plythickness_input.sizePolicy().hasHeightForWidth())
        self.skin_plythickness_input.setSizePolicy(sizePolicy1)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.skin_plythickness_input)

        self.label_33 = QLabel(self.frame_sec_params)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_33)

        self.skin_overlaptarget_input = QLineEdit(self.frame_sec_params)
        self.skin_overlaptarget_input.setObjectName(u"skin_overlaptarget_input")
        sizePolicy1.setHeightForWidth(self.skin_overlaptarget_input.sizePolicy().hasHeightForWidth())
        self.skin_overlaptarget_input.setSizePolicy(sizePolicy1)
        self.skin_overlaptarget_input.setStyleSheet(u"")
        self.skin_overlaptarget_input.setReadOnly(True)

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.FieldRole, self.skin_overlaptarget_input)

        self.label_34 = QLabel(self.frame_sec_params)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_34)

        self.skin_tethickness_input = QLineEdit(self.frame_sec_params)
        self.skin_tethickness_input.setObjectName(u"skin_tethickness_input")
        sizePolicy1.setHeightForWidth(self.skin_tethickness_input.sizePolicy().hasHeightForWidth())
        self.skin_tethickness_input.setSizePolicy(sizePolicy1)

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.FieldRole, self.skin_tethickness_input)

        self.label_54 = QLabel(self.frame_sec_params)
        self.label_54.setObjectName(u"label_54")

        self.formLayout_4.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_54)

        self.skin_bond_input = QLineEdit(self.frame_sec_params)
        self.skin_bond_input.setObjectName(u"skin_bond_input")
        sizePolicy1.setHeightForWidth(self.skin_bond_input.sizePolicy().hasHeightForWidth())
        self.skin_bond_input.setSizePolicy(sizePolicy1)

        self.formLayout_4.setWidget(5, QFormLayout.ItemRole.FieldRole, self.skin_bond_input)

        self.label_59 = QLabel(self.frame_sec_params)
        self.label_59.setObjectName(u"label_59")

        self.formLayout_4.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_59)

        self.skin_jiggle_toggle = QCheckBox(self.frame_sec_params)
        self.skin_jiggle_toggle.setObjectName(u"skin_jiggle_toggle")
        sizePolicy1.setHeightForWidth(self.skin_jiggle_toggle.sizePolicy().hasHeightForWidth())
        self.skin_jiggle_toggle.setSizePolicy(sizePolicy1)
        self.skin_jiggle_toggle.setChecked(True)

        self.formLayout_4.setWidget(6, QFormLayout.ItemRole.FieldRole, self.skin_jiggle_toggle)

        self.label_36 = QLabel(self.frame_sec_params)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_4.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_36)

        self.skin_savefig_input = QCheckBox(self.frame_sec_params)
        self.skin_savefig_input.setObjectName(u"skin_savefig_input")
        sizePolicy1.setHeightForWidth(self.skin_savefig_input.sizePolicy().hasHeightForWidth())
        self.skin_savefig_input.setSizePolicy(sizePolicy1)
        self.skin_savefig_input.setMinimumSize(QSize(0, 0))
        self.skin_savefig_input.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_4.setWidget(7, QFormLayout.ItemRole.FieldRole, self.skin_savefig_input)


        self.verticalLayout_17.addWidget(self.frame_sec_params)

        self.widget_11 = QWidget(self.frame_11)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.skin_delSection_button = QPushButton(self.widget_11)
        self.skin_delSection_button.setObjectName(u"skin_delSection_button")
        sizePolicy1.setHeightForWidth(self.skin_delSection_button.sizePolicy().hasHeightForWidth())
        self.skin_delSection_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.skin_delSection_button)

        self.skin_saveSection_button = QPushButton(self.widget_11)
        self.skin_saveSection_button.setObjectName(u"skin_saveSection_button")
        sizePolicy1.setHeightForWidth(self.skin_saveSection_button.sizePolicy().hasHeightForWidth())
        self.skin_saveSection_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.skin_saveSection_button)

        self.skin_saveAll_button = QPushButton(self.widget_11)
        self.skin_saveAll_button.setObjectName(u"skin_saveAll_button")
        sizePolicy1.setHeightForWidth(self.skin_saveAll_button.sizePolicy().hasHeightForWidth())
        self.skin_saveAll_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.skin_saveAll_button)


        self.verticalLayout_17.addWidget(self.widget_11)

        self.line_4 = QFrame(self.frame_11)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_4)

        self.skin_zoomedgraph_frame = QFrame(self.frame_11)
        self.skin_zoomedgraph_frame.setObjectName(u"skin_zoomedgraph_frame")
        self.skin_zoomedgraph_frame.setMinimumSize(QSize(0, 0))
        self.skin_zoomedgraph_frame.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.skin_zoomedgraph_frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.skin_zoomedgraph_frame)
        self.label_51.setObjectName(u"label_51")

        self.verticalLayout_22.addWidget(self.label_51)

        self.label_53 = QLabel(self.skin_zoomedgraph_frame)
        self.label_53.setObjectName(u"label_53")
        sizePolicy1.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy1)
        self.label_53.setMaximumSize(QSize(250, 250))
        self.label_53.setStyleSheet(u"")
        self.label_53.setPixmap(QPixmap(u":/resources/images/skin_help.png"))
        self.label_53.setScaledContents(True)
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_53)


        self.verticalLayout_17.addWidget(self.skin_zoomedgraph_frame)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_5)


        self.horizontalLayout_12.addWidget(self.frame_11)

        self.skin_maingraph_frame = QFrame(self.skin_page)
        self.skin_maingraph_frame.setObjectName(u"skin_maingraph_frame")
        self.skin_maingraph_frame.setMinimumSize(QSize(0, 0))
        self.skin_maingraph_frame.setStyleSheet(u"")
        self.skin_maingraph_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_16 = QVBoxLayout(self.skin_maingraph_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_50 = QLabel(self.skin_maingraph_frame)
        self.label_50.setObjectName(u"label_50")

        self.verticalLayout_16.addWidget(self.label_50)

        self.skin_full_chart = QWidget(self.skin_maingraph_frame)
        self.skin_full_chart.setObjectName(u"skin_full_chart")
        sizePolicy5.setHeightForWidth(self.skin_full_chart.sizePolicy().hasHeightForWidth())
        self.skin_full_chart.setSizePolicy(sizePolicy5)
        self.skin_full_chart.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.skin_full_chart)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_16.addWidget(self.skin_full_chart)


        self.horizontalLayout_12.addWidget(self.skin_maingraph_frame)

        self.stackedWidget.addWidget(self.skin_page)
        self.export_page = QWidget()
        self.export_page.setObjectName(u"export_page")
        self.horizontalLayout_14 = QHBoxLayout(self.export_page)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.export_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_12)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_42 = QLabel(self.frame_12)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_42)

        self.widget_13 = QWidget(self.frame_12)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.verticalLayout_8 = QVBoxLayout(self.widget_13)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_58 = QLabel(self.widget_13)
        self.label_58.setObjectName(u"label_58")

        self.verticalLayout_8.addWidget(self.label_58)

        self.export_json_toggle = QRadioButton(self.widget_13)
        self.export_json_toggle.setObjectName(u"export_json_toggle")
        sizePolicy1.setHeightForWidth(self.export_json_toggle.sizePolicy().hasHeightForWidth())
        self.export_json_toggle.setSizePolicy(sizePolicy1)
        self.export_json_toggle.setChecked(True)

        self.verticalLayout_8.addWidget(self.export_json_toggle)

        self.export_csv_toggle = QRadioButton(self.widget_13)
        self.export_csv_toggle.setObjectName(u"export_csv_toggle")
        sizePolicy1.setHeightForWidth(self.export_csv_toggle.sizePolicy().hasHeightForWidth())
        self.export_csv_toggle.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.export_csv_toggle)


        self.verticalLayout_18.addWidget(self.widget_13)

        self.export_sectionsList = QListWidget(self.frame_12)
        self.export_sectionsList.setObjectName(u"export_sectionsList")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.export_sectionsList.sizePolicy().hasHeightForWidth())
        self.export_sectionsList.setSizePolicy(sizePolicy7)
        self.export_sectionsList.setStyleSheet(u"")
        self.export_sectionsList.setFrameShape(QFrame.Shape.NoFrame)
        self.export_sectionsList.setFrameShadow(QFrame.Shadow.Plain)
        self.export_sectionsList.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)
        self.export_sectionsList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_18.addWidget(self.export_sectionsList)

        self.label_45 = QLabel(self.frame_12)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_18.addWidget(self.label_45)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_46 = QLabel(self.frame_13)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_13.addWidget(self.label_46)

        self.export_expFileName_input = QLineEdit(self.frame_13)
        self.export_expFileName_input.setObjectName(u"export_expFileName_input")
        sizePolicy1.setHeightForWidth(self.export_expFileName_input.sizePolicy().hasHeightForWidth())
        self.export_expFileName_input.setSizePolicy(sizePolicy1)
        self.export_expFileName_input.setMaximumSize(QSize(200, 16777215))
        self.export_expFileName_input.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.export_expFileName_input)

        self.label_47 = QLabel(self.frame_13)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_13.addWidget(self.label_47)

        self.export_export_button = QPushButton(self.frame_13)
        self.export_export_button.setObjectName(u"export_export_button")
        sizePolicy1.setHeightForWidth(self.export_export_button.sizePolicy().hasHeightForWidth())
        self.export_export_button.setSizePolicy(sizePolicy1)
        self.export_export_button.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.export_export_button)


        self.verticalLayout_18.addWidget(self.frame_13)


        self.horizontalLayout_14.addWidget(self.frame_12)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_27)

        self.stackedWidget.addWidget(self.export_page)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.display_widget)

        self.statusBar = QFrame(self.mainFrame)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMinimumSize(QSize(0, 0))
        self.statusBar.setStyleSheet(u"")
        self.statusBar.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.statusBar)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 9, 9, 9)
        self.def_msgbar = QLabel(self.statusBar)
        self.def_msgbar.setObjectName(u"def_msgbar")
        sizePolicy3.setHeightForWidth(self.def_msgbar.sizePolicy().hasHeightForWidth())
        self.def_msgbar.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.def_msgbar)

        self.msgbar = QLabel(self.statusBar)
        self.msgbar.setObjectName(u"msgbar")
        sizePolicy3.setHeightForWidth(self.msgbar.sizePolicy().hasHeightForWidth())
        self.msgbar.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.msgbar)

        self.progressBar = QProgressBar(self.statusBar)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMinimumSize(QSize(120, 0))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        self.progressBar.setFont(font5)
        self.progressBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(100)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.statusBar)


        self.appLayout.addWidget(self.mainFrame)


        self.appMargins.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.stylesheet)
        QWidget.setTabOrder(self.home_page_button, self.airfoil_page_button)
        QWidget.setTabOrder(self.airfoil_page_button, self.station_page_button)
        QWidget.setTabOrder(self.station_page_button, self.blade_page_button)
        QWidget.setTabOrder(self.blade_page_button, self.skin_page_button)
        QWidget.setTabOrder(self.skin_page_button, self.export_page_button)
        QWidget.setTabOrder(self.export_page_button, self.settings_button)
        QWidget.setTabOrder(self.settings_button, self.info_button)
        QWidget.setTabOrder(self.info_button, self.quit_button)
        QWidget.setTabOrder(self.quit_button, self.workpath_lineedit)
        QWidget.setTabOrder(self.workpath_lineedit, self.changedir_button)
        QWidget.setTabOrder(self.changedir_button, self.airfoil_calculateairfoil_button)
        QWidget.setTabOrder(self.airfoil_calculateairfoil_button, self.airfoil_seconddigit_input)
        QWidget.setTabOrder(self.airfoil_seconddigit_input, self.airfoil_thirddigit_input)
        QWidget.setTabOrder(self.airfoil_thirddigit_input, self.airfoil_lasttwodigits_input)
        QWidget.setTabOrder(self.airfoil_lasttwodigits_input, self.station_uploadairfoil_button)
        QWidget.setTabOrder(self.station_uploadairfoil_button, self.station_listairfoils_box)
        QWidget.setTabOrder(self.station_listairfoils_box, self.station_chordlength_input)
        QWidget.setTabOrder(self.station_chordlength_input, self.station_twistangle_input)
        QWidget.setTabOrder(self.station_twistangle_input, self.station_offsetx_input)
        QWidget.setTabOrder(self.station_offsetx_input, self.station_offsety_input)
        QWidget.setTabOrder(self.station_offsety_input, self.station_offsetz_input)
        QWidget.setTabOrder(self.station_offsetz_input, self.station_multx_input)
        QWidget.setTabOrder(self.station_multx_input, self.station_multy_input)
        QWidget.setTabOrder(self.station_multy_input, self.station_multz_input)
        QWidget.setTabOrder(self.station_multz_input, self.station_mirrorx_input)
        QWidget.setTabOrder(self.station_mirrorx_input, self.station_mirrory_input)
        QWidget.setTabOrder(self.station_mirrory_input, self.station_savestation_button)
        QWidget.setTabOrder(self.station_savestation_button, self.station_delstation_button)
        QWidget.setTabOrder(self.station_delstation_button, self.blade_skinolplen_table)
        QWidget.setTabOrder(self.blade_skinolplen_table, self.blade_skinolpsta_table)
        QWidget.setTabOrder(self.blade_skinolpsta_table, self.skin_liststations)
        QWidget.setTabOrder(self.skin_liststations, self.skin_nplies_input)
        QWidget.setTabOrder(self.skin_nplies_input, self.skin_plythickness_input)
        QWidget.setTabOrder(self.skin_plythickness_input, self.skin_overlaptarget_input)
        QWidget.setTabOrder(self.skin_overlaptarget_input, self.skin_tethickness_input)
        QWidget.setTabOrder(self.skin_tethickness_input, self.skin_savefig_input)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.station_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.topName.setText(QCoreApplication.translate("MainWindow", u"EdFoil", None))
        self.topInfo.setText(QCoreApplication.translate("MainWindow", u"UoEdinburgh", None))
        self.home_page_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.airfoil_page_button.setText(QCoreApplication.translate("MainWindow", u"Airfoil Creator", None))
        self.station_page_button.setText(QCoreApplication.translate("MainWindow", u"Station Generator", None))
        self.blade_page_button.setText(QCoreApplication.translate("MainWindow", u"Blade Parameters", None))
        self.skin_page_button.setText(QCoreApplication.translate("MainWindow", u"Skin Sections", None))
        self.export_page_button.setText(QCoreApplication.translate("MainWindow", u"Blade Export", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.info_button.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.quit_button.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.page_title_label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Work Directory:", None))
        self.workpath_lineedit.setText("")
        self.changedir_button.setText(QCoreApplication.translate("MainWindow", u"Change...", None))
        self.newproject_button.setText(QCoreApplication.translate("MainWindow", u"New Project...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Welcome to EdFoil", None))
#if QT_CONFIG(tooltip)
        self.loadproject_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Coming Soon.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.loadproject_button.setText(QCoreApplication.translate("MainWindow", u"Load Project...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Version 0.3.0", None))
        self.descriptionMsg.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Welcome to EdFoil!<span style=\" font-size:10pt;\"><br/></span></p><p><span style=\" font-size:10pt; font-weight:400;\">This is a contained design tool to generate guide curves for a 3D model of wind and tidal turbine blades.</span></p><p><span style=\" font-size:10pt; font-weight:400;\">The workflow to get the curves is the following:</span></p><ol><li><span style=\" font-size:10pt; font-weight:400;\">Generate or upload NACA airfoils to the current session (&quot;Airfoil Creator&quot; tab)</span></li><li><span style=\" font-size:10pt; font-weight:400;\"> Assign parameters (e.g., twist angle, chord length) to airfoils at key stations along the span of the blade. (&quot;Station Generator&quot; tab)</span></li><li><span style=\" font-size:10pt; font-weight:400;\"> Determine blade parameters (&quot;Blade Parameters&quot; tab) such as:</span></li><ul><li><span style=\" font-size:10pt; font-weight:400;\">Where the skin is split in top and bottom surfaces.</span></li><li><span style=\" font-siz"
                        "e:10pt; font-weight:400;\">The overlap distance of the top and bottom skin surfaces.</span></li><li><span style=\" font-size:10pt; font-weight:400;\">The thickness of the adhesive.</span></li><li><span style=\" font-size:10pt; font-weight:400;\">The trailing edge trim distance.</span></li></ul><li><span style=\" font-size:10pt; font-weight:400;\">Determine ply parameters for the skin (&quot;Skin&quot; tab) such as number of plies, and ply thickness.</span></li><li><span style=\" font-size:10pt; font-weight:400;\">Export the point cloud to be imported to CAD softwares (e.g., SolidWorks, Abaqus CAE)</span></ol></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"NACA series:", None))
        self.airfoil_nacaseries_input.setItemText(0, QCoreApplication.translate("MainWindow", u"NACA 4-digit", None))
        self.airfoil_nacaseries_input.setItemText(1, QCoreApplication.translate("MainWindow", u"NACA 6-series", None))
        self.airfoil_nacaseries_input.setItemText(2, QCoreApplication.translate("MainWindow", u"NACA 6A-series", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"1st digit (max camber):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"2nd digit (pos max camber)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Last two digits (thickness):", None))
        self.airfoil_calculateairfoil_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.airfoil_saveairfoil_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Airfoils available:", None))
        self.airfoil_delAirfoil_button.setText(QCoreApplication.translate("MainWindow", u"Delete airfoil", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Airfoil Plot", None))
#if QT_CONFIG(tooltip)
        self.station_tab_widget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Airfoil", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Upload airfoil file:", None))
        self.station_uploadairfoil_button.setText(QCoreApplication.translate("MainWindow", u"Select file...", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Available airfoils:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Offset y:", None))
        self.station_mirrory_input.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Multiplier x:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Multiplier y:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Offset x:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Twist angle:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Offset z:", None))
        self.station_mirrorx_input.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Mirror y:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Mirror x:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Multiplier z:", None))
        self.station_multz_input.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.station_multy_input.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.station_multx_input.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.station_offsetz_input.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.station_offsety_input.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.station_offsetx_input.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.station_twistangle_input.setText(QCoreApplication.translate("MainWindow", u"18.0", None))
        self.station_chordlength_input.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Chord length:", None))
        self.station_savestation_button.setText(QCoreApplication.translate("MainWindow", u"Save Station", None))
        self.station_delstation_button.setText(QCoreApplication.translate("MainWindow", u"Delete Station", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Station Plot", None))
        self.station_xy_current.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"y [d]", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"x [d]", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Current station:", None))
        self.station_tab_widget.setTabText(self.station_tab_widget.indexOf(self.station_tab1), QCoreApplication.translate("MainWindow", u"Interactive", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Number of stations:", None))
        ___qtablewidgetitem = self.station_tableStations_input.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Airfoil", None));
        ___qtablewidgetitem1 = self.station_tableStations_input.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Chord Length", None));
        ___qtablewidgetitem2 = self.station_tableStations_input.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Twist Angle", None));
        ___qtablewidgetitem3 = self.station_tableStations_input.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"x-offset", None));
        ___qtablewidgetitem4 = self.station_tableStations_input.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"y-offset", None));
        ___qtablewidgetitem5 = self.station_tableStations_input.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"z-offset", None));
        ___qtablewidgetitem6 = self.station_tableStations_input.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"x-multiplier", None));
        ___qtablewidgetitem7 = self.station_tableStations_input.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"y-multiplier", None));
        ___qtablewidgetitem8 = self.station_tableStations_input.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"z-mutiplier", None));
        ___qtablewidgetitem9 = self.station_tableStations_input.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"x-mirror", None));
        ___qtablewidgetitem10 = self.station_tableStations_input.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"y-mirror", None));
#if QT_CONFIG(tooltip)
        self.station_impTable_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">IMPORTANT: This deletes all previously saved stations.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.station_impTable_button.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.station_impTable_button.setText(QCoreApplication.translate("MainWindow", u"Import from file...", None))
#if QT_CONFIG(tooltip)
        self.station_sortTable_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Sorts the stations based on the Z axis.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.station_sortTable_button.setText(QCoreApplication.translate("MainWindow", u"Sort Stations", None))
        self.station_saveTable_button.setText(QCoreApplication.translate("MainWindow", u"Save Stations", None))
        self.station_tab_widget.setTabText(self.station_tab_widget.indexOf(self.station_tab2), QCoreApplication.translate("MainWindow", u"Advanced", None))
#if QT_CONFIG(tooltip)
        self.frame_skin_loc.setToolTip(QCoreApplication.translate("MainWindow", u"Location of the overlap normalised to the local chord length.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Skin Overlap Location", None))
        self.skin_loc_radio1.setText(QCoreApplication.translate("MainWindow", u"As a function of the chord length (c)", None))
        self.skin_loc_radio2.setText(QCoreApplication.translate("MainWindow", u"Constant along the blade [d]", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Input values:", None))
        ___qtablewidgetitem11 = self.blade_skinolpsta_table.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Z [d]", None));
        ___qtablewidgetitem12 = self.blade_skinolpsta_table.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Norm. Value [-]", None));
#if QT_CONFIG(tooltip)
        self.loc_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Less than the smallest \n"
"chord length", None))
#endif // QT_CONFIG(tooltip)
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Distance from the LE: ", None))
#if QT_CONFIG(tooltip)
        self.frame_skin_len.setToolTip(QCoreApplication.translate("MainWindow", u"Length of the overlap normalised to the local chord length.", None))
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Skin Overlap Length", None))
        self.skin_len_radio1.setText(QCoreApplication.translate("MainWindow", u"As a function of the chord length (c)", None))
        self.skin_len_radio2.setText(QCoreApplication.translate("MainWindow", u"Constant along the blade [d]", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Input values:", None))
        ___qtablewidgetitem13 = self.blade_skinolplen_table.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Z [d]", None));
        ___qtablewidgetitem14 = self.blade_skinolplen_table.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Norm. Value [-]", None));
#if QT_CONFIG(tooltip)
        self.len_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Distance parallel to\n"
"the chord length", None))
#endif // QT_CONFIG(tooltip)
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Total overlap distance:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Interpolation order:", None))
#if QT_CONFIG(tooltip)
        self.blade_order_input.setToolTip(QCoreApplication.translate("MainWindow", u"1 = Linear interpolation.\n"
"2 = Quadratic interpolation.\n"
"etc.", None))
#endif // QT_CONFIG(tooltip)
        self.blade_order_input.setSuffix("")
        self.blade_interpolate_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Choose skin interpolation order:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.blade_saveparams_button.setText(QCoreApplication.translate("MainWindow", u"Save Parameters", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Interpolation values at each station:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Interpolation Factors", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Blade Top View", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Available stations:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Number of plies:", None))
        self.skin_nplies_input.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Ply thickness:", None))
        self.skin_plythickness_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Skin top/bottom split:", None))
#if QT_CONFIG(tooltip)
        self.skin_overlaptarget_input.setToolTip(QCoreApplication.translate("MainWindow", u"Calculated (Non-editable)", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Trailing edge thickness:", None))
        self.skin_tethickness_input.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Bond thickness:", None))
        self.skin_bond_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Generate overlap:", None))
        self.skin_jiggle_toggle.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Save figures:", None))
        self.skin_savefig_input.setText("")
        self.skin_delSection_button.setText(QCoreApplication.translate("MainWindow", u"Delete Section", None))
        self.skin_saveSection_button.setText(QCoreApplication.translate("MainWindow", u"Save Section", None))
#if QT_CONFIG(tooltip)
        self.skin_saveAll_button.setToolTip(QCoreApplication.translate("MainWindow", u"Save all stations at once.\n"
"Parameters are the same for all.", None))
#endif // QT_CONFIG(tooltip)
        self.skin_saveAll_button.setText(QCoreApplication.translate("MainWindow", u"Save All", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Parameters guide:", None))
        self.label_53.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Cross Section Plot", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Export Sections", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Select the export type:", None))
        self.export_json_toggle.setText(QCoreApplication.translate("MainWindow", u"Single File (JSON) - General purpose and scripting", None))
        self.export_csv_toggle.setText(QCoreApplication.translate("MainWindow", u"Multiple files (CSV) - Optmised for SolidWorks", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Select the sections to be exported as .json files:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Export file name:", None))
        self.export_expFileName_input.setText(QCoreApplication.translate("MainWindow", u"skin", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u".json", None))
        self.export_export_button.setText(QCoreApplication.translate("MainWindow", u"Export Sections", None))
        self.def_msgbar.setText(QCoreApplication.translate("MainWindow", u"Ready.", None))
        self.msgbar.setText("")
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
    # retranslateUi

