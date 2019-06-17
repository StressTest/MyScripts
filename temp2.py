from PySide2 import QtWidgets, QtGui, QtCore
import sys
import random

class MainWindow(QtWidgets.QWidget):
    i=0
    def __init__(self):
        super().__init__()
        # self.init_UI()

    # def init_UI(self):
        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
            "Hola Mundo", "Привет мир"]
        self.button = QtWidgets.QPushButton('Кнопка', self)
        # self.text = QtWidgets.QTextBrowser(self)

        # self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.button.clicked.connect(self.button_pushed())
        self.button.move(200,200)


    def button_pushed(self):
        self.i += 1
        # self.setWindowTitle(str(self.i))
        # print('Нажата')

class MyWidget(QtWidgets.QWidget):
    i = 0
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
            "Hola Mundo", "Привет мир"]
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.magic)



    def magic(self):
        self.i += 1
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    # widget = MyWidget()
    widget.show()
    app.exec_()
    print(widget.i)
    sys.exit()
