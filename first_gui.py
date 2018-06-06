import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn = QPushButton("Start/Stop", self)
        btn.resize(btn.sizeHint())
        btn.move(150 - btn.size().width()//2, 25)
        # btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.pressed()
        self.resize(300, 150)
        self.setWindowTitle("First Gui App")

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # w = QWidget()
    # #w.resize(250, 150)
    # w.move(1200, 300)
    # w.setWindowTitle('Simple')
    # w.show()
    wd = Example()
    # print(wd.close())

    sys.exit(app.exec())
    