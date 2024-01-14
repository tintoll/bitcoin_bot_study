from pybithumb import WebSocketManager
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Worker(QThread):
    receiveData = pyqtSignal(dict)

    def run(self):
        wm = WebSocketManager("ticker", ["BTC_KRW"])
        self.alive = True

        while self.alive:
            data = wm.get()
            self.receiveData.emit(data)
        wm.terminate()

    # 메인프로세스가 죽어도 워커가 죽지 않아 조건값을 줌.
    def end(self):
        self.alive = False


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w = Worker()
        self.w.receiveData.connect(self.processData)
        self.w.start()

    # 윈도우가 종료 되는 기본 이벤트
    def closeEvent(self, event):
        self.w.end()

    def processData(self, data):
        print(data)

if __name__ == "__main__":
    app = QApplication([])
    m = MyWindow()
    m.show()
    app.exec_()
