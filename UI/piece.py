import os
import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

BASE_PATH = os.path.realpath(sys.argv[0])
while not BASE_PATH.endswith('Terra-Mystica'):
    BASE_PATH = os.path.dirname(BASE_PATH)


class Piece(QWidget):
    def __init__(self,col):
        super().__init__()
        self.col=col
        self.init_ui()

    def init_ui(self):
        # self.setGeometry(500,500,100,100)
        self.Grid = QGridLayout()  # 建立网格布局
        self.Grid.setSpacing(0)
        self.Grid.setContentsMargins(0, 0, 0, 0)


        # 7个地形的图片路径
        image_path = os.path.join(BASE_PATH, 'images', 'terrains_hexes.png')
        full_pixmap = QPixmap(image_path)
        seven_shapes = []
        for i in range(7):
            tmp_pic = full_pixmap.copy(i * 137, 0, 136, full_pixmap.height())
            tmp_pic = tmp_pic.scaled(int(tmp_pic.height()//1.2), tmp_pic.width())
            seven_shapes.append(tmp_pic)

        # 添加背景地形
        background = QLabel()
        background.setScaledContents(True)
        background.setPixmap(seven_shapes[self.col])
        background.setScaledContents(True)
        self.Grid.addWidget(background, 0, 0, 20, 20)
        self.change_ground(random.randint(0,8))
        self.setLayout(self.Grid)


    def change_ground(self,col):
        # 9个转换地形图片
        image_path = os.path.join(BASE_PATH, 'images', 'terrain_tiles.png')
        full_pixmap = QPixmap(image_path)
        nine_change_shapes = []
        for i in range(9):
            tmp_pic = full_pixmap.copy(i * 128, 0, 128, full_pixmap.height())
            # tmp_pic = tmp_pic.scaled(int(tmp_pic.height()/1.5), int(tmp_pic.width()/1.5))
            nine_change_shapes.append(tmp_pic)

        change_shape = QLabel()
        change_shape.setScaledContents(True)
        change_shape.setPixmap(nine_change_shapes[col])
        # change_shape.raise_()
        change_shape.setScaledContents(True)
        self.Grid.addWidget(change_shape, 2,2, 16, 16)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    Piece = Piece()
    Piece.show()
    sys.exit(app.exec_())
