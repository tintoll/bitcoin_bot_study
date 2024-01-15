from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtChart import *
from PyQt5.QtGui import *

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/19_chart.ui", self)

        # 1) 데이터 추가
        self.priceData = QLineSeries()
        self.priceData.append(0, 10)
        self.priceData.append(1, 20)
        self.priceData.append(2, 10)

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