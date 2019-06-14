# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Terminal(object):
    def setupUi(self, Terminal):
        Terminal.setObjectName("Terminal")
        Terminal.resize(460, 200)
        Terminal.setMaximumSize(QtCore.QSize(640, 800))
        Terminal.setSizeGripEnabled(False)
        self.connectBtn = QtWidgets.QPushButton(Terminal)
        self.connectBtn.setGeometry(QtCore.QRect(20, 20, 90, 40))
        self.connectBtn.setObjectName("connectBtn")
        self.reconnectBtn = QtWidgets.QPushButton(Terminal)
        self.reconnectBtn.setGeometry(QtCore.QRect(20, 80, 90, 40))
        self.reconnectBtn.setObjectName("reconnectBtn")
        self.closeBtn = QtWidgets.QPushButton(Terminal)
        self.closeBtn.setGeometry(QtCore.QRect(20, 140, 90, 40))
        self.closeBtn.setObjectName("closeBtn")
        self.updateBtn = QtWidgets.QPushButton(Terminal)
        self.updateBtn.setGeometry(QtCore.QRect(140, 80, 90, 40))
        self.updateBtn.setObjectName("updateBtn")
        self.comportBox = QtWidgets.QComboBox(Terminal)
        self.comportBox.setGeometry(QtCore.QRect(140, 20, 90, 40))
        self.comportBox.setObjectName("comportBox")
        self.comportBox.addItem("")
        self.comportBox.addItem("")
        self.comportBox.addItem("")
        self.comportBox.addItem("")
        self.comportBox.addItem("")
        self.speedBox = QtWidgets.QComboBox(Terminal)
        self.speedBox.setGeometry(QtCore.QRect(140, 140, 90, 40))
        self.speedBox.setObjectName("speedBox")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(Terminal)
        self.textBrowser.setGeometry(QtCore.QRect(250, 20, 190, 160))
        self.textBrowser.setBaseSize(QtCore.QSize(190, 160))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Terminal)
        QtCore.QMetaObject.connectSlotsByName(Terminal)

    def retranslateUi(self, Terminal):
        _translate = QtCore.QCoreApplication.translate
        Terminal.setWindowTitle(_translate("Terminal", "UART Terminal "))
        self.connectBtn.setText(_translate("Terminal", "Connect"))
        self.reconnectBtn.setText(_translate("Terminal", "Reconnect"))
        self.closeBtn.setText(_translate("Terminal", "Close"))
        self.updateBtn.setText(_translate("Terminal", "Update"))
        self.comportBox.setItemText(0, _translate("Terminal", "COM 1"))
        self.comportBox.setItemText(1, _translate("Terminal", "COM 2"))
        self.comportBox.setItemText(2, _translate("Terminal", "COM 3"))
        self.comportBox.setItemText(3, _translate("Terminal", "COM 4"))
        self.comportBox.setItemText(4, _translate("Terminal", "COM 5"))
        self.speedBox.setItemText(0, _translate("Terminal", "9600"))
        self.speedBox.setItemText(1, _translate("Terminal", "115200"))

