import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

BASE_PATH= os.path.realpath(sys.argv[0])
while not BASE_PATH.endswith('Terra-Mystica'):
    BASE_PATH=os.path.dirname(BASE_PATH)


class Piece(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(500,500,100,100)
        Grid=QGridLayout()# 建立网格布局

        # 7个地形的图片路径
        image_path = os.path.join(BASE_PATH,'images','terrains_hexes.png')

        full_pixmap=QPixmap(image_path)
        seven_shapes = []
        for i in range(7):
            tmp_pic = full_pixmap.copy(i * 137, 0, 136, full_pixmap.height())
            tmp_pic = tmp_pic.scaled(tmp_pic.height()//2, tmp_pic.width())
            # tmp_pic=tmp_pic.scaledToWidth(tmp_pic.width()//2)
            # tmp_pic=tmp_pic.scaledToHeight(tmp_pic.height()//2)
            seven_shapes.append(tmp_pic)



        background=QLabel()
        background.setScaledContents(True)
        background.setPixmap(seven_shapes[0])

        Grid.addWidget(background,0,0,5,5)

        self.setLayout(Grid)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Piece = Piece()
    Piece.show()
    sys.exit(app.exec_())
