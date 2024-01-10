from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit
class MyWidgetSet(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("ui/16-3-widget.ui", self)
        self.btn.clicked.connect(self.click_btn)
    def click_btn(self):
        price = pyupbit.get_current_price('KRW-BTC')
        self.price.setText(str(price))