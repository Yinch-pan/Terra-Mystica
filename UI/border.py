import os.path
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QDesktopWidget, QLabel
import grid


BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR=os.path.dirname(BASE_DIR)

class Border(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

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
        border_layout.addWidget(background_board,0,0,440,640)

        for i in range(22):
            colored_label = QLabel()
            if i%2:    colored_label.setStyleSheet("background-color: red; color: white;")
            else:    colored_label.setStyleSheet("background-color: blue; color: white;")

            border_layout.addWidget(colored_label, 20*i,620, 20, 20)

        for i in range(6,22):
            colored_label = QLabel()
            if i%2:    colored_label.setStyleSheet("background-color: red; color: white;")
            else:    colored_label.setStyleSheet("background-color: blue; color: white;")

            border_layout.addWidget(colored_label, 20*i,0, 20, 20)

        for i in range(32):
            colored_label = QLabel()
            if i%2:    colored_label.setStyleSheet("background-color: red; color: white;")
            else:    colored_label.setStyleSheet("background-color: blue; color: white;")

            border_layout.addWidget(colored_label,420,20*i, 20, 20)

        for i in range(6,32):
            colored_label = QLabel()
            if i%2:    colored_label.setStyleSheet("background-color: red; color: white;")
            else:    colored_label.setStyleSheet("background-color: blue; color: white;")

            border_layout.addWidget(colored_label,0,20*i, 20, 20)

        colored_label = QLabel()
        colored_label.setStyleSheet("background-color: red; color: white;")
        border_layout.addWidget(colored_label, 180, 20, 40, 70)

        colored_label = QLabel()
        colored_label.setStyleSheet("background-color: blue; color: white;")
        border_layout.addWidget(colored_label, 22, 2, 4, 7)

        colored_label = QLabel()
        colored_label.setStyleSheet("background-color: red; color: white;")
        border_layout.addWidget(colored_label, 26, 2, 4, 7)

        colored_label = QLabel()
        colored_label.setStyleSheet("background-color: blue; color: white;")
        border_layout.addWidget(colored_label, 30, 2, 4, 7)

        colored_label = QLabel()
        colored_label.setStyleSheet("background-color: red; color: white;")
        border_layout.addWidget(colored_label, 34, 2, 4, 7)

        colored_label = QLabel()
        colored_label.setStyleSheet("background-color: blue; color: white;")
        border_layout.addWidget(colored_label, 38, 2, 4, 7)

        colored_label = QLabel()
        colored_label.setStyleSheet("background-color: blue; color: white;")
        border_layout.addWidget(colored_label, 380, 130, 30, 30)

