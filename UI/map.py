import os
import sys

from PyQt5.QtWidgets import QWidget, QGridLayout
import piece

BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR=os.path.dirname(BASE_DIR)

class map_area(QWidget):
    def __init__(self, parent=None,map_name='map_txt.txt'):
        super().__init__(parent)
        self.read_map(map_name)
        self.initUI()

    def read_map(self, map_name):
        map_file_path = os.path.join(BASE_DIR,"images\\maps")
        map_file_path = os.path.join(map_file_path,map_name)

        with open(map_file_path) as mp:
            area = mp.read().split()
        self.area = [i.split(',') for i in area]


    def initUI(self):
        map_area = QGridLayout()
        Nc = 48+1
        Nr = 27
        area = [[None for i in range(14)] for j in range(10)]
        map_area.setSpacing(0)

        color = {"G": 0, "Y": 1, "B": 2, "U": 3, "R": 4, "K": 5, "S": 6, "I": 7}

        nx=-1
        for i in range(0, Nr,3):
            nx+=1
            ny=-1
            river=0
            for j in range(0, Nc, 2):
                if (i % 6 == 0 and j % 4 == 0) or (i % 6 == 3 and j % 4 == 2 and j != Nc - 2):
                    col = color[self.area[i // 3][j // 4]]
                    if col == 7:
                        river+=1
                        col=-1
                    ny+=1
                    area[nx][ny]=piece.Piece(col,nx,ny,river)
                    # area[nx][ny].setScaledContents(True)
                    map_area.addWidget(area[nx][ny], i, j, 4, 4)
        map_area.setSpacing(0)

        self.setLayout(map_area)
