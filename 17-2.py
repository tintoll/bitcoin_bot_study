from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("1000", self)

        timer = QTimer(self)
        timer.start(1000) # 1초 한번
        timer.timeout.connect(self.func)
    def func(self):
        price = pyupbit.get_current_price("KRW-BTC")
        self.label.setText(str(price))


if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
