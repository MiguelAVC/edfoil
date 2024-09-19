# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_widget = QWidget(self.centralwidget)
        self.sidebar_widget.setObjectName(u"sidebar_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_widget.sizePolicy().hasHeightForWidth())
        self.sidebar_widget.setSizePolicy(sizePolicy)
        self.sidebar_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(35, 46, 47);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:left;\n"
"	border:none;\n"
"	height:30px;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,255,255,0.4);\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	color: rgb(35, 46, 47);\n"
"	background-color: white;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.sidebar_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fastblade_logo = QLabel(self.sidebar_widget)
        self.fastblade_logo.setObjectName(u"fastblade_logo")
        self.fastblade_logo.setMaximumSize(QSize(139, 32))
        self.fastblade_logo.setPixmap(QPixmap(u":/images/fastablade-white.png"))
        self.fastblade_logo.setScaledContents(True)
        self.fastblade_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fastblade_logo.setMargin(2)

        self.verticalLayout_3.addWidget(self.fastblade_logo)

        self.app_label = QLabel(self.sidebar_widget)
        self.app_label.setObjectName(u"app_label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.app_label.setFont(font1)
        self.app_label.setStyleSheet(u"color:white")
        self.app_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.app_label)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 57, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.naca_button = QPushButton(self.sidebar_widget)
        self.naca_button.setObjectName(u"naca_button")
        icon = QIcon()
        icon.addFile(u":/images/board-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/images/board.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.naca_button.setIcon(icon)
        self.naca_button.setCheckable(True)
        self.naca_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.naca_button)

        self.airfoil_button = QPushButton(self.sidebar_widget)
        self.airfoil_button.setObjectName(u"airfoil_button")
        icon1 = QIcon()
        icon1.addFile(u":/images/energy-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/images/energy.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.airfoil_button.setIcon(icon1)
        self.airfoil_button.setCheckable(True)
        self.airfoil_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.airfoil_button)

        self.station_button = QPushButton(self.sidebar_widget)
        self.station_button.setObjectName(u"station_button")
        self.station_button.setIcon(icon1)
        self.station_button.setCheckable(True)
        self.station_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.station_button)

        self.parameter_button = QPushButton(self.sidebar_widget)
        self.parameter_button.setObjectName(u"parameter_button")
        self.parameter_button.setIcon(icon1)
        self.parameter_button.setCheckable(True)
        self.parameter_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.parameter_button)

        self.abaqus_button = QPushButton(self.sidebar_widget)
        self.abaqus_button.setObjectName(u"abaqus_button")
        icon2 = QIcon()
        icon2.addFile(u":/images/settings-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/images/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.abaqus_button.setIcon(icon2)
        self.abaqus_button.setCheckable(True)
        self.abaqus_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.abaqus_button)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 140, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.settings_button = QPushButton(self.sidebar_widget)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setIcon(icon2)

        self.verticalLayout.addWidget(self.settings_button)

        self.info_button = QPushButton(self.sidebar_widget)
        self.info_button.setObjectName(u"info_button")
        icon3 = QIcon()
        icon3.addFile(u":/images/info-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/images/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.info_button.setIcon(icon3)

        self.verticalLayout.addWidget(self.info_button)

        self.quit_button = QPushButton(self.sidebar_widget)
        self.quit_button.setObjectName(u"quit_button")
        icon4 = QIcon()
        icon4.addFile(u":/images/door-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/images/door.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.quit_button.setIcon(icon4)

        self.verticalLayout.addWidget(self.quit_button)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.sidebar_widget, 0, 0, 2, 1)

        self.title_widget = QWidget(self.centralwidget)
        self.title_widget.setObjectName(u"title_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_widget.sizePolicy().hasHeightForWidth())
        self.title_widget.setSizePolicy(sizePolicy1)
        self.title_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255,255,255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.title_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.page_title_label = QLabel(self.title_widget)
        self.page_title_label.setObjectName(u"page_title_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_title_label.sizePolicy().hasHeightForWidth())
        self.page_title_label.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setUnderline(False)
        self.page_title_label.setFont(font2)

        self.horizontalLayout.addWidget(self.page_title_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.work_dir_label = QLabel(self.title_widget)
        self.work_dir_label.setObjectName(u"work_dir_label")
        sizePolicy2.setHeightForWidth(self.work_dir_label.sizePolicy().hasHeightForWidth())
        self.work_dir_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.work_dir_label)

        self.path_label = QLabel(self.title_widget)
        self.path_label.setObjectName(u"path_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.path_label.sizePolicy().hasHeightForWidth())
        self.path_label.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.path_label)

        self.change_path_button = QPushButton(self.title_widget)
        self.change_path_button.setObjectName(u"change_path_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.change_path_button.sizePolicy().hasHeightForWidth())
        self.change_path_button.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.change_path_button)


        self.gridLayout.addWidget(self.title_widget, 0, 1, 1, 1)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(221, 221, 221);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.main_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy5)
        self.intro_page = QWidget()
        self.intro_page.setObjectName(u"intro_page")
        self.label_6 = QLabel(self.intro_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 230, 81, 41))
        self.stackedWidget.addWidget(self.intro_page)
        self.naca_page = QWidget()
        self.naca_page.setObjectName(u"naca_page")
        self.label_9 = QLabel(self.naca_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(280, 230, 141, 61))
        self.stackedWidget.addWidget(self.naca_page)
        self.airfoil_page = QWidget()
        self.airfoil_page.setObjectName(u"airfoil_page")
        self.widget = QWidget(self.airfoil_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 1078, 602))
        self.horizontalLayout_14 = QHBoxLayout(self.widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_23)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_12.addWidget(self.label_2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_16)

        self.upload_airfoil_button = QPushButton(self.widget)
        self.upload_airfoil_button.setObjectName(u"upload_airfoil_button")

        self.horizontalLayout_12.addWidget(self.upload_airfoil_button)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_18)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_13.addWidget(self.label)

        self.horizontalSpacer_17 = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.list_airfoils_box = QComboBox(self.widget)
        self.list_airfoils_box.setObjectName(u"list_airfoils_box")
        self.list_airfoils_box.setDuplicatesEnabled(False)

        self.verticalLayout_6.addWidget(self.list_airfoils_box)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_12)

        self.chord_length_input = QLineEdit(self.widget)
        self.chord_length_input.setObjectName(u"chord_length_input")
        sizePolicy4.setHeightForWidth(self.chord_length_input.sizePolicy().hasHeightForWidth())
        self.chord_length_input.setSizePolicy(sizePolicy4)
        self.chord_length_input.setMaxLength(16)
        self.chord_length_input.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.chord_length_input.setInputMask('#DDDDDDD')

        self.horizontalLayout_4.addWidget(self.chord_length_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.twist_angle_input = QLineEdit(self.widget)
        self.twist_angle_input.setObjectName(u"twist_angle_input")
        sizePolicy4.setHeightForWidth(self.twist_angle_input.sizePolicy().hasHeightForWidth())
        self.twist_angle_input.setSizePolicy(sizePolicy4)
        self.twist_angle_input.setMaxLength(16)
        self.twist_angle_input.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.twist_angle_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_14)

        self.x_offset_input = QLineEdit(self.widget)
        self.x_offset_input.setObjectName(u"x_offset_input")
        sizePolicy4.setHeightForWidth(self.x_offset_input.sizePolicy().hasHeightForWidth())
        self.x_offset_input.setSizePolicy(sizePolicy4)
        self.x_offset_input.setMaxLength(16)
        self.x_offset_input.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.x_offset_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_15)

        self.y_offset_input = QLineEdit(self.widget)
        self.y_offset_input.setObjectName(u"y_offset_input")
        sizePolicy4.setHeightForWidth(self.y_offset_input.sizePolicy().hasHeightForWidth())
        self.y_offset_input.setSizePolicy(sizePolicy4)
        self.y_offset_input.setMaxLength(16)
        self.y_offset_input.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.y_offset_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_16)

        self.z_offset_input = QLineEdit(self.widget)
        self.z_offset_input.setObjectName(u"z_offset_input")
        sizePolicy4.setHeightForWidth(self.z_offset_input.sizePolicy().hasHeightForWidth())
        self.z_offset_input.setSizePolicy(sizePolicy4)
        self.z_offset_input.setMaxLength(16)
        self.z_offset_input.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.z_offset_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_17)

        self.x_multiplier_input = QLineEdit(self.widget)
        self.x_multiplier_input.setObjectName(u"x_multiplier_input")
        sizePolicy4.setHeightForWidth(self.x_multiplier_input.sizePolicy().hasHeightForWidth())
        self.x_multiplier_input.setSizePolicy(sizePolicy4)
        self.x_multiplier_input.setMaxLength(16)
        self.x_multiplier_input.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.x_multiplier_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy6)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_18)

        self.y_multiplier_input = QLineEdit(self.widget)
        self.y_multiplier_input.setObjectName(u"y_multiplier_input")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.y_multiplier_input.sizePolicy().hasHeightForWidth())
        self.y_multiplier_input.setSizePolicy(sizePolicy7)
        self.y_multiplier_input.setMaxLength(16)
        self.y_multiplier_input.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.y_multiplier_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_19)

        self.z_multiplier_input = QLineEdit(self.widget)
        self.z_multiplier_input.setObjectName(u"z_multiplier_input")
        sizePolicy4.setHeightForWidth(self.z_multiplier_input.sizePolicy().hasHeightForWidth())
        self.z_multiplier_input.setSizePolicy(sizePolicy4)
        self.z_multiplier_input.setMaxLength(16)
        self.z_multiplier_input.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.z_multiplier_input)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_20)

        self.horizontalSpacer_12 = QSpacerItem(52, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.x_mirror_input = QCheckBox(self.widget)
        self.x_mirror_input.setObjectName(u"x_mirror_input")

        self.horizontalLayout_2.addWidget(self.x_mirror_input)

        self.horizontalSpacer_13 = QSpacerItem(52, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_21)

        self.horizontalSpacer_14 = QSpacerItem(52, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.y_mirror_input = QCheckBox(self.widget)
        self.y_mirror_input.setObjectName(u"y_mirror_input")
        self.y_mirror_input.setChecked(True)

        self.horizontalLayout_11.addWidget(self.y_mirror_input)

        self.horizontalSpacer_15 = QSpacerItem(52, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.horizontalLayout_14.addLayout(self.verticalLayout_7)

        self.airfoil_chart_widget = QWidget(self.widget)
        self.airfoil_chart_widget.setObjectName(u"airfoil_chart_widget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.airfoil_chart_widget.sizePolicy().hasHeightForWidth())
        self.airfoil_chart_widget.setSizePolicy(sizePolicy8)
        self.airfoil_chart_widget.setMinimumSize(QSize(800, 600))

        self.horizontalLayout_14.addWidget(self.airfoil_chart_widget)

        self.stackedWidget.addWidget(self.airfoil_page)
        self.station_page = QWidget()
        self.station_page.setObjectName(u"station_page")
        self.label_11 = QLabel(self.station_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(270, 260, 141, 61))
        self.stackedWidget.addWidget(self.station_page)
        self.parameters_page = QWidget()
        self.parameters_page.setObjectName(u"parameters_page")
        self.label_10 = QLabel(self.parameters_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(250, 300, 141, 61))
        self.stackedWidget.addWidget(self.parameters_page)
        self.abaqus_page = QWidget()
        self.abaqus_page.setObjectName(u"abaqus_page")
        self.label_7 = QLabel(self.abaqus_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 220, 141, 61))
        self.stackedWidget.addWidget(self.abaqus_page)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.main_widget, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.title_widget.raise_()
        self.main_widget.raise_()
        self.sidebar_widget.raise_()
        QWidget.setTabOrder(self.change_path_button, self.naca_button)
        QWidget.setTabOrder(self.naca_button, self.airfoil_button)
        QWidget.setTabOrder(self.airfoil_button, self.station_button)
        QWidget.setTabOrder(self.station_button, self.parameter_button)
        QWidget.setTabOrder(self.parameter_button, self.abaqus_button)
        QWidget.setTabOrder(self.abaqus_button, self.settings_button)
        QWidget.setTabOrder(self.settings_button, self.info_button)
        QWidget.setTabOrder(self.info_button, self.quit_button)
        QWidget.setTabOrder(self.quit_button, self.upload_airfoil_button)
        QWidget.setTabOrder(self.upload_airfoil_button, self.list_airfoils_box)
        QWidget.setTabOrder(self.list_airfoils_box, self.chord_length_input)
        QWidget.setTabOrder(self.chord_length_input, self.twist_angle_input)
        QWidget.setTabOrder(self.twist_angle_input, self.x_offset_input)
        QWidget.setTabOrder(self.x_offset_input, self.y_offset_input)
        QWidget.setTabOrder(self.y_offset_input, self.z_offset_input)
        QWidget.setTabOrder(self.z_offset_input, self.x_multiplier_input)
        QWidget.setTabOrder(self.x_multiplier_input, self.y_multiplier_input)
        QWidget.setTabOrder(self.y_multiplier_input, self.z_multiplier_input)
        QWidget.setTabOrder(self.z_multiplier_input, self.x_mirror_input)
        QWidget.setTabOrder(self.x_mirror_input, self.y_mirror_input)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fastblade_logo.setText("")
        self.app_label.setText(QCoreApplication.translate("MainWindow", u"TBlade Designer", None))
        self.naca_button.setText(QCoreApplication.translate("MainWindow", u"NACA Generator", None))
        self.airfoil_button.setText(QCoreApplication.translate("MainWindow", u"Airfoils", None))
        self.station_button.setText(QCoreApplication.translate("MainWindow", u"Stations", None))
        self.parameter_button.setText(QCoreApplication.translate("MainWindow", u"Blade Parameters", None))
        self.abaqus_button.setText(QCoreApplication.translate("MainWindow", u"Abaqus Export", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.info_button.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.quit_button.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.page_title_label.setText(QCoreApplication.translate("MainWindow", u"Blade Parameters", None))
        self.work_dir_label.setText(QCoreApplication.translate("MainWindow", u"Work Directory:", None))
        self.path_label.setText("")
        self.change_path_button.setText(QCoreApplication.translate("MainWindow", u"Change...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Intro Page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"NACA Page", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Airfoil", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Upload airfoil file:", None))
        self.upload_airfoil_button.setText(QCoreApplication.translate("MainWindow", u"Select file...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Available airfoils:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Chord length:", None))
        self.chord_length_input.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Twist angle:", None))
        self.twist_angle_input.setText(QCoreApplication.translate("MainWindow", u"32.0", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Offset x:", None))
        self.x_offset_input.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Offset y:", None))
        self.y_offset_input.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Offset z:", None))
        self.z_offset_input.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Multiplier x:", None))
        self.x_multiplier_input.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Multiplier y:", None))
        self.y_multiplier_input.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Multiplier z:", None))
        self.z_multiplier_input.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Mirror x:", None))
        self.x_mirror_input.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Mirror y:", None))
        self.y_mirror_input.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Station Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Parameters Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Abaqus Page", None))
    # retranslateUi

