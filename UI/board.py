import os.path
import sys
import map
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QLabel, QPushButton
import border

BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR=os.path.dirname(BASE_DIR)

class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(1550,1000)
        self.board_layout=QGridLayout()
        self.board_layout.setSpacing(0)

        background_board=border.Border()
        background_board.lower()
        self.board_layout.addWidget(background_board, 0,0,30,50)









        map_area = map.map_area(map_name='map_txt.txt')
        self.board_layout.addWidget(map_area, 3, 11,21,35)






        self.setLayout(self.board_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Board()
    sys.exit(app.exec_())
