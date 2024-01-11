from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyupbit
import time

class Worker(QThread):
    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker

    def run(self):
        while True:
            price = pyupbit.get_current_price(self.ticker)
            print(price)
            time.sleep(1)

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w0 = Worker('KRW-BTC')
        self.w0.start()

        self.w1 = Worker('KRW-XRP')
        self.w1.start()

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
