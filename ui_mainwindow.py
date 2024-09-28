# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #0B212E;\n"
"}\n"
"\n"
"QStatusBar{\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,255,255,0.4);\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QFrame{\n"
"	border:none;\n"
"}\n"
"\n"
"Line{\n"
"	color: #0B212E;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_widget = QWidget(self.centralwidget)
        self.sidebar_widget.setObjectName(u"sidebar_widget")
        self.sidebar_widget.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	font:10pt;\n"
"	text-align:left;\n"
"	border:none;\n"
"	height:30px;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.sidebar_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.label_2 = QLabel(self.sidebar_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setMaximumSize(QSize(150, 40))
        self.label_2.setPixmap(QPixmap(u":/resources/images/simbladed.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(150, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.home_page_button = QPushButton(self.sidebar_widget)
        self.home_page_button.setObjectName(u"home_page_button")
        self.home_page_button.setMinimumSize(QSize(150, 0))
        self.home_page_button.setMaximumSize(QSize(200, 16777215))
        self.home_page_button.setStyleSheet(u"QPushButton:checked{\n"
"	color: rgb(35, 46, 47);\n"
"	background-color: white;\n"
"	font-weight:bold;\n"
"}")
        self.home_page_button.setCheckable(True)
        self.home_page_button.setChecked(True)
        self.home_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_page_button)

        self.airfoil_page_button = QPushButton(self.sidebar_widget)
        self.airfoil_page_button.setObjectName(u"airfoil_page_button")
        self.airfoil_page_button.setMinimumSize(QSize(150, 0))
        self.airfoil_page_button.setMaximumSize(QSize(200, 16777215))
        self.airfoil_page_button.setStyleSheet(u"QPushButton:checked{\n"
"	color: rgb(35, 46, 47);\n"
"	background-color: white;\n"
"	font-weight:bold;\n"
"}")
        self.airfoil_page_button.setCheckable(True)
        self.airfoil_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.airfoil_page_button)

        self.station_page_button = QPushButton(self.sidebar_widget)
        self.station_page_button.setObjectName(u"station_page_button")
        self.station_page_button.setMinimumSize(QSize(150, 0))
        self.station_page_button.setMaximumSize(QSize(200, 16777215))
        self.station_page_button.setStyleSheet(u"QPushButton:checked{\n"
"	color: rgb(35, 46, 47);\n"
"	background-color: white;\n"
"	font-weight:bold;\n"
"}")
        self.station_page_button.setCheckable(True)
        self.station_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.station_page_button)

        self.blade_page_button = QPushButton(self.sidebar_widget)
        self.blade_page_button.setObjectName(u"blade_page_button")
        self.blade_page_button.setMinimumSize(QSize(150, 0))
        self.blade_page_button.setMaximumSize(QSize(200, 16777215))
        self.blade_page_button.setStyleSheet(u"QPushButton:checked{\n"
"	color: rgb(35, 46, 47);\n"
"	background-color: white;\n"
"	font-weight:bold;\n"
"}")
        self.blade_page_button.setCheckable(True)
        self.blade_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.blade_page_button)

        self.parts_button = QPushButton(self.sidebar_widget)
        self.parts_button.setObjectName(u"parts_button")
        self.parts_button.setStyleSheet(u"QPushButton:checked{\n"
"	color: rgb(35, 46, 47);\n"
"	background-color: white;\n"
"	font-weight:bold;\n"
"}")
        self.parts_button.setCheckable(False)
        self.parts_button.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.parts_button)

        self.skin_page_button = QPushButton(self.sidebar_widget)
        self.skin_page_button.setObjectName(u"skin_page_button")
        self.skin_page_button.setStyleSheet(u"QPushButton:checked{\n"
"	color: rgb(35, 46, 47);\n"
"	background-color: white;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding-left:25px;\n"
"}")
        self.skin_page_button.setCheckable(True)
        self.skin_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.skin_page_button)

        self.spar_page_button = QPushButton(self.sidebar_widget)
        self.spar_page_button.setObjectName(u"spar_page_button")
        self.spar_page_button.setStyleSheet(u"QPushButton:checked{\n"
"	color: rgb(35, 46, 47);\n"
"	background-color: white;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding-left:25px;\n"
"}")
        self.spar_page_button.setCheckable(True)
        self.spar_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.spar_page_button)

        self.abaqus_page_button = QPushButton(self.sidebar_widget)
        self.abaqus_page_button.setObjectName(u"abaqus_page_button")
        self.abaqus_page_button.setMinimumSize(QSize(150, 0))
        self.abaqus_page_button.setMaximumSize(QSize(200, 16777215))
        self.abaqus_page_button.setStyleSheet(u"QPushButton:checked{\n"
"	color: rgb(35, 46, 47);\n"
"	background-color: white;\n"
"	font-weight:bold;\n"
"}")
        self.abaqus_page_button.setCheckable(True)
        self.abaqus_page_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.abaqus_page_button)

        self.verticalSpacer_2 = QSpacerItem(150, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.settings_button = QPushButton(self.sidebar_widget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(150, 0))
        self.settings_button.setMaximumSize(QSize(200, 16777215))
        self.settings_button.setCheckable(True)
        self.settings_button.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.settings_button)

        self.info_button = QPushButton(self.sidebar_widget)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setMinimumSize(QSize(150, 0))
        self.info_button.setMaximumSize(QSize(200, 16777215))
        self.info_button.setCheckable(True)
        self.info_button.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.info_button)

        self.quit_button = QPushButton(self.sidebar_widget)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setMinimumSize(QSize(150, 0))
        self.quit_button.setMaximumSize(QSize(200, 16777215))
        self.quit_button.setCheckable(True)
        self.quit_button.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.quit_button)


        self.gridLayout.addWidget(self.sidebar_widget, 0, 0, 1, 1)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout_2 = QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.startbar_widget = QWidget(self.main_widget)
        self.startbar_widget.setObjectName(u"startbar_widget")
        self.startbar_widget.setMaximumSize(QSize(16777215, 50))
        self.startbar_widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.startbar_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 0, -1)
        self.page_title_label = QLabel(self.startbar_widget)
        self.page_title_label.setObjectName(u"page_title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_title_label.sizePolicy().hasHeightForWidth())
        self.page_title_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.page_title_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.page_title_label)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.startbar_widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.workpath_lineedit = QLineEdit(self.startbar_widget)
        self.workpath_lineedit.setObjectName(u"workpath_lineedit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.workpath_lineedit.sizePolicy().hasHeightForWidth())
        self.workpath_lineedit.setSizePolicy(sizePolicy2)
        self.workpath_lineedit.setStyleSheet(u"QLineEdit{\n"
"	color:black;\n"
"}")
        self.workpath_lineedit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.workpath_lineedit)

        self.changedir_button = QPushButton(self.startbar_widget)
        self.changedir_button.setObjectName(u"changedir_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.changedir_button.sizePolicy().hasHeightForWidth())
        self.changedir_button.setSizePolicy(sizePolicy3)
        self.changedir_button.setMinimumSize(QSize(70, 0))
        self.changedir_button.setMaximumSize(QSize(80, 22))
        self.changedir_button.setStyleSheet(u"QPushButton{\n"
"	background-color:white;\n"
"	color:black;\n"
"	border:none;\n"
"	height:30px;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgba(255,255,255,0.5);\n"
"}")
        self.changedir_button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.changedir_button)


        self.verticalLayout_2.addWidget(self.startbar_widget)

        self.display_widget = QWidget(self.main_widget)
        self.display_widget.setObjectName(u"display_widget")
        self.display_widget.setStyleSheet(u"QWidget{\n"
"	background-color:white;\n"
"	border-radius:5px;\n"
"	color:black;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align:center;\n"
"	padding:0px;\n"
"	border-radius:5px;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.display_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(self.display_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
        self.stackedWidget.setStyleSheet(u"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"QLabel{\n"
"	font: 700 12pt;\n"
"}\n"
"\n"
"QPushButton{\n"
"	font:700 10pt;\n"
"	background-color: #0B212E;\n"
"	border-radius:5px;\n"
"	color:white;\n"
"	padding:0.25em 3em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,0,0,0.2);\n"
"	color:rgb(35, 46, 47);\n"
"	font: 700;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.home_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.loadproject_button = QPushButton(self.home_page)
        self.loadproject_button.setObjectName(u"loadproject_button")
        self.loadproject_button.setMinimumSize(QSize(125, 0))

        self.gridLayout_5.addWidget(self.loadproject_button, 4, 1, 1, 1)

        self.newproject_button = QPushButton(self.home_page)
        self.newproject_button.setObjectName(u"newproject_button")
        self.newproject_button.setMinimumSize(QSize(125, 0))

        self.gridLayout_5.addWidget(self.newproject_button, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 5, 1, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 0, 1, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 4, 4, 1)

        self.label_6 = QLabel(self.home_page)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_6, 3, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 0, 4, 1)

        self.label_7 = QLabel(self.home_page)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 4, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 3, 2, 2, 1)

        self.label_5 = QLabel(self.home_page)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMaximumSize(QSize(500, 115))
        self.label_5.setSizeIncrement(QSize(16, 9))
        self.label_5.setTextFormat(Qt.TextFormat.AutoText)
        self.label_5.setPixmap(QPixmap(u":/resources/images/simbladed-dark.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_5, 2, 1, 1, 3)

        self.stackedWidget.addWidget(self.home_page)
        self.airfoil_page = QWidget()
        self.airfoil_page.setObjectName(u"airfoil_page")
        self.gridLayout_6 = QGridLayout(self.airfoil_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalWidget_2 = QWidget(self.airfoil_page)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setStyleSheet(u"QPushButton{\n"
"	font:700 10pt;\n"
"	background-color:#0B212E;\n"
"	border-radius:5px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,0,0,0.2);\n"
"	color:rgb(35, 46, 47);\n"
"	font: 700;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.airfoil_saveairfoil_button = QPushButton(self.horizontalWidget_2)
        self.airfoil_saveairfoil_button.setObjectName(u"airfoil_saveairfoil_button")
        sizePolicy2.setHeightForWidth(self.airfoil_saveairfoil_button.sizePolicy().hasHeightForWidth())
        self.airfoil_saveairfoil_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.airfoil_saveairfoil_button)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.airfoil_delairfoil_button = QPushButton(self.horizontalWidget_2)
        self.airfoil_delairfoil_button.setObjectName(u"airfoil_delairfoil_button")
        sizePolicy2.setHeightForWidth(self.airfoil_delairfoil_button.sizePolicy().hasHeightForWidth())
        self.airfoil_delairfoil_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.airfoil_delairfoil_button)


        self.gridLayout_6.addWidget(self.horizontalWidget_2, 2, 0, 1, 3)

        self.airfoil_parameters_widget = QWidget(self.airfoil_page)
        self.airfoil_parameters_widget.setObjectName(u"airfoil_parameters_widget")
        self.airfoil_parameters_widget.setStyleSheet(u"QWidget{\n"
"	background-color:#0B212E;\n"
"	color:white;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"	background-color:white;\n"
"	color: #0B212E;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color:white;\n"
"	color:#0B212E;\n"
"	border-radius:5px;\n"
"}")
        self.formLayout_2 = QFormLayout(self.airfoil_parameters_widget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(9)
        self.airfoil_uploadcoords_button = QPushButton(self.airfoil_parameters_widget)
        self.airfoil_uploadcoords_button.setObjectName(u"airfoil_uploadcoords_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.airfoil_uploadcoords_button.sizePolicy().hasHeightForWidth())
        self.airfoil_uploadcoords_button.setSizePolicy(sizePolicy5)
        self.airfoil_uploadcoords_button.setMinimumSize(QSize(125, 0))
        self.airfoil_uploadcoords_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.airfoil_uploadcoords_button.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgba(255,255,255,0.5);\n"
"	border-radius:5px;\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.airfoil_uploadcoords_button)

        self.airfoil_coord_name = QLineEdit(self.airfoil_parameters_widget)
        self.airfoil_coord_name.setObjectName(u"airfoil_coord_name")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.airfoil_coord_name.sizePolicy().hasHeightForWidth())
        self.airfoil_coord_name.setSizePolicy(sizePolicy6)
        self.airfoil_coord_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.airfoil_coord_name.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.airfoil_coord_name)

        self.label_9 = QLabel(self.airfoil_parameters_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(125, 0))
        self.label_9.setMaximumSize(QSize(150, 16777215))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.airfoil_parameters_widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(125, 0))
        self.label_10.setMaximumSize(QSize(150, 16777215))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.airfoil_parameters_widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(125, 0))
        self.label_11.setMaximumSize(QSize(150, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.airfoil_parameters_widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(125, 0))
        self.label_12.setMaximumSize(QSize(150, 16777215))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.label_13 = QLabel(self.airfoil_parameters_widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(125, 0))
        self.label_13.setMaximumSize(QSize(150, 16777215))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_13)

        self.airfoil_firstdigit_input = QSpinBox(self.airfoil_parameters_widget)
        self.airfoil_firstdigit_input.setObjectName(u"airfoil_firstdigit_input")
        self.airfoil_firstdigit_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.airfoil_firstdigit_input.setMinimum(5)
        self.airfoil_firstdigit_input.setMaximum(6)
        self.airfoil_firstdigit_input.setValue(6)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.airfoil_firstdigit_input)

        self.airfoil_seconddigit_input = QSpinBox(self.airfoil_parameters_widget)
        self.airfoil_seconddigit_input.setObjectName(u"airfoil_seconddigit_input")
        self.airfoil_seconddigit_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.airfoil_seconddigit_input.setValue(3)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.airfoil_seconddigit_input)

        self.airfoil_thirddigit_input = QSpinBox(self.airfoil_parameters_widget)
        self.airfoil_thirddigit_input.setObjectName(u"airfoil_thirddigit_input")
        self.airfoil_thirddigit_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.airfoil_thirddigit_input.setValue(4)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.airfoil_thirddigit_input)

        self.airfoil_lasttwodigits_input = QSpinBox(self.airfoil_parameters_widget)
        self.airfoil_lasttwodigits_input.setObjectName(u"airfoil_lasttwodigits_input")
        self.airfoil_lasttwodigits_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.airfoil_lasttwodigits_input.setValue(30)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.airfoil_lasttwodigits_input)

        self.airfoil_npoints_input = QSpinBox(self.airfoil_parameters_widget)
        self.airfoil_npoints_input.setObjectName(u"airfoil_npoints_input")
        self.airfoil_npoints_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.airfoil_npoints_input.setMinimum(50)
        self.airfoil_npoints_input.setMaximum(200)
        self.airfoil_npoints_input.setValue(100)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.airfoil_npoints_input)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.formLayout_2.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer_5)


        self.gridLayout_6.addWidget(self.airfoil_parameters_widget, 1, 0, 1, 3)

        self.airfoil_graph_widget = QWidget(self.airfoil_page)
        self.airfoil_graph_widget.setObjectName(u"airfoil_graph_widget")
        self.airfoil_graph_widget.setMinimumSize(QSize(800, 0))
        self.airfoil_graph_widget.setStyleSheet(u"QWidget{\n"
"	background-color:#0B212E;\n"
"	color:white;\n"
"	border-radius:10px;\n"
"}")
        self.gridLayout_12 = QGridLayout(self.airfoil_graph_widget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(20, 20, 20, 20)
        self.airfoil_resetzoom_button = QPushButton(self.airfoil_graph_widget)
        self.airfoil_resetzoom_button.setObjectName(u"airfoil_resetzoom_button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.airfoil_resetzoom_button.sizePolicy().hasHeightForWidth())
        self.airfoil_resetzoom_button.setSizePolicy(sizePolicy7)

        self.gridLayout_12.addWidget(self.airfoil_resetzoom_button, 0, 2, 1, 1)

        self.airfoil_xy_current = QLabel(self.airfoil_graph_widget)
        self.airfoil_xy_current.setObjectName(u"airfoil_xy_current")
        sizePolicy.setHeightForWidth(self.airfoil_xy_current.sizePolicy().hasHeightForWidth())
        self.airfoil_xy_current.setSizePolicy(sizePolicy)
        self.airfoil_xy_current.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_12.addWidget(self.airfoil_xy_current, 0, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_21, 0, 0, 1, 1)

        self.airfoil_chartview = QChartView(self.airfoil_graph_widget)
        self.airfoil_chartview.setObjectName(u"airfoil_chartview")
        self.airfoil_chartview.viewport().setProperty("cursor", QCursor(Qt.CursorShape.CrossCursor))
        self.airfoil_chartview.setMouseTracking(True)
        self.airfoil_chartview.setStyleSheet(u"QGraphicsView{\n"
"	background-color:white;\n"
"}")
        self.airfoil_chartview.setRenderHints(QPainter.RenderHint.Antialiasing|QPainter.RenderHint.LosslessImageRendering|QPainter.RenderHint.NonCosmeticBrushPatterns|QPainter.RenderHint.SmoothPixmapTransform|QPainter.RenderHint.TextAntialiasing|QPainter.RenderHint.VerticalSubpixelPositioning)

        self.gridLayout_12.addWidget(self.airfoil_chartview, 1, 0, 1, 3)


        self.gridLayout_6.addWidget(self.airfoil_graph_widget, 0, 3, 5, 1)

        self.label_14 = QLabel(self.airfoil_page)
        self.label_14.setObjectName(u"label_14")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"QLabel{\n"
"	font:700 12pt;\n"
"	background-color: #0B212E;\n"
"	border-radius:10px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_14, 3, 0, 1, 3)

        self.airfoil_listairfoils_widget = QListView(self.airfoil_page)
        self.airfoil_listairfoils_widget.setObjectName(u"airfoil_listairfoils_widget")
        self.airfoil_listairfoils_widget.setStyleSheet(u"QListWidget{\n"
"	border-color:yellow;\n"
"	background-color:rgb(35, 46, 47);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}")

        self.gridLayout_6.addWidget(self.airfoil_listairfoils_widget, 4, 0, 1, 3)

        self.label_8 = QLabel(self.airfoil_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	font:700 12pt;\n"
"	background-color: #0B212E;\n"
"	border-radius:10px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.airfoil_page)
        self.station_page = QWidget()
        self.station_page.setObjectName(u"station_page")
        self.station_page.setStyleSheet(u"QPushButton{\n"
"	font:700 10pt;\n"
"	background-color:#0B212E;\n"
"	border-radius:5px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,0,0,0.2);\n"
"	color:rgb(35, 46, 47);\n"
"	font: 700;\n"
"}")
        self.gridLayout_8 = QGridLayout(self.station_page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.station_tab_widget = QTabWidget(self.station_page)
        self.station_tab_widget.setObjectName(u"station_tab_widget")
        self.station_tab1 = QWidget()
        self.station_tab1.setObjectName(u"station_tab1")
        self.gridLayout_16 = QGridLayout(self.station_tab1)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.station_tab1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel{\n"
"	font: 700 14pt;\n"
"}")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_15, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.station_tab1)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QWidget{\n"
"	background-color:#0B212E;\n"
"	color:white;\n"
"}")
        self.formLayout_3 = QFormLayout(self.widget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.station_uploadairfoil_button = QPushButton(self.widget_3)
        self.station_uploadairfoil_button.setObjectName(u"station_uploadairfoil_button")
        self.station_uploadairfoil_button.setStyleSheet(u"QPushButton{\n"
"	background-color:white;\n"
"	color:rgb(35, 46, 47);\n"
"	border-radius:5px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.station_uploadairfoil_button)

        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.station_listairfoils_box = QComboBox(self.widget_3)
        self.station_listairfoils_box.setObjectName(u"station_listairfoils_box")
        self.station_listairfoils_box.setStyleSheet(u"QComboBox{\n"
"	background-color:white;\n"
"	color:rgb(35, 46, 47);\n"
"	border-radius:5px;\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.station_listairfoils_box)


        self.gridLayout_16.addWidget(self.widget_3, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 55, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_16.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.label_18 = QLabel(self.station_tab1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"QLabel{\n"
"	font: 700 14pt;\n"
"}")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_18, 3, 0, 1, 1)

        self.widget_4 = QWidget(self.station_tab1)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget{\n"
"	background-color:#0B212E;\n"
"	color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color:white;\n"
"	color:rgb(35, 46, 47);\n"
"	padding-left:0.5em;\n"
"}")
        self.gridLayout_9 = QGridLayout(self.widget_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_22 = QLabel(self.widget_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(100, 0))
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_22, 3, 0, 1, 1)

        self.station_mirrory_input = QCheckBox(self.widget_4)
        self.station_mirrory_input.setObjectName(u"station_mirrory_input")
        self.station_mirrory_input.setChecked(True)

        self.gridLayout_9.addWidget(self.station_mirrory_input, 9, 2, 1, 1)

        self.label_24 = QLabel(self.widget_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(100, 0))
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_24, 5, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_17, 8, 1, 1, 1)

        self.label_25 = QLabel(self.widget_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(100, 0))
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_25, 6, 0, 1, 1)

        self.label_21 = QLabel(self.widget_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(100, 0))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_21, 2, 0, 1, 1)

        self.label_20 = QLabel(self.widget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(100, 0))
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_23 = QLabel(self.widget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(100, 0))
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_23, 4, 0, 1, 1)

        self.station_mirrorx_input = QCheckBox(self.widget_4)
        self.station_mirrorx_input.setObjectName(u"station_mirrorx_input")

        self.gridLayout_9.addWidget(self.station_mirrorx_input, 8, 2, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_16, 9, 1, 1, 1)

        self.label_28 = QLabel(self.widget_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(100, 0))
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_28, 9, 0, 1, 1)

        self.label_27 = QLabel(self.widget_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(100, 0))
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_27, 8, 0, 1, 1)

        self.label_26 = QLabel(self.widget_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(100, 0))
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_26, 7, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_18, 8, 3, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_19, 9, 3, 1, 1)

        self.station_multz_input = QLineEdit(self.widget_4)
        self.station_multz_input.setObjectName(u"station_multz_input")

        self.gridLayout_9.addWidget(self.station_multz_input, 7, 1, 1, 3)

        self.station_multy_input = QLineEdit(self.widget_4)
        self.station_multy_input.setObjectName(u"station_multy_input")

        self.gridLayout_9.addWidget(self.station_multy_input, 6, 1, 1, 3)

        self.station_multx_input = QLineEdit(self.widget_4)
        self.station_multx_input.setObjectName(u"station_multx_input")

        self.gridLayout_9.addWidget(self.station_multx_input, 5, 1, 1, 3)

        self.station_offsetz_input = QLineEdit(self.widget_4)
        self.station_offsetz_input.setObjectName(u"station_offsetz_input")

        self.gridLayout_9.addWidget(self.station_offsetz_input, 4, 1, 1, 3)

        self.station_offsety_input = QLineEdit(self.widget_4)
        self.station_offsety_input.setObjectName(u"station_offsety_input")

        self.gridLayout_9.addWidget(self.station_offsety_input, 3, 1, 1, 3)

        self.station_offsetx_input = QLineEdit(self.widget_4)
        self.station_offsetx_input.setObjectName(u"station_offsetx_input")

        self.gridLayout_9.addWidget(self.station_offsetx_input, 2, 1, 1, 3)

        self.station_twistangle_input = QLineEdit(self.widget_4)
        self.station_twistangle_input.setObjectName(u"station_twistangle_input")

        self.gridLayout_9.addWidget(self.station_twistangle_input, 1, 1, 1, 3)

        self.station_chordlength_input = QLineEdit(self.widget_4)
        self.station_chordlength_input.setObjectName(u"station_chordlength_input")

        self.gridLayout_9.addWidget(self.station_chordlength_input, 0, 1, 1, 3)

        self.label_19 = QLabel(self.widget_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(100, 0))
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_19, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_4, 4, 0, 1, 1)

        self.widget_5 = QWidget(self.station_tab1)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy4.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy4)
        self.widget_5.setStyleSheet(u"QPushButton{\n"
"	font:700 10pt;\n"
"	background-color: #0B212E;\n"
"	border-radius:5px;\n"
"	color:white;\n"
"	padding:0.25em 0.5em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,0,0,0.2);\n"
"	color:#0B212E;\n"
"	font: 700;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.station_savestation_button = QPushButton(self.widget_5)
        self.station_savestation_button.setObjectName(u"station_savestation_button")
        sizePolicy2.setHeightForWidth(self.station_savestation_button.sizePolicy().hasHeightForWidth())
        self.station_savestation_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.station_savestation_button)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.station_delstation_button = QPushButton(self.widget_5)
        self.station_delstation_button.setObjectName(u"station_delstation_button")
        sizePolicy2.setHeightForWidth(self.station_delstation_button.sizePolicy().hasHeightForWidth())
        self.station_delstation_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.station_delstation_button)


        self.gridLayout_16.addWidget(self.widget_5, 5, 0, 1, 2)

        self.widget = QWidget(self.station_tab1)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.sta_list_widget = QWidget(self.widget)
        self.sta_list_widget.setObjectName(u"sta_list_widget")
        self.sta_list_widget.setMinimumSize(QSize(50, 0))
        self.sta_list_widget.setMaximumSize(QSize(16777215, 50))
        self.sta_list_widget.setStyleSheet(u"QWidget{\n"
"	background-color:#0B212E;\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color:white;\n"
"	border-radius:5px;\n"
"	color:#0B212E;\n"
"	padding-left:0.5em;\n"
"}")
        self.formLayout = QFormLayout(self.sta_list_widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label_35 = QLabel(self.sta_list_widget)
        self.label_35.setObjectName(u"label_35")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_35)

        self.station_liststation_box = QComboBox(self.sta_list_widget)
        self.station_liststation_box.setObjectName(u"station_liststation_box")
        sizePolicy2.setHeightForWidth(self.station_liststation_box.sizePolicy().hasHeightForWidth())
        self.station_liststation_box.setSizePolicy(sizePolicy2)
        self.station_liststation_box.setMinimumSize(QSize(100, 0))
        self.station_liststation_box.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.station_liststation_box)


        self.horizontalLayout_6.addWidget(self.sta_list_widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_20)


        self.gridLayout_16.addWidget(self.widget, 5, 2, 1, 1)

        self.station_graph_widget = QWidget(self.station_tab1)
        self.station_graph_widget.setObjectName(u"station_graph_widget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.station_graph_widget.sizePolicy().hasHeightForWidth())
        self.station_graph_widget.setSizePolicy(sizePolicy8)
        self.station_graph_widget.setMinimumSize(QSize(800, 0))
        self.station_graph_widget.setStyleSheet(u"QWidget{\n"
"	background-color:#0B212E;\n"
"	color:white;\n"
"	border-radius:10px;\n"
"}")
        self.gridLayout_13 = QGridLayout(self.station_graph_widget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.station_resetzoom_button = QPushButton(self.station_graph_widget)
        self.station_resetzoom_button.setObjectName(u"station_resetzoom_button")
        sizePolicy7.setHeightForWidth(self.station_resetzoom_button.sizePolicy().hasHeightForWidth())
        self.station_resetzoom_button.setSizePolicy(sizePolicy7)

        self.gridLayout_13.addWidget(self.station_resetzoom_button, 0, 2, 1, 1)

        self.station_xy_current = QLabel(self.station_graph_widget)
        self.station_xy_current.setObjectName(u"station_xy_current")

        self.gridLayout_13.addWidget(self.station_xy_current, 0, 1, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_26, 0, 0, 1, 1)

        self.station_chartview = QChartView(self.station_graph_widget)
        self.station_chartview.setObjectName(u"station_chartview")
        self.station_chartview.viewport().setProperty("cursor", QCursor(Qt.CursorShape.CrossCursor))
        self.station_chartview.setStyleSheet(u"QGraphicsView{\n"
"	background-color:white;\n"
"}")
        self.station_chartview.setRenderHints(QPainter.RenderHint.Antialiasing|QPainter.RenderHint.LosslessImageRendering|QPainter.RenderHint.NonCosmeticBrushPatterns|QPainter.RenderHint.SmoothPixmapTransform|QPainter.RenderHint.TextAntialiasing|QPainter.RenderHint.VerticalSubpixelPositioning)

        self.gridLayout_13.addWidget(self.station_chartview, 1, 0, 1, 3)


        self.gridLayout_16.addWidget(self.station_graph_widget, 0, 1, 5, 2)

        self.station_tab_widget.addTab(self.station_tab1, "")
        self.station_tab2 = QWidget()
        self.station_tab2.setObjectName(u"station_tab2")
        self.station_tab2.setStyleSheet(u"QSpinBox{\n"
"	border: 2px solid #0B212E;\n"
"	padding-top: 0.2em;\n"
"	padding-bottom: 0.2em;\n"
"	padding-left:0.5rem;\n"
"	border-radius:5px;\n"
"}")
        self.gridLayout_17 = QGridLayout(self.station_tab2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.station_tab2)
        self.label_44.setObjectName(u"label_44")
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)

        self.gridLayout_17.addWidget(self.label_44, 0, 0, 1, 1)

        self.station_saveTable_button = QPushButton(self.station_tab2)
        self.station_saveTable_button.setObjectName(u"station_saveTable_button")

        self.gridLayout_17.addWidget(self.station_saveTable_button, 2, 1, 1, 1)

        self.station_sortTable_button = QPushButton(self.station_tab2)
        self.station_sortTable_button.setObjectName(u"station_sortTable_button")

        self.gridLayout_17.addWidget(self.station_sortTable_button, 2, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_12, 0, 2, 1, 1)

        self.station_nStationsAdv_input = QSpinBox(self.station_tab2)
        self.station_nStationsAdv_input.setObjectName(u"station_nStationsAdv_input")
        self.station_nStationsAdv_input.setMouseTracking(False)
        self.station_nStationsAdv_input.setProperty("showGroupSeparator", False)
        self.station_nStationsAdv_input.setMinimum(1)

        self.gridLayout_17.addWidget(self.station_nStationsAdv_input, 0, 1, 1, 1)

        self.station_tableStations_input = QTableWidget(self.station_tab2)
        if (self.station_tableStations_input.columnCount() < 11):
            self.station_tableStations_input.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.station_tableStations_input.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.station_tableStations_input.rowCount() < 1):
            self.station_tableStations_input.setRowCount(1)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.station_tableStations_input.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.station_tableStations_input.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.station_tableStations_input.setItem(0, 5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.station_tableStations_input.setItem(0, 6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.station_tableStations_input.setItem(0, 7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.station_tableStations_input.setItem(0, 8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.station_tableStations_input.setItem(0, 9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.station_tableStations_input.setItem(0, 10, __qtablewidgetitem18)
        self.station_tableStations_input.setObjectName(u"station_tableStations_input")
        font2 = QFont()
        font2.setBold(False)
        self.station_tableStations_input.setFont(font2)
        self.station_tableStations_input.setStyleSheet(u"QTableWidget{\n"
"	border: 3px solid #0B212E;\n"
"	border-radius:10px;\n"
"}")
        self.station_tableStations_input.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.station_tableStations_input.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)
        self.station_tableStations_input.setAlternatingRowColors(True)
        self.station_tableStations_input.setGridStyle(Qt.PenStyle.SolidLine)
        self.station_tableStations_input.setSortingEnabled(True)
        self.station_tableStations_input.setWordWrap(True)
        self.station_tableStations_input.setRowCount(1)
        self.station_tableStations_input.horizontalHeader().setCascadingSectionResizes(False)
        self.station_tableStations_input.horizontalHeader().setMinimumSectionSize(40)
        self.station_tableStations_input.horizontalHeader().setDefaultSectionSize(90)
        self.station_tableStations_input.horizontalHeader().setProperty("showSortIndicator", True)

        self.gridLayout_17.addWidget(self.station_tableStations_input, 1, 0, 1, 3)

        self.station_tab_widget.addTab(self.station_tab2, "")

        self.gridLayout_8.addWidget(self.station_tab_widget, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.station_page)
        self.blade_page = QWidget()
        self.blade_page.setObjectName(u"blade_page")
        self.blade_page.setStyleSheet(u"QPushButton{\n"
"	font:700 10pt;\n"
"	background-color: #0B212E;\n"
"	border-radius:5px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,0,0,0.2);\n"
"	color: #0B212E;\n"
"	font: 700;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.blade_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_7 = QWidget(self.blade_page)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(35, 46, 47);\n"
"	border-radius:10px;\n"
"	color:white;\n"
"}\n"
"\n"
"QGraphicsView{\n"
"	background-color: white;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.blade_olpsta_chartview = QChartView(self.widget_7)
        self.blade_olpsta_chartview.setObjectName(u"blade_olpsta_chartview")
        self.blade_olpsta_chartview.setRenderHints(QPainter.RenderHint.Antialiasing|QPainter.RenderHint.LosslessImageRendering|QPainter.RenderHint.NonCosmeticBrushPatterns|QPainter.RenderHint.SmoothPixmapTransform|QPainter.RenderHint.TextAntialiasing|QPainter.RenderHint.VerticalSubpixelPositioning)

        self.verticalLayout_3.addWidget(self.blade_olpsta_chartview)

        self.blade_olplen_chartview = QChartView(self.widget_7)
        self.blade_olplen_chartview.setObjectName(u"blade_olplen_chartview")
        self.blade_olplen_chartview.setRenderHints(QPainter.RenderHint.Antialiasing|QPainter.RenderHint.LosslessImageRendering|QPainter.RenderHint.NonCosmeticBrushPatterns|QPainter.RenderHint.SmoothPixmapTransform|QPainter.RenderHint.TextAntialiasing|QPainter.RenderHint.VerticalSubpixelPositioning)

        self.verticalLayout_3.addWidget(self.blade_olplen_chartview)


        self.gridLayout_2.addWidget(self.widget_7, 0, 2, 2, 1)

        self.widget_9 = QWidget(self.blade_page)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_6 = QVBoxLayout(self.widget_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_9)

        self.blade_interpolate_button = QPushButton(self.widget_9)
        self.blade_interpolate_button.setObjectName(u"blade_interpolate_button")
        sizePolicy5.setHeightForWidth(self.blade_interpolate_button.sizePolicy().hasHeightForWidth())
        self.blade_interpolate_button.setSizePolicy(sizePolicy5)
        self.blade_interpolate_button.setStyleSheet(u"")
        self.blade_interpolate_button.setCheckable(False)

        self.verticalLayout_6.addWidget(self.blade_interpolate_button)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)


        self.gridLayout_2.addWidget(self.widget_9, 0, 1, 1, 1)

        self.widget_6 = QWidget(self.blade_page)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMaximumSize(QSize(233, 16777215))
        self.widget_6.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_37 = QLabel(self.widget_6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"QLabel{\n"
"	font:700 12pt;\n"
"	background-color: #0B212E;\n"
"	border-radius:10px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}")

        self.verticalLayout_5.addWidget(self.label_37)

        self.blade_skinolplen_table = QTableWidget(self.widget_6)
        if (self.blade_skinolplen_table.columnCount() < 2):
            self.blade_skinolplen_table.setColumnCount(2)
        font3 = QFont()
        font3.setBold(True)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font3);
        self.blade_skinolplen_table.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font3);
        self.blade_skinolplen_table.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        if (self.blade_skinolplen_table.rowCount() < 2):
            self.blade_skinolplen_table.setRowCount(2)
        self.blade_skinolplen_table.setObjectName(u"blade_skinolplen_table")
        self.blade_skinolplen_table.setStyleSheet(u"")
        self.blade_skinolplen_table.setAlternatingRowColors(True)
        self.blade_skinolplen_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.blade_skinolplen_table.setRowCount(2)
        self.blade_skinolplen_table.setColumnCount(2)

        self.verticalLayout_5.addWidget(self.blade_skinolplen_table)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_15)


        self.gridLayout_2.addWidget(self.widget_6, 1, 0, 1, 1)

        self.widget_10 = QWidget(self.blade_page)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.widget_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)

        self.label_41 = QLabel(self.widget_10)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_7.addWidget(self.label_41)

        self.blade_order_input = QSpinBox(self.widget_10)
        self.blade_order_input.setObjectName(u"blade_order_input")
        self.blade_order_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.blade_order_input.setMinimum(1)
        self.blade_order_input.setMaximum(5)
        self.blade_order_input.setValue(1)

        self.verticalLayout_7.addWidget(self.blade_order_input)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_16)

        self.label_40 = QLabel(self.widget_10)
        self.label_40.setObjectName(u"label_40")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_40.setFont(font4)
        self.label_40.setStyleSheet(u"QLabel{\n"
"	font:700 10pt;\n"
"	background-color:#0B212E;\n"
"	border-radius:10px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}")

        self.verticalLayout_7.addWidget(self.label_40)

        self.label_38 = QLabel(self.widget_10)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_7.addWidget(self.label_38)

        self.blade_skinolpsta_selected = QComboBox(self.widget_10)
        self.blade_skinolpsta_selected.setObjectName(u"blade_skinolpsta_selected")
        self.blade_skinolpsta_selected.setEditable(False)

        self.verticalLayout_7.addWidget(self.blade_skinolpsta_selected)

        self.label_39 = QLabel(self.widget_10)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_7.addWidget(self.label_39)

        self.blade_skinolplen_selected = QComboBox(self.widget_10)
        self.blade_skinolplen_selected.setObjectName(u"blade_skinolplen_selected")
        self.blade_skinolplen_selected.setEditable(False)

        self.verticalLayout_7.addWidget(self.blade_skinolplen_selected)

        self.blade_saveparams_button = QPushButton(self.widget_10)
        self.blade_saveparams_button.setObjectName(u"blade_saveparams_button")

        self.verticalLayout_7.addWidget(self.blade_saveparams_button)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_12)


        self.gridLayout_2.addWidget(self.widget_10, 1, 1, 1, 1)

        self.widget_2 = QWidget(self.blade_page)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QSize(233, 16777215))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"	font:700 12pt;\n"
