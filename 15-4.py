from PyQt5.QtWidgets import *

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("1", self)
        btn1.move(30,30)
        btn1.resize(100,30)
        btn1.clicked.connect(self.click)

        btn2 = QPushButton("2", self)
        btn2.move(130, 30)
        btn2.resize(100, 30)
        btn2.clicked.connect(self.click)

        btn3 = QPushButton("3", self)
        btn3.move(30, 60)
        btn3.resize(100, 30)
        btn3.clicked.connect(self.click)

        btn4 = QPushButton("4", self)
        btn4.move(130, 60)
        btn4.resize(100, 30)
        btn4.clicked.connect(self.click)

        self.resize(260,120)
    def click(self):
        b = self.sender()
        print(b.text())



if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()