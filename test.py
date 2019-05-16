import sys
from Simple import Ui_mainWindow
from PyQt5.QtWidgets import QApplication , QMainWindow

class Mainwindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)

test = QApplication(sys.argv)
w = Mainwindow()
w.show()
sys.exit(test.exec_())