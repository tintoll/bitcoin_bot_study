from PyQt5.QtWidgets import *

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel('ID', self)
        label.setGeometry(10,10,30,40)

        lineEdit = QLineEdit(self)
        lineEdit.setGeometry(40,10,250,40)

        textEdit = QTextEdit(self)
        textEdit.setGeometry(10, 60, 280, 200)
        textEdit.setText("안녕하세요\n반갑습니다.")
        textEdit.append("다음줄에 추가되네요.")

        self.resize(320,280)


if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()