"	background-color: #0B212E;\n"
"	border-radius:10px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_3)

        self.blade_skinolpsta_table = QTableWidget(self.widget_2)
        if (self.blade_skinolpsta_table.columnCount() < 2):
            self.blade_skinolpsta_table.setColumnCount(2)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font3);
        self.blade_skinolpsta_table.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font3);
        self.blade_skinolpsta_table.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        if (self.blade_skinolpsta_table.rowCount() < 2):
            self.blade_skinolpsta_table.setRowCount(2)
        self.blade_skinolpsta_table.setObjectName(u"blade_skinolpsta_table")
        self.blade_skinolpsta_table.setStyleSheet(u"")
        self.blade_skinolpsta_table.setAlternatingRowColors(True)
        self.blade_skinolpsta_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.blade_skinolpsta_table.setRowCount(2)
        self.blade_skinolpsta_table.setColumnCount(2)

        self.verticalLayout_4.addWidget(self.blade_skinolpsta_table)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_14)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.blade_page)
        self.skin_page = QWidget()
        self.skin_page.setObjectName(u"skin_page")
        self.skin_page.setStyleSheet(u"")
        self.gridLayout_10 = QGridLayout(self.skin_page)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_7, 3, 0, 1, 1)

        self.skin_zoomedgraph_widget = QWidget(self.skin_page)
        self.skin_zoomedgraph_widget.setObjectName(u"skin_zoomedgraph_widget")
        self.skin_zoomedgraph_widget.setMinimumSize(QSize(600, 0))
        self.skin_zoomedgraph_widget.setStyleSheet(u"QWidget{\n"
"	background-color:#0B212E;\n"
"	border-radius:10px;\n"
"}")
        self.gridLayout_15 = QGridLayout(self.skin_zoomedgraph_widget)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.skin_zoom_chartview = QChartView(self.skin_zoomedgraph_widget)
        self.skin_zoom_chartview.setObjectName(u"skin_zoom_chartview")
        self.skin_zoom_chartview.viewport().setProperty("cursor", QCursor(Qt.CursorShape.CrossCursor))
        self.skin_zoom_chartview.setStyleSheet(u"QGraphicsView{\n"
"	background-color:white;\n"
"}")
        self.skin_zoom_chartview.setRenderHints(QPainter.RenderHint.Antialiasing|QPainter.RenderHint.LosslessImageRendering|QPainter.RenderHint.NonCosmeticBrushPatterns|QPainter.RenderHint.SmoothPixmapTransform|QPainter.RenderHint.TextAntialiasing|QPainter.RenderHint.VerticalSubpixelPositioning)

        self.gridLayout_15.addWidget(self.skin_zoom_chartview, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.skin_zoomedgraph_widget, 0, 1, 2, 1)

        self.skin_maingraph_widget = QWidget(self.skin_page)
        self.skin_maingraph_widget.setObjectName(u"skin_maingraph_widget")
        self.skin_maingraph_widget.setMinimumSize(QSize(600, 0))
        self.skin_maingraph_widget.setStyleSheet(u"QWidget{\n"
"	background-color:#0B212E;\n"
"	border-radius:10px;\n"
"}")
        self.gridLayout_7 = QGridLayout(self.skin_maingraph_widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.skin_full_chartview = QChartView(self.skin_maingraph_widget)
        self.skin_full_chartview.setObjectName(u"skin_full_chartview")
        self.skin_full_chartview.viewport().setProperty("cursor", QCursor(Qt.CursorShape.CrossCursor))
        self.skin_full_chartview.setStyleSheet(u"QGraphicsView{\n"
"	background-color:white;\n"
"}")
        self.skin_full_chartview.setRenderHints(QPainter.RenderHint.Antialiasing|QPainter.RenderHint.LosslessImageRendering|QPainter.RenderHint.NonCosmeticBrushPatterns|QPainter.RenderHint.SmoothPixmapTransform|QPainter.RenderHint.TextAntialiasing|QPainter.RenderHint.VerticalSubpixelPositioning)

        self.gridLayout_7.addWidget(self.skin_full_chartview, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.skin_maingraph_widget, 2, 1, 2, 1)

        self.label_29 = QLabel(self.skin_page)
        self.label_29.setObjectName(u"label_29")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_29.setFont(font5)
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_29, 0, 0, 1, 1)

        self.widget_8 = QWidget(self.skin_page)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"QWidget{\n"
