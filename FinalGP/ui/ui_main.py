# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(542, 418)
        icon = QIcon()
        icon.addFile(u":/icons/key_FILL0_wght400_GRAD0_opsz48.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"    background-color: #a7a7a7;\n"
"    color:black;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin:10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: #090;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 4px solid #090;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #006300;\n"
"	border-color: #090;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setStyleSheet(u"border: none")
        icon1 = QIcon()
        icon1.addFile(u":/icons/lock_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.pushButton)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.frame_password = QFrame(self.centralwidget)
        self.frame_password.setObjectName(u"frame_password")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_password.sizePolicy().hasHeightForWidth())
        self.frame_password.setSizePolicy(sizePolicy)
        self.frame_password.setStyleSheet(u"QFrame{\n"
"	border: 2px solid black;\n"
"	border-radius: 5px;\n"
"	margin-right:0;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border-color:#090;\n"
"}")
        self.frame_password.setFrameShape(QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_password)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_password = QLineEdit(self.frame_password)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setStyleSheet(u"QLineEdit{\n"
"	border: none;\n"
"	margin:0;\n"
"	font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.line_password)

        self.btn_visibility = QPushButton(self.frame_password)
        self.btn_visibility.setObjectName(u"btn_visibility")
        self.btn_visibility.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visibility.setStyleSheet(u"QPushButton{\n"
"    border: none;\n"
"    margin: 0;\n"
"    background-color: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/visibility_off_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/visibility_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visibility.setIcon(icon2)
        self.btn_visibility.setIconSize(QSize(30, 30))
        self.btn_visibility.setCheckable(True)
        self.btn_visibility.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btn_visibility)


        self.layout_password.addWidget(self.frame_password)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"    margin-right: 0;\n"
"    margin-left: 0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/refresh_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_refresh.setIcon(icon3)
        self.btn_refresh.setIconSize(QSize(52, 52))

        self.layout_password.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_copy.sizePolicy().hasHeightForWidth())
        self.btn_copy.setSizePolicy(sizePolicy1)
        self.btn_copy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_copy.setLayoutDirection(Qt.LeftToRight)
        self.btn_copy.setStyleSheet(u"QPushButton{\n"
"    padding: 5px;\n"
"    margin-left: 0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/content_copy_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_copy.setIcon(icon4)
        self.btn_copy.setIconSize(QSize(42, 42))

        self.layout_password.addWidget(self.btn_copy)


        self.verticalLayout.addLayout(self.layout_password)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.label_strength = QLabel(self.centralwidget)
        self.label_strength.setObjectName(u"label_strength")
        sizePolicy.setHeightForWidth(self.label_strength.sizePolicy().hasHeightForWidth())
        self.label_strength.setSizePolicy(sizePolicy)
        self.label_strength.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.label_strength)

        self.label_entropy = QLabel(self.centralwidget)
        self.label_entropy.setObjectName(u"label_entropy")
        sizePolicy.setHeightForWidth(self.label_entropy.sizePolicy().hasHeightForWidth())
        self.label_entropy.setSizePolicy(sizePolicy)
        self.label_entropy.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.label_entropy)


        self.verticalLayout.addLayout(self.layout_info)

        self.layout_length = QHBoxLayout()
        self.layout_length.setObjectName(u"layout_length")
        self.slider_length = QSlider(self.centralwidget)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_length.setStyleSheet(u"QSlider::groove:horizontal{\n"
"    background-color: #090;\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"	backgrounf-color: #090;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"	background-color:black;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"	background-color: black;\n"
"	widht: 22px;\n"
"	border-radius:10px;\n"
"	margin-top:-8px;\n"
"	margin-bottom:-8px;\n"
"}")
        self.slider_length.setMaximum(100)
        self.slider_length.setSingleStep(0)
        self.slider_length.setValue(12)
        self.slider_length.setOrientation(Qt.Horizontal)

        self.layout_length.addWidget(self.slider_length)

        self.spinbox_length = QSpinBox(self.centralwidget)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setStyleSheet(u"QSpinBox{\n"
"	border: 2px solid black;\n"
"	border-radius: 5px;\n"
"	background: transparent;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"	border-color: #009900;\n"
"}")
        self.spinbox_length.setAlignment(Qt.AlignCenter)
        self.spinbox_length.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinbox_length.setMaximum(100)
        self.spinbox_length.setValue(12)

        self.layout_length.addWidget(self.spinbox_length)


        self.verticalLayout.addLayout(self.layout_length)

        self.layout_symbols = QHBoxLayout()
        self.layout_symbols.setObjectName(u"layout_symbols")
        self.Button_az = QPushButton(self.centralwidget)
        self.Button_az.setObjectName(u"Button_az")
        self.Button_az.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_az.setIconSize(QSize(16, 16))
        self.Button_az.setCheckable(True)
        self.Button_az.setChecked(True)

        self.layout_symbols.addWidget(self.Button_az)

        self.Button_AZ = QPushButton(self.centralwidget)
        self.Button_AZ.setObjectName(u"Button_AZ")
        self.Button_AZ.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_AZ.setIconSize(QSize(16, 16))
        self.Button_AZ.setCheckable(True)
        self.Button_AZ.setChecked(True)

        self.layout_symbols.addWidget(self.Button_AZ)

        self.Button_09 = QPushButton(self.centralwidget)
        self.Button_09.setObjectName(u"Button_09")
        self.Button_09.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_09.setIconSize(QSize(16, 16))
        self.Button_09.setCheckable(True)
        self.Button_09.setChecked(True)

        self.layout_symbols.addWidget(self.Button_09)

        self.Button_Special = QPushButton(self.centralwidget)
        self.Button_Special.setObjectName(u"Button_Special")
        self.Button_Special.setCursor(QCursor(Qt.PointingHandCursor))
        self.Button_Special.setIconSize(QSize(16, 16))
        self.Button_Special.setCheckable(True)
        self.Button_Special.setChecked(False)

        self.layout_symbols.addWidget(self.Button_Special)


        self.verticalLayout.addLayout(self.layout_symbols)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PasswordGeneration", None))
        self.pushButton.setText("")
        self.btn_visibility.setText("")
        self.btn_refresh.setText("")
        self.btn_copy.setText("")
        self.label_strength.setText("")
        self.label_entropy.setText("")
        self.Button_az.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.Button_AZ.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.Button_09.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.Button_Special.setText(QCoreApplication.translate("MainWindow", u"#$%", None))
    # retranslateUi

