from PyQt5.QtWidgets import *
from PyQt5 import uic
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main_window.ui", self)
        self.lineEdit.setText('안녕하세요.')
        self.pushButton.clicked.connect(self.click)
        self.clickFlag = False
    def click(self):
        if self.clickFlag == True:
            self.pushButton.setText("클릭됨.")
            self.clickFlag = False
        else:
            self.pushButton.setText('버튼!!')
            self.clickFlag = True

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
