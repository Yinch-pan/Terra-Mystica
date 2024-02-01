import os.path
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
import tokens

BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR = os.path.dirname(BASE_DIR)


class Favor(QWidget):
    def __init__(self):
        super().__init__()
        self.p_all = [[] for _ in range(4)]
        self.favor_scores_all = [[] for _ in range(4)]
        self.initUI()

    def initUI(self):
        favor_layout = QGridLayout()
        self.setLayout(favor_layout)
        favor_layout.setSpacing(0)
        self.setFixedSize(660, 1000)

        cult_board = QLabel(self)
        cult_board_pic = QPixmap(os.path.join(BASE_DIR, 'images', 'cult_board.jpg'))
        cult_board.setScaledContents(True)
        cult_board.setPixmap(cult_board_pic)
        favor_layout.addWidget(cult_board, 0, 0, 40, 60)


        for k in range(4):
            for i in range(2):
                for j in range(2):
                    pos_p = tokens.Token()
                    self.p_all[k].append(pos_p)
                    pos_p.set_p(1)
                    favor_layout.addWidget(pos_p, 32 + 3 * i,
                                            j * 8 + 15 * k - (1 if k == 3 else 0) + (1 if k == 0 else 0), 2, 2)



        post=[30,26, 24, 20, 18, 15, 13, 10, 8, 6, 1]
        for k in range(4):
            for i in range(11):
                pos_fs = tokens.Token()
                self.favor_scores_all[k].append(pos_fs)
                pos_fs.set_token(1)
                favor_layout.addWidget(pos_fs,post[i],6+14*k,2,2)

        #
        # fire_p = QLabel()
        # fire_p.setStyleSheet("background-color: red; color: white;")
        # favor_layout.addWidget(fire_p, 16,1,1,1)
