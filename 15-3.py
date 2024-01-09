from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 윈도우 사이즈 지정
        self.resize(400, 300)
        # 초기 생성위치 지정
        self.move(300,300)
        # 타이틀 변경
        self.setWindowTitle('자동매매')
        # 아이콘 추가
        self.setWindowIcon(QIcon('stock.png'))

app = QApplication([])
window = MyWindow()
window.show()

app.exec_()