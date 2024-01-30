import os.path
import sys
import map
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QLabel, QPushButton

BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR=os.path.dirname(BASE_DIR)

class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.board_layout=QGridLayout()


        background_board = QLabel()
        background_board.setScaledContents(True)
        background_pic=QPixmap(os.path.join(BASE_DIR, 'images', 'maps', 'board_all.png'))
        background_pic = background_pic.scaled(int(background_pic.width()*0.25), int(background_pic.height()*0.25))
        background_board.setPixmap(background_pic)
        background_board.lower()
        self.board_layout.addWidget(background_board, 0,0,30,50)

        # test = QPushButton()
        # self.board_layout.addWidget(test,0,0)

        map_area = map.map_area(map_name='map_txt.txt')
        self.board_layout.addWidget(map_area, 3, 11,21,35)


        # self.background_board.stackUnder(self.map_area)
        # self.map_area.stackUnder(self.background_board)



        self.setLayout(self.board_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Board()
    sys.exit(app.exec_())
