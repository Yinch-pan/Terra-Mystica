import os.path
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR=os.path.dirname(BASE_DIR)

class Favor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        favor_layout=QGridLayout()
        self.setLayout(favor_layout)
        favor_layout.setSpacing(0)
        self.setFixedSize(660,1000)

        cult_board = QLabel(self)
        cult_board_pic = QPixmap(os.path.join(BASE_DIR,'images','cult_board.jpg'))
        cult_board.setScaledContents(True)
        cult_board.setPixmap(cult_board_pic)
        favor_layout.addWidget(cult_board)
