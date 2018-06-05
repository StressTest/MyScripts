import sys
from PyQt5.QtWidgets import  QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    #w.resize(250, 150)
    w.move(1200, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec())