import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn = QRadioButton("Name", self)
        self.resize(250, 150)
        self.setWindowTitle("ups")

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # w = QWidget()
    # #w.resize(250, 150)
    # w.move(1200, 300)
    # w.setWindowTitle('Simple')
    # w.show()
    wd = Example()
    sys.exit(app.exec())