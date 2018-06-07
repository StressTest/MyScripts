# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/andrew/PycharmProjects/MyScripts/first_form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(10, 24, 451, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.min = QtWidgets.QLCDNumber(self.widget1)
        self.min.setObjectName("min")
        self.horizontalLayout_2.addWidget(self.min)
        self.sec = QtWidgets.QLCDNumber(self.widget1)
        self.sec.setObjectName("sec")
        self.horizontalLayout_2.addWidget(self.sec)
        self.dsec = QtWidgets.QLCDNumber(self.widget1)
        self.dsec.setObjectName("dsec")
        self.horizontalLayout_2.addWidget(self.dsec)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(100, 70, 256, 441))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listWidget.setFont(font)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.widget)
        self.widget2 = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget2.sizePolicy().hasHeightForWidth())
        self.widget2.setSizePolicy(sizePolicy)
        self.widget2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_stop_btn = QtWidgets.QPushButton(self.widget2)
        self.start_stop_btn.setObjectName("start_stop_btn")
        self.horizontalLayout.addWidget(self.start_stop_btn)
        self.lap_reset_btn = QtWidgets.QPushButton(self.widget2)
        self.lap_reset_btn.setObjectName("lap_reset_btn")
        self.horizontalLayout.addWidget(self.lap_reset_btn)
        self.verticalLayout.addWidget(self.widget2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.start_stop_btn, self.lap_reset_btn)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "First Gui Application"))
        self.start_stop_btn.setText(_translate("Dialog", "Start/Stop"))
        self.lap_reset_btn.setText(_translate("Dialog", "Lap/Reset"))

