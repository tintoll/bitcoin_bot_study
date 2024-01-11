from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit
import time

class Worker(QThread):
    currPrice = pyqtSignal(float)
    diffPrice = pyqtSignal(str)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker

    def run(self):
        prev = None
        while True:
            price = pyupbit.get_current_price(self.ticker)
            self.currPrice.emit(price)

            if prev != None:
                if prev > price:
                    self.diffPrice.emit('Up')
                else:
                    self.diffPrice.emit('Down')

            prev = price
            time.sleep(1)

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label1 = QLabel('1000', self)
        self.label1_diff = QLabel('-', self)
        self.label1_diff.move(100, 0)

        self.label2 = QLabel('1000', self)
        self.label2.move(0, 40)
        self.label2_diff = QLabel('-', self)
        self.label2_diff.move(100, 40)

        self.w0 = Worker('KRW-BTC')
        self.w0.start()
        self.w0.currPrice.connect(self.btcPrice)
        self.w0.diffPrice.connect(self.btcDiff)

        self.w1 = Worker('KRW-XRP')
        self.w1.start()
        self.w1.currPrice.connect(self.xrpPrice)
        self.w1.diffPrice.connect(self.xrpDiff)
    def btcDiff(self, value):
        self.label1_diff.setText(value)
    def xrpDiff(self, value):
        self.label2_diff.setText(value)
    def btcPrice(self, value):
        self.label1.setText(str(value))
    def xrpPrice(self, value):
        self.label2.setText(str(value))

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
