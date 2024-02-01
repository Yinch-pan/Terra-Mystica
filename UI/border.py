import os.path
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QDesktopWidget, QLabel
import tokens


BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR=os.path.dirname(BASE_DIR)

class Border(QWidget):
    def __init__(self):
        super().__init__()
        self.scores=[None]*105
        self.initUI()

        # for i in range(1,101):
        #     self.scores[i].set_p(1)


    def initUI(self):
        border_layout=QGridLayout()
        self.setLayout(border_layout)
        border_layout.setSpacing(0)


        Q1=QLabel()
        Q1.setStyleSheet("background-color: red; color: white;")

        background_board = QLabel()
        background_board.setScaledContents(True)
        background_pic = QPixmap(os.path.join(BASE_DIR, 'images', 'maps', 'board_all.png'))
        background_pic = background_pic.scaled(int(background_pic.width() * 0.25), int(background_pic.height() * 0.25))
        background_board.setPixmap(background_pic)
        f=2
        border_layout.addWidget(background_board,1,1,44*f,64*f)

        for i in range(22):
            token_space = tokens.Token()
            self.scores[49+ i] = token_space
            border_layout.addWidget(token_space, 2*f*i,62*f, 2*f, 2*f)

        for i in range(6,22):
            token_space = tokens.Token()
            self.scores[22-i]=token_space
            border_layout.addWidget(token_space, 2*f*i,0, 2*f, 2*f)

        for i in range(1,31):
            token_space = tokens.Token()
            self.scores[101-i] = token_space
            border_layout.addWidget(token_space,42*f,2*f*i, 2*f, 2*f)

        for i in range(6,31):
            token_space = tokens.Token()
            self.scores[18+i] = token_space
            border_layout.addWidget(token_space,0,2*f*i, 2*f, 2*f)


        token_space = tokens.Token()
        self.scores[20] = token_space
        border_layout.addWidget(token_space, 0*f, 0*f+1, 4*f, 4*f)

        token_space = tokens.Token()
        self.scores[19] = token_space
        border_layout.addWidget(token_space, 4*f, 0*f, 3*f, 3*f)


        token_space = tokens.Token()
        self.scores[18] = token_space
        border_layout.addWidget(token_space, 7*f, 0*f, 2*f+1, 2*f+1)

        token_space = tokens.Token()
        self.scores[17] = token_space
        border_layout.addWidget(token_space, 9*f+1, 0*f, 2*f+1, 2*f+1)

        token_space = tokens.Token()
        self.scores[21] = token_space
        border_layout.addWidget(token_space, 0*f, 4*f, 3*f, 3*f)


        token_space = tokens.Token()
        self.scores[22] = token_space
        border_layout.addWidget(token_space, 0*f, 7*f, 2*f+1, 2*f+1)

        token_space = tokens.Token()
        self.scores[23] = token_space
        border_layout.addWidget(token_space, 0*f, 9*f+1, 2*f+1, 2*f+1)








        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: red; color: white;")
        # border_layout.addWidget(token_space, 18*f, 2*f, 4*f, 7*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: blue; color: white;")
        # border_layout.addWidget(token_space, 22*f, 2*f, 4*f, 7*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: red; color: white;")
        # border_layout.addWidget(token_space, 26*f, 2*f, 4*f, 7*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: blue; color: white;")
        # border_layout.addWidget(token_space, 30*f, 2*f, 4*f, 7*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: red; color: white;")
        # border_layout.addWidget(token_space, 34*f, 2*f, 4*f, 7*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: blue; color: white;")
        # border_layout.addWidget(token_space, 38*f, 2*f, 4*f, 7*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: blue; color: white;")
        # border_layout.addWidget(token_space, 38*f+1, 13*f+1, 3*f, 3*f)
        #
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: blue; color: white;")
        # border_layout.addWidget(token_space, 38*f+1, 22*f, 3*f, 3*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: blue; color: white;")
        # border_layout.addWidget(token_space, 38*f+1, 31*f, 3*f, 3*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: blue; color: white;")
        # border_layout.addWidget(token_space, 38*f+1, 40*f, 3*f, 3*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: blue; color: white;")
        # border_layout.addWidget(token_space, 38*f+1, 49*f-1, 3*f, 3*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: blue; color: white;")
        # border_layout.addWidget(token_space, 38*f+1, 58*f-1, 3*f, 3*f)
        #
        # token_space = QLabel()
        # token_space.setStyleSheet("background-color: blue; color: white;")
        # border_layout.addWidget(token_space, 3*f,2*f, 8*f, 7*f)

