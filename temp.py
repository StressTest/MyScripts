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
import sys

if __name__ == '__main__':
    class MainWindow(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            self.init_window()

        def init_window(self):
            self.setGeometry(300,300,600, 600)
            self.setWindowIcon(QtGui.QIcon('icons.png'))
            self.setWindowTitle('My Terminal')
            btn = QtWidgets.QPushButton(QtGui.QIcon('icons.png'),'Hello', self)
            btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
            self.show()

    app = QtWidgets.QApplication()
    window = MainWindow()
    sys.exit(app.exec_())
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