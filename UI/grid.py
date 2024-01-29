import os.path
import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QApplication, QScrollArea, QDesktopWidget
import map


BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR=os.path.dirname(BASE_DIR)

class Grid(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        map_area = map.map_area(self, map_name='map12.txt')
        self.main_layout.setSpacing(0)
        self.main_layout.addWidget(map_area, 0, 0)



        cult_board = QLabel(self)
        cult_board_pic = QPixmap(BASE_DIR+'\\images\\cult_board.jpg')
        cult_board.setScaledContents(True)
        cult_board.setPixmap(cult_board_pic)
        self.main_layout.addWidget(cult_board, 0, 20, 20, 10)

        function1 = QLabel(self)
        function1_pic = QPixmap(BASE_DIR+'\\images\\functions\\base\\black\\Darklings.jpg')
        function1_pic = function1_pic.scaledToHeight(function1_pic.height() // 2)
        function1.setScaledContents(True)
        function1.setPixmap(function1_pic)
        self.main_layout.addWidget(function1, 20, 0, 4, 15)

        # function2 = QLabel(self)
        # function2_pic = QPixmap(BASE_DIR+'\\images\\functions\\base\\black\\Darklings.jpg')
        # function2_pic = function2_pic.scaledToHeight(function2_pic.height() // 2)
        # function2.setScaledContents(True)
        # function2.setPixmap(function2_pic)
        # main_layout.addWidget(function2, 20, 16, 10, 15)

        # scroll_area.setVerticalScrollBarPolicy(0x2)  # 始终显示垂直滚动条
    def moved(self):
        self.move(self.grid_pos)

    def mousePressEvent(self,event):
        self.grid_pos = self.pos()
        self.pressed_pos =event.globalPos()
        # if event.buttons==Qt.RightButton:

        if event.buttons==Qt.LeftButton:
            event.ignore()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.RightButton:
            global_pos = event.globalPos()
            pos=self.grid_pos - (self.pressed_pos - global_pos)
            self.move(pos)
            # self.setGeometry(pos.x(),pos.y(),self.width(),self.height())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec_())
