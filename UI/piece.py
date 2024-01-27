import os
import random
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

BASE_PATH = os.path.realpath(sys.argv[0])
while not BASE_PATH.endswith('Terra-Mystica'):
    BASE_PATH = os.path.dirname(BASE_PATH)


class Piece(QWidget):
    def __init__(self, col):
        super().__init__()
        self.col = col
        self.size_factor = 1.2
        self.stu = None
        self.init_ui()

    def init_ui(self):
        self.Grid = QGridLayout()  # 建立网格布局
        self.Grid.setSpacing(0)
        self.Grid.setContentsMargins(0, 0, 0, 0)
        self.build_background()
        self.setLayout(self.Grid)

    def build_background(self):
        # 7个地形的图片路径
        image_path = os.path.join(BASE_PATH, 'images', 'terrains_hexes.png')
        full_pixmap = QPixmap(image_path)
        seven_shapes = []
        for i in range(7):
            tmp_pic = full_pixmap.copy(i * 137, 0, 136, full_pixmap.height())
            tmp_pic = tmp_pic.scaled(int(tmp_pic.width() / self.size_factor), int(tmp_pic.height() / self.size_factor))
            seven_shapes.append(tmp_pic)

        # 添加背景地形
        background = QLabel()
        # background.setScaledContents(True)
        background.setPixmap(seven_shapes[self.col])
        self.Grid.addWidget(background, 0, 0, 20, 20)

        # self.change_ground(random.randint(0,0))
        # self.build_landscape(random.randint(0,18))
        # self.build_sh()
        # self.build_tp()
        # self.build_d()



    def change_ground(self, col):
        # 9个转换地形图片
        image_path = os.path.join(BASE_PATH, 'images', 'terrain_tiles.png')
        full_pixmap = QPixmap(image_path)
        nine_change_shapes = []
        for i in range(9):
            tmp_pic = full_pixmap.copy(i * 128, 0, 128, full_pixmap.height())
            tmp_pic = tmp_pic.scaled(int(tmp_pic.width() / self.size_factor), int(tmp_pic.height() / self.size_factor))
            nine_change_shapes.append(tmp_pic)

        change_shape = QLabel()
        # change_shape.setScaledContents(True)
        change_shape.setPixmap(nine_change_shapes[col])
        self.Grid.addWidget(change_shape, 0, 0, 16, 16)

    def build_d(self):
        self.stu = 'd'
        image_path = os.path.join(BASE_PATH, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_d_all = []
        for i in range(9):
            tmp_pic = full_pixmap.copy(i * 140, 0, 140, 140)
            tmp_pic = tmp_pic.scaled(int(tmp_pic.width() / self.size_factor / 1.5),
                                     int(tmp_pic.height() / self.size_factor / 1.5))
            stu_d_all.append(tmp_pic)

        self.stu_d = QLabel()
        # self.stu_d.setScaledContents(True)
        self.stu_d.setPixmap(stu_d_all[self.col])
        self.Grid.addWidget(self.stu_d,10, 10, 1, 1)

    def build_tp(self):
        self.stu = 'tp'
        self.stu_d.deleteLater()
        image_path = os.path.join(BASE_PATH, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_tp_all = []
        for i in range(9):
            tmp_pic = full_pixmap.copy(i * 140, 160, 140, 140)
            tmp_pic = tmp_pic.scaled(int(tmp_pic.width() / self.size_factor / 1.5),
                                     int(tmp_pic.height() / self.size_factor / 1.5))
            stu_tp_all.append(tmp_pic)

        self.stu_tp = QLabel()
        # self.stu_tp.setScaledContents(True)
        self.stu_tp.setPixmap(stu_tp_all[self.col])
        self.Grid.addWidget(self.stu_tp, 10, 10, 1, 1)

    def build_te(self):
        self.stu = 'te'
        self.stu_tp.deleteLater()
        image_path = os.path.join(BASE_PATH, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_te_all = []
        for i in range(9):
            tmp_pic = full_pixmap.copy(i * 140, 480, 140, 140)
            tmp_pic = tmp_pic.scaled(int(tmp_pic.width() / self.size_factor / 1.5),
                                     int(tmp_pic.height() / self.size_factor / 1.5))
            stu_te_all.append(tmp_pic)

        self.stu_te = QLabel()
        # self.stu_tp.setScaledContents(True)
        self.stu_te.setPixmap(stu_te_all[self.col])
        self.Grid.addWidget(self.stu_te, 10, 10, 1, 1)

    def build_sh(self):
        self.stu = 'sh'
        self.stu_tp.deleteLater()
        image_path = os.path.join(BASE_PATH, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_sh_all = []
        for i in range(9):
            tmp_pic = full_pixmap.copy(i * 141, 310, 140, 160)
            tmp_pic = tmp_pic.scaled(int(tmp_pic.width() / self.size_factor / 1.5),
                                     int(tmp_pic.height() / self.size_factor / 1.5))
            stu_sh_all.append(tmp_pic)

        self.stu_sh = QLabel()
        # self.stu_sh.setScaledContents(True)
        self.stu_sh.setPixmap(stu_sh_all[self.col])
        self.Grid.addWidget(self.stu_sh, 10, 10, 1, 1)

    def build_sa(self):
        self.stu = 'sa'
        self.stu_te.deleteLater()
        image_path = os.path.join(BASE_PATH, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_sa_all = []
        for i in range(9):
            tmp_pic = full_pixmap.copy(i * 141, 620, 140, 160)
            tmp_pic = tmp_pic.scaled(int(tmp_pic.width() / self.size_factor / 1.5),
                                     int(tmp_pic.height() / self.size_factor / 1.5))
            stu_sa_all.append(tmp_pic)

        self.stu_sa = QLabel()
        # self.stu_sh.setScaledContents(True)
        self.stu_sa.setPixmap(stu_sa_all[self.col])
        self.Grid.addWidget(self.stu_sa, 10, 10, 1, 1)

    def build_landscape(self):
        # 20个景观地形图片
        self.stu = 'ls'
        image_path = os.path.join(BASE_PATH, 'images', 'landscape_tiles.png')
        full_pixmap = QPixmap(image_path)
        ls_shapes = []
        for i in range(20):
            tmp_pic = full_pixmap.copy(i * 128, 0, 128, full_pixmap.height())
            tmp_pic = tmp_pic.scaled(int(tmp_pic.width() / self.size_factor),
                                     int(tmp_pic.height() / self.size_factor))
            ls_shapes.append(tmp_pic)

        self.ls_shape = QLabel()
        # change_shape.setScaledContents(True)
        self.ls_shape.setPixmap(ls_shapes[1])
        self.Grid.addWidget(self.ls_shape, 10, 10, 1, 1)

    def upgrate1(self):
        if self.stu == None: self.build_d()
        elif self.stu == 'd': self.build_tp()
        elif self.stu == 'tp': self.build_sh()

    def upgrate2(self):
        if self.stu == None: self.build_landscape()
        elif self.stu == 'd': self.build_tp()
        elif self.stu == 'tp': self.build_te()
        elif self.stu == 'te': self.build_sa()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.upgrate1()
        if event.button() == Qt.RightButton:
            self.upgrate2()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Piece = Piece(random.randint(0, 6))
    Piece.show()
    sys.exit(app.exec_())
