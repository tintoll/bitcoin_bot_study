from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit
import time

class Worker(QThread):
    currPrice = pyqtSignal(float)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker

    def run(self):
        while True:
            price = pyupbit.get_current_price(self.ticker)
            self.currPrice.emit(price)
            time.sleep(1)

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label1 = QLabel('1000', self)
        self.label2 = QLabel('1000', self)
        self.label2.move(0, 40)

        self.w0 = Worker('KRW-BTC')
        self.w0.start()
        self.w0.currPrice.connect(self.btcPrice)

        self.w1 = Worker('KRW-XRP')
        self.w1.start()
        self.w1.currPrice.connect(self.xrpPrice)
    def btcPrice(self, value):
        self.label1.setText(str(value))
    def xrpPrice(self, value):
        self.label2.setText(str(value))

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
