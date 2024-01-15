from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtChart import *
from PyQt5.QtGui import *
import pybithumb

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/19_chart.ui", self)

        # 1) 데이터 추가
        self.priceData = QLineSeries()

        df = pybithumb.get_ohlcv("BTC")
        print(df.loc["2023", "close"])
        for i in range(len(df.loc["2023", "close"])):
            self.priceData.append(i, df.loc["2023", "close"][i])

        # 2) 도화지 연결
        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)
        self.priceChart.legend().hide()
        self.priceChart.layout().setContentsMargins(0, 0, 0, 0)

        # 3) 위젯에 출력
        self.priceView.setChart(self.priceChart)
        self.priceView.setRenderHints(QPainter.Antialiasing)


if __name__ == "__main__":
    app = QApplication([])
    m = ChartWidget()
    m.show()
    app.exec_()