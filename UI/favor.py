import os.path
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QDesktopWidget
import grid


BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR=os.path.dirname(BASE_DIR)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        ...