"	background-color:#0B212E;\n"
"	color:white;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color:white;\n"
"	color: #0B212E;\n"
"	border-radius:5px;\n"
"	padding-left:5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:white;\n"
"	color:#0B212E;\n"
"	padding: 0em 1.5em;\n"
"	border:none;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgba(255,255,255,0.5);\n"
"}\n"
"\n"
"QCheckBox{\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color:white;\n"
"	color:#0B212E;\n"
"	border-radius:5px;\n"
"}")
        self.gridLayout_11 = QGridLayout(self.widget_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_22, 5, 3, 1, 2)

        self.label_36 = QLabel(self.widget_8)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_36, 5, 0, 1, 2)

        self.label_32 = QLabel(self.widget_8)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_32, 2, 0, 1, 2)

        self.label_34 = QLabel(self.widget_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_34, 4, 0, 1, 2)

        self.skin_nplies_input = QLineEdit(self.widget_8)
        self.skin_nplies_input.setObjectName(u"skin_nplies_input")

        self.gridLayout_11.addWidget(self.skin_nplies_input, 1, 2, 1, 3)

        self.skin_plythickness_input = QLineEdit(self.widget_8)
        self.skin_plythickness_input.setObjectName(u"skin_plythickness_input")

        self.gridLayout_11.addWidget(self.skin_plythickness_input, 2, 2, 1, 3)

        self.skin_savefig_input = QCheckBox(self.widget_8)
        self.skin_savefig_input.setObjectName(u"skin_savefig_input")
        sizePolicy5.setHeightForWidth(self.skin_savefig_input.sizePolicy().hasHeightForWidth())
        self.skin_savefig_input.setSizePolicy(sizePolicy5)
        self.skin_savefig_input.setMinimumSize(QSize(0, 0))
        self.skin_savefig_input.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_11.addWidget(self.skin_savefig_input, 5, 2, 1, 1)

        self.skin_liststations = QComboBox(self.widget_8)
        self.skin_liststations.setObjectName(u"skin_liststations")

        self.gridLayout_11.addWidget(self.skin_liststations, 0, 2, 1, 3)

        self.skin_tethickness_input = QLineEdit(self.widget_8)
        self.skin_tethickness_input.setObjectName(u"skin_tethickness_input")

        self.gridLayout_11.addWidget(self.skin_tethickness_input, 4, 2, 1, 3)

        self.label_31 = QLabel(self.widget_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_31, 1, 0, 1, 2)

        self.label_33 = QLabel(self.widget_8)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_33, 3, 0, 1, 2)

        self.label_30 = QLabel(self.widget_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_30, 0, 0, 1, 2)

        self.skin_overlaptarget_input = QLineEdit(self.widget_8)
        self.skin_overlaptarget_input.setObjectName(u"skin_overlaptarget_input")
        self.skin_overlaptarget_input.setReadOnly(True)

        self.gridLayout_11.addWidget(self.skin_overlaptarget_input, 3, 2, 1, 3)


        self.gridLayout_10.addWidget(self.widget_8, 1, 0, 1, 1)

        self.widget_11 = QWidget(self.skin_page)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"QPushButton{\n"
