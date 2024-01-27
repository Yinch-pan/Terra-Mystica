import os
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import piece

BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR=os.path.dirname(BASE_DIR)

class map_area(QWidget):
    def __init__(self, parent=None,map_name='map12.txt'):
        super().__init__(parent)
        self.read_map(map_name)
        self.initUI()


    def read_map(self, map_name):
        map_file_path = os.path.join(BASE_DIR,"images\\maps")
        # map_name = 'map12.txt'
        map_file_path = os.path.join(map_file_path,map_name)


        with open(map_file_path) as mp:
            area = mp.read().split()
        self.area = [i.split(',') for i in area]

    def initUI(self):
        map_area = QGridLayout()
        Nc = 48
        Nr = 27
        area = [[piece.Piece(0) for i in range(Nc)] for j in range(Nr)]
        map_area.setSpacing(0)
        # image_path = BASE_DIR+'/images/terrains_hexes.png'  # 替换为你的图片路径
        # full_pixmap = QPixmap(image_path)

        color = {"S": 0, "R": 1, "Y": 2, "U": 3, "K": 4, "B": 5, "G": 6, "I": 7}

        # pixmap = []
        # for i in range(7):
        #     tmp_pic = full_pixmap.copy(i * 137, 0, 136, full_pixmap.height())
        #     tmp_pic = tmp_pic.scaled(tmp_pic.height()//2, tmp_pic.width())
        #     pixmap.append(tmp_pic)

        for i in range(0, Nr):
            for j in range(0, Nc, 2):
                if (i % 6 == 0 and j % 4 == 0) or (i % 6 == 3 and j % 4 == 2 and j != Nc - 2):
                    col = color[self.area[i // 3][j // 4]]
                    if col != 7:
                        area[i][j]=piece.Piece(col)
                        # area[i][j].setScaledContents(True)
                        # area[i][j].setPixmap(pixmap[col])

                        # area[i][j].setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    # a=QWidget()
                    # a.setStyleSheet('background-color: red;')
                    # map_area.addWidget(a,i,j,4,4)
                    map_area.addWidget(area[i][j], i, j, 4, 4)
        map_area.setSpacing(0)

        self.setLayout(map_area)
