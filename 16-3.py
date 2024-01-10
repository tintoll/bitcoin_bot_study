from PyQt5.QtWidgets import *
from mywidgetset import MyWidgetSet
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        w0 = MyWidgetSet(self)
        w1 = MyWidgetSet(self)
        w1.move(0, 50)
        w2 = MyWidgetSet(self)
        w2.move(0, 100)

        self.resize(400,200)

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()