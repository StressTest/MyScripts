# import sys
# from PyQt5.QtWidgets import (QWidget, QProgressBar,
#     QPushButton, QApplication)
# from PyQt5.QtCore import QBasicTimer
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         self.pbar = QProgressBar(self)
#         self.pbar.setGeometry(30, 40, 200, 25)
#
#         self.btn = QPushButton('Start', self)
#         self.btn.move(40, 80)
#         self.btn.clicked.connect(self.doAction)
#
#         self.timer = QBasicTimer()
#         self.step = 0
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('QProgressBar')
#         self.show()
#
#
#     def timerEvent(self, e):
#
#         if self.step >= 100:
#             self.timer.stop()
#             self.btn.setText('Finished')
#             return
#
#         self.step = self.step + 1
#         self.pbar.setValue(self.step)
#
#
#     def doAction(self):
#
#         if self.timer.isActive():
#             self.timer.stop()
#             self.btn.setText('Start')
#         else:
#             self.timer.start(100, self)
#             self.btn.setText('Stop')

from PySide2 import QtWidgets, QtGui, QtCore
# from PyQt5 import QtWidgets, QtGui, QtCore
import serial.tools.list_ports as list_ports
import serial
import sys


def ports_listO():
    print('pushed external')

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowIcon(QtGui.QIcon('icons.png'))
        self.setWindowTitle('My Terminal')
        self.connect_btn = QtWidgets.QPushButton(QtGui.QIcon('icons.png'), 'Connect', self)
        self.connect_btn.setGeometry(20, 20, 90, 40)

        self.disconnect_btn = QtWidgets.QPushButton('Disconnect', self)
        self.disconnect_btn.setGeometry(20, 80, 90, 40)

        self.close_btn = QtWidgets.QPushButton('Close', self)
        self.close_btn.setGeometry(20, 140, 90, 40)

        self.update_btn = QtWidgets.QPushButton('Update', self)
        self.update_btn.setGeometry(140, 80, 90, 40)


        self.ports_box = QtWidgets.QComboBox(self)
        self.ports_box.setGeometry(140, 20, 90, 40)
        self.update_ports_list()

        self.speed_box = QtWidgets.QComboBox(self)
        self.speed_box.setGeometry(140, 140, 90, 40)
        self.speed_box.addItem('300')
        self.speed_box.addItem('600')
        self.speed_box.addItem('1200')
        self.speed_box.addItem('2400')
        self.speed_box.addItem('4800')
        self.speed_box.addItem('9600')
        self.speed_box.addItem('19200')
        self.speed_box.addItem('38400')
        self.speed_box.addItem('57600')
        self.speed_box.addItem("115200")


        self.connection = serial.Serial()
        print(self.connection.is_open)
        self.close_btn.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.update_btn.clicked.connect(self.update_ports_list)

        self.connect_btn.clicked.connect(self.uart_connect)
        self.disconnect_btn.clicked.connect(self.uart_disconnect)
        # self.connect_btn.clicked.connect()
        # self.update_btn.clicked.connect(print('xxx'))
        self.show()

    def update_ports_list(self):
        for i in range(self.ports_box.count(), -1, -1):
            self.ports_box.removeItem(i)
        ports = [port.device for port in list_ports.comports()]
        ports.sort()
        for port in ports:
            self.ports_box.addItem(port)


    def uart_connect(self):
        # port = self.ports_box.currentText()
        # baudrate = self.speed_box.currentText()
        # self.connection = serial.Serial(port=port, baudrate=baudrate)
        # self.connection.write(b'hello')
        port = self.ports_box.currentText()
        baudrate = self.speed_box.currentText()
        self.connection = serial.Serial(port=port, baudrate=baudrate)
        self.connection.write(b'hello')
        # self.connection.close()
        # print(self.connection.is_open)

    def uart_disconnect(self):
        # port = self.ports_box.currentText()
        # baudrate = self.speed_box.currentText()
        print(self.connection.is_open)
        self.connection.close()
        print(self.connection.is_open)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
    sys.exit()

    # sys.exit(app.exec_())
    # w = QtWidgets.QWidget()
    # print(w)
    # w.setWindowTitle('Hi, everyone!')
    # # w.resize(100,200)
    # w.resize(1024, 768)
    # w.set
    # # w.setBaseSize((100, 200))
    # ico = QtGui.QIcon('icons.png')
    # w.setWindowIcon(ico)
    # w.show()
    # w.setG
    # # sys.exit()
    #
    # app.exec_()

    # app = QApplication(sys.argv)
    # ex = Example()
    # sys.exit(app.exec_())

#     def str_to_float(text):
#         """Функция переводящяя строку в число
#
# str -> float
#         """
#         result = 0
#         try:
#             if not isinstance(text, str):
#                 raise TypeError
#             result = float(text)
#         except ValueError:
#             print('Невозможно перевести в число. Будет возвращено 0')
#         except TypeError:
#             print('Невозможно перевести в число. Будет возвращено 1')
#             result = 1
#         finally:
#             return result
#
#     class Square:
#         squares = []
#
#         def __init__(self, w, h):
#             self.width = w
#             self.height = h
#             self.squares.append((w, h))
#
#
#         def __repr__(self):
#             return "width = {}, height = {}".format(self.width, self.height)
#
#         def print_squares(self):
#             print(self.squares)
#
#
#     x = Square(3,4)
#     y = Square(7, 8)
#     # z = Square(5)
#     print(type(x), type(y))
#     if type(x) is type(y):
#         print(True)
#     else:
#         print(False)
#     print(x)
#     print(x.squares)
#     y.print_squares()