"	font:700 10pt;\n"
"	background-color: #0B212E;\n"
"	border-radius:5px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,0,0,0.2);\n"
"	color: #0B212E;\n"
"	font: 700;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.skin_saveSection_button = QPushButton(self.widget_11)
        self.skin_saveSection_button.setObjectName(u"skin_saveSection_button")

        self.horizontalLayout_3.addWidget(self.skin_saveSection_button)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.skin_delSection_button = QPushButton(self.widget_11)
        self.skin_delSection_button.setObjectName(u"skin_delSection_button")

        self.horizontalLayout_3.addWidget(self.skin_delSection_button)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)


        self.gridLayout_10.addWidget(self.widget_11, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.skin_page)
        self.spar_page = QWidget()
        self.spar_page.setObjectName(u"spar_page")
        self.gridLayout_14 = QGridLayout(self.spar_page)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_43 = QLabel(self.spar_page)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_14.addWidget(self.label_43, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.spar_page)
        self.abaqus_page = QWidget()
        self.abaqus_page.setObjectName(u"abaqus_page")
        self.gridLayout_3 = QGridLayout(self.abaqus_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(15)
        self.abaqus_expFileName_input = QLineEdit(self.abaqus_page)
        self.abaqus_expFileName_input.setObjectName(u"abaqus_expFileName_input")
        self.abaqus_expFileName_input.setMaximumSize(QSize(200, 16777215))
        self.abaqus_expFileName_input.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid #0B212E;\n"
"	padding-top: 0.1em;\n"
"	padding-bottom: 0.1em;\n"
"	padding-left:0.5em;\n"
"	border-radius:5px;\n"
"}")

        self.gridLayout_3.addWidget(self.abaqus_expFileName_input, 3, 1, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_27, 0, 4, 4, 1)

        self.label_46 = QLabel(self.abaqus_page)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_3.addWidget(self.label_46, 3, 0, 1, 1)

        self.label_47 = QLabel(self.abaqus_page)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_3.addWidget(self.label_47, 3, 2, 1, 1)

        self.abaqus_export_button = QPushButton(self.abaqus_page)
        self.abaqus_export_button.setObjectName(u"abaqus_export_button")
        self.abaqus_export_button.setStyleSheet(u"QPushButton{\n"
"	font:700 10pt;\n"
"	background-color: #0B212E;\n"
"	border-radius:5px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,0,0,0.2);\n"
"	color: #0B212E;\n"
"	font: 700;\n"
"}")

        self.gridLayout_3.addWidget(self.abaqus_export_button, 3, 3, 1, 1)

        self.label_42 = QLabel(self.abaqus_page)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"QLabel{\n"
