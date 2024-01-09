from PyQt5.QtWidgets import *

app = QApplication([])

label = QLabel("Hello PyQt")
label.show()

# 이벤트 루프 활성화 (종료되지 않도록)
app.exec_()