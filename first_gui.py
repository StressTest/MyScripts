import sys
import first_form
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, QBasicTimer


# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#
#     def init_ui(self):
#         btn = QPushButton("Start/Stop", self)
#         btn.resize(btn.sizeHint())
#         btn.move(150 - btn.size().width()//2, 25)
#         # btn.clicked.connect(QCoreApplication.instance().quit)
#         # btn.pressed()
#         self.resize(300, 150)
#         self.setWindowTitle("First Gui App")
#
#         self.show()

class Example(QWidget, first_form.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dsec.display("00")
        self.sec.display("00")
        self.min.display("0")
        self.tmr = QBasicTimer()
        # self.start_stop_btn.clicked.connect(self.inc_lcd)
        self.start_stop_btn.clicked.connect(self.clock)
        self.lap_reset_btn.clicked.connect(self.reset)
        self.show()

    # def inc_lcd(self):
    #     self.lcdDisplay.display(self.lcdDisplay.intValue() + 1)

    def timerEvent(self, e):
        self.dsec.display("{:02d}".format(self.dsec.intValue() + 1))
        if self.dsec.intValue() >= 100:
            self.dsec.display(0)
            self.sec.display("{:02d}".format(self.sec.intValue() + 1))
            if self.sec.intValue() >= 60:
                self.sec.display(0)
                self.min.display(self.min.intValue() + 1)

        # self.inc_lcd()
    def reset(self):
        if not self.tmr.isActive():
            self.tmr.stop()
            self.dsec.display("00")
            self.sec.display("00")
            self.min.display("0")
        else:
            self.listWidget.addItem("{:3d} : {:02d} : {:02d}".format(self.min.intValue(), self.sec.intValue(), self.dsec.intValue()))



    def clock(self):
        print(self.tmr.isActive())
        # self.tmr.start(1000, self)
        if self.tmr.isActive():
            self.tmr.stop()
            print('stop')
        else:
            self.tmr.start(10, self)



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
    