"	font:700 12pt;\n"
"	background-color: #0B212E;\n"
"	border-radius:10px;\n"
"	color:white;\n"
"	padding:0.25em 1em;\n"
"}")

        self.gridLayout_3.addWidget(self.label_42, 0, 0, 1, 3)

        self.abaqus_sectionsList = QListWidget(self.abaqus_page)
        self.abaqus_sectionsList.setObjectName(u"abaqus_sectionsList")
        self.abaqus_sectionsList.setStyleSheet(u"QListWidget{\n"
"	border: 2px solid #0B212E;\n"
"	padding-top:1em;\n"
"	padding-bottom: 1em;\n"
"	padding-left:1em;\n"
"	border-radius:10px;\n"
"}")
        self.abaqus_sectionsList.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed|QAbstractItemView.EditTrigger.SelectedClicked)
        self.abaqus_sectionsList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.gridLayout_3.addWidget(self.abaqus_sectionsList, 2, 0, 1, 4)

        self.label_45 = QLabel(self.abaqus_page)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_3.addWidget(self.label_45, 1, 0, 1, 4)

        self.stackedWidget.addWidget(self.abaqus_page)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.display_widget)

        self.statusbar_widget = QWidget(self.main_widget)
        self.statusbar_widget.setObjectName(u"statusbar_widget")
        self.statusbar_widget.setMinimumSize(QSize(0, 20))
        self.statusbar_widget.setStyleSheet(u"QWidget{\n"
"	background-color:gray;\n"
"	border-radius:5px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.statusbar_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 0, 0)
        self.def_msgbar = QLabel(self.statusbar_widget)
        self.def_msgbar.setObjectName(u"def_msgbar")
        sizePolicy4.setHeightForWidth(self.def_msgbar.sizePolicy().hasHeightForWidth())
        self.def_msgbar.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.def_msgbar)

        self.msgbar = QLabel(self.statusbar_widget)
        self.msgbar.setObjectName(u"msgbar")
        sizePolicy4.setHeightForWidth(self.msgbar.sizePolicy().hasHeightForWidth())
        self.msgbar.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.msgbar)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.progressBar = QProgressBar(self.statusbar_widget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setMinimumSize(QSize(100, 15))
        self.progressBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	font: 700;\n"
"	text-align:center;\n"
"}")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(100)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.statusbar_widget)


        self.gridLayout.addWidget(self.main_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_9.setBuddy(self.airfoil_firstdigit_input)
        self.label_10.setBuddy(self.airfoil_seconddigit_input)
        self.label_11.setBuddy(self.airfoil_thirddigit_input)
        self.label_12.setBuddy(self.airfoil_lasttwodigits_input)
        self.label_13.setBuddy(self.airfoil_npoints_input)
        self.label_16.setBuddy(self.station_uploadairfoil_button)
        self.label_17.setBuddy(self.station_listairfoils_box)
        self.label_22.setBuddy(self.station_offsety_input)
        self.label_24.setBuddy(self.station_multx_input)
        self.label_25.setBuddy(self.station_multy_input)
        self.label_21.setBuddy(self.station_offsetx_input)
        self.label_20.setBuddy(self.station_twistangle_input)
        self.label_23.setBuddy(self.station_offsetz_input)
        self.label_28.setBuddy(self.station_mirrory_input)
        self.label_27.setBuddy(self.station_mirrorx_input)
        self.label_26.setBuddy(self.station_multz_input)
        self.label_19.setBuddy(self.station_chordlength_input)
        self.label_44.setBuddy(self.station_nStationsAdv_input)
        self.label_36.setBuddy(self.skin_savefig_input)
        self.label_32.setBuddy(self.skin_plythickness_input)
        self.label_34.setBuddy(self.skin_tethickness_input)
        self.label_31.setBuddy(self.skin_nplies_input)
        self.label_33.setBuddy(self.skin_overlaptarget_input)
        self.label_30.setBuddy(self.skin_liststations)
        self.label_46.setBuddy(self.abaqus_expFileName_input)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.home_page_button, self.airfoil_page_button)
        QWidget.setTabOrder(self.airfoil_page_button, self.station_page_button)
        QWidget.setTabOrder(self.station_page_button, self.blade_page_button)
        QWidget.setTabOrder(self.blade_page_button, self.parts_button)
        QWidget.setTabOrder(self.parts_button, self.skin_page_button)
        QWidget.setTabOrder(self.skin_page_button, self.spar_page_button)
        QWidget.setTabOrder(self.spar_page_button, self.abaqus_page_button)
        QWidget.setTabOrder(self.abaqus_page_button, self.settings_button)
        QWidget.setTabOrder(self.settings_button, self.info_button)
        QWidget.setTabOrder(self.info_button, self.quit_button)
        QWidget.setTabOrder(self.quit_button, self.workpath_lineedit)
        QWidget.setTabOrder(self.workpath_lineedit, self.changedir_button)
        QWidget.setTabOrder(self.changedir_button, self.newproject_button)
        QWidget.setTabOrder(self.newproject_button, self.loadproject_button)
        QWidget.setTabOrder(self.loadproject_button, self.airfoil_saveairfoil_button)
        QWidget.setTabOrder(self.airfoil_saveairfoil_button, self.airfoil_delairfoil_button)
        QWidget.setTabOrder(self.airfoil_delairfoil_button, self.airfoil_uploadcoords_button)
        QWidget.setTabOrder(self.airfoil_uploadcoords_button, self.airfoil_coord_name)
        QWidget.setTabOrder(self.airfoil_coord_name, self.airfoil_firstdigit_input)
        QWidget.setTabOrder(self.airfoil_firstdigit_input, self.airfoil_seconddigit_input)
        QWidget.setTabOrder(self.airfoil_seconddigit_input, self.airfoil_thirddigit_input)
        QWidget.setTabOrder(self.airfoil_thirddigit_input, self.airfoil_lasttwodigits_input)
        QWidget.setTabOrder(self.airfoil_lasttwodigits_input, self.airfoil_npoints_input)
        QWidget.setTabOrder(self.airfoil_npoints_input, self.airfoil_resetzoom_button)
        QWidget.setTabOrder(self.airfoil_resetzoom_button, self.airfoil_chartview)
        QWidget.setTabOrder(self.airfoil_chartview, self.airfoil_listairfoils_widget)
        QWidget.setTabOrder(self.airfoil_listairfoils_widget, self.station_uploadairfoil_button)
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
        QWidget.setTabOrder(self.station_delstation_button, self.station_chartview)
        QWidget.setTabOrder(self.station_chartview, self.station_resetzoom_button)
        QWidget.setTabOrder(self.station_resetzoom_button, self.station_liststation_box)
        QWidget.setTabOrder(self.station_liststation_box, self.blade_olpsta_chartview)
        QWidget.setTabOrder(self.blade_olpsta_chartview, self.blade_olplen_chartview)
        QWidget.setTabOrder(self.blade_olplen_chartview, self.blade_interpolate_button)
        QWidget.setTabOrder(self.blade_interpolate_button, self.blade_skinolplen_table)
        QWidget.setTabOrder(self.blade_skinolplen_table, self.blade_order_input)
        QWidget.setTabOrder(self.blade_order_input, self.blade_skinolpsta_selected)
        QWidget.setTabOrder(self.blade_skinolpsta_selected, self.blade_skinolplen_selected)
        QWidget.setTabOrder(self.blade_skinolplen_selected, self.blade_saveparams_button)
        QWidget.setTabOrder(self.blade_saveparams_button, self.blade_skinolpsta_table)
        QWidget.setTabOrder(self.blade_skinolpsta_table, self.skin_liststations)
        QWidget.setTabOrder(self.skin_liststations, self.skin_nplies_input)
        QWidget.setTabOrder(self.skin_nplies_input, self.skin_plythickness_input)
        QWidget.setTabOrder(self.skin_plythickness_input, self.skin_overlaptarget_input)
        QWidget.setTabOrder(self.skin_overlaptarget_input, self.skin_tethickness_input)
        QWidget.setTabOrder(self.skin_tethickness_input, self.skin_savefig_input)
        QWidget.setTabOrder(self.skin_savefig_input, self.skin_full_chartview)
        QWidget.setTabOrder(self.skin_full_chartview, self.skin_zoom_chartview)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.station_tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.home_page_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.airfoil_page_button.setText(QCoreApplication.translate("MainWindow", u"Airfoil Creator", None))
        self.station_page_button.setText(QCoreApplication.translate("MainWindow", u"Station Generator", None))
        self.blade_page_button.setText(QCoreApplication.translate("MainWindow", u"Blade Parameters", None))
        self.parts_button.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.skin_page_button.setText(QCoreApplication.translate("MainWindow", u"Skin", None))
        self.spar_page_button.setText(QCoreApplication.translate("MainWindow", u"Spar", None))
        self.abaqus_page_button.setText(QCoreApplication.translate("MainWindow", u"Abaqus Export", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.info_button.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.quit_button.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.page_title_label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Work Directory:", None))
        self.workpath_lineedit.setText("")
        self.changedir_button.setText(QCoreApplication.translate("MainWindow", u"Change...", None))
        self.loadproject_button.setText(QCoreApplication.translate("MainWindow", u"Load Project...", None))
        self.newproject_button.setText(QCoreApplication.translate("MainWindow", u"New Project...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Welcome to SimBladEd", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Version 0.1", None))
        self.label_5.setText("")
        self.airfoil_saveairfoil_button.setText(QCoreApplication.translate("MainWindow", u"Save airfoil", None))
        self.airfoil_delairfoil_button.setText(QCoreApplication.translate("MainWindow", u"Delete airfoil", None))
        self.airfoil_uploadcoords_button.setText(QCoreApplication.translate("MainWindow", u"Upload coordinates:", None))
        self.airfoil_coord_name.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"NACA series:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Second digit:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Third digit:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Last two digits:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Number of points:", None))
        self.airfoil_resetzoom_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.airfoil_xy_current.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Airfoils available:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Airfoil", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Upload airfoil file:", None))
        self.station_uploadairfoil_button.setText(QCoreApplication.translate("MainWindow", u"Select file...", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Available airfoils:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Offset y:", None))
        self.station_mirrory_input.setText(QCoreApplication.translate("MainWindow", u"True", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Multiplier x:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Multiplier y:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Offset x:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Twist angle:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Offset z:", None))
        self.station_mirrorx_input.setText(QCoreApplication.translate("MainWindow", u"True", None))
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
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Current station:", None))
        self.station_resetzoom_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.station_xy_current.setText("")
        self.station_tab_widget.setTabText(self.station_tab_widget.indexOf(self.station_tab1), QCoreApplication.translate("MainWindow", u"Interactive", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Number of stations:", None))
        self.station_saveTable_button.setText(QCoreApplication.translate("MainWindow", u"Save Stations", None))
        self.station_sortTable_button.setText(QCoreApplication.translate("MainWindow", u"Sort Stations", None))
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

        __sortingEnabled = self.station_tableStations_input.isSortingEnabled()
        self.station_tableStations_input.setSortingEnabled(False)
        self.station_tableStations_input.setSortingEnabled(__sortingEnabled)

        self.station_tab_widget.setTabText(self.station_tab_widget.indexOf(self.station_tab2), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.blade_interpolate_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Skin Overlap Length", None))
        ___qtablewidgetitem11 = self.blade_skinolplen_table.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Distance", None));
        ___qtablewidgetitem12 = self.blade_skinolplen_table.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Interpolation order:", None))
        self.blade_order_input.setSuffix("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Choose interpolation order:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Skin overlap distance:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Skin overlap length:", None))
        self.blade_saveparams_button.setText(QCoreApplication.translate("MainWindow", u"Save Parameters", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Skin Overlap Distance", None))
        ___qtablewidgetitem13 = self.blade_skinolpsta_table.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Distance", None));
        ___qtablewidgetitem14 = self.blade_skinolpsta_table.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Save figures:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Ply thickness:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Trailing edge thickness:", None))
        self.skin_nplies_input.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.skin_plythickness_input.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.skin_savefig_input.setText(QCoreApplication.translate("MainWindow", u"True", None))
        self.skin_tethickness_input.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Number of plies:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Overlap target:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Available stations:", None))
        self.skin_saveSection_button.setText(QCoreApplication.translate("MainWindow", u"Save Section", None))
        self.skin_delSection_button.setText(QCoreApplication.translate("MainWindow", u"Delete Section", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Spar Page: Coming Soon", None))
        self.abaqus_expFileName_input.setText(QCoreApplication.translate("MainWindow", u"skin", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Export file name:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u".json", None))
        self.abaqus_export_button.setText(QCoreApplication.translate("MainWindow", u"Export Sections", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Export Sections", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Select the sections to be exported as .json files:", None))
        self.def_msgbar.setText(QCoreApplication.translate("MainWindow", u"Ready.", None))
        self.msgbar.setText("")
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
    # retranslateUi

