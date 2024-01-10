from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/16-2-1.ui", self)
        self.loginButton.clicked.connect(self.login_click)

    def login_click(self):
        access = self.input1.text()
        secret = self.input2.text()
        upbit = pyupbit.Upbit(access, secret)
        krw = upbit.get_balance('KRW')
        self.log.setText(str(krw))


if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()