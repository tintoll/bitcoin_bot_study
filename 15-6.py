from PyQt5.QtWidgets import *
import pyupbit

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        table = QTableWidget(self)
        table.resize(250, 180)
        table.setColumnCount(2)
        table.setRowCount(5)
        table.setHorizontalHeaderLabels(["금액", "잔고"])
        # table.setVerticalHeaderLabels(["a","b","c","d","e"])
        table.verticalHeader().setVisible(False)
        # 호가창 정보 불러와서 매도호가 5개 표현하기
        data = pyupbit.get_orderbook("KRW-BTC")
        for i in range(5):
            # string만들어가기 때문 str로 변환해줘야 한다.
            d = QTableWidgetItem(str(data['orderbook_units'][4 - i]['ask_price']))
            table.setItem(i, 0, d)

            d = QTableWidgetItem(str(data['orderbook_units'][4 - i]['ask_size']))
            table.setItem(i, 1, d)

        self.resize(250, 180)


if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
