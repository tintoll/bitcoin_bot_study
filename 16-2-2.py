from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/16-2-2.ui", self)
        self.b1.clicked.connect(self.b1_click)
        self.b2.clicked.connect(self.b2_click)
        self.b3.clicked.connect(self.b3_click)

    def b1_click(self):
        price = pyupbit.get_current_price('KRW-BTC')
        self.l0.setText(str(price))
    def b2_click(self):
        price = pyupbit.get_current_price('KRW-BTT')
        self.l1.setText(str(price))

    def b3_click(self):
        price = pyupbit.get_current_price('KRW-XRP')
        self.l2.setText(str(price))


if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()