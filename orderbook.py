import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pybithumb
from PyQt5 import uic
import time

class OrderbookWorker(QThread):
    # 시그널을 만들면서 보내줄 데이터로 dict 형태로 지정
    dataReceive = pyqtSignal(dict)
    def run(self):
        while True:
            data = pybithumb.get_orderbook('BTC', limit=10)
            self.dataReceive.emit(data) # 데이터를 메인쓰레드로 넘겨준다.
            time.sleep(0.2)

class OrderbookWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/orderbook.ui", self)

        # Worker 생성
        self.ow = OrderbookWorker()
        # 워커 스레드에서 넘어오는 데이터를 넘겨줄 함수를 지정해준다.
        self.ow.dataReceive.connect(self.updateOrderbook)
        self.ow.start()
    def updateOrderbook(self, param):
        for i in range(10):
            item = param['asks'][9 - i]
            value = item['price'] * item['quantity']
            d = QTableWidgetItem(str(item['price']))
            self.askTable.setItem(i, 0, d)
            d = QTableWidgetItem(str(item['quantity']))
            self.askTable.setItem(i, 1, d)
            d = QTableWidgetItem(str(value))
            self.askTable.setItem(i, 2, d)

            item = param['bids'][i]
            value = item['price'] * item['quantity']
            d = QTableWidgetItem(str(item['price']))
            self.bidTable.setItem(i, 0, d)
            d = QTableWidgetItem(str(item['quantity']))
            self.bidTable.setItem(i, 1, d)
            d = QTableWidgetItem(str(value))
            self.bidTable.setItem(i, 2, d)


if __name__ == "__main__":
    app = QApplication([])
    orderbookWidget = OrderbookWidget()
    orderbookWidget.show()
    app.exec_()