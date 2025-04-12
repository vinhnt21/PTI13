from PyQt6 import uic
from PyQt6.QtWidgets import *


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)


app = QApplication([])



window = MainApp()
window.show()

app.exec()
