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
        self.size_factor = 0.8
        self.stu = None
        self.real_width = int(136 * self.size_factor)
        self.real_height = int(156 * self.size_factor)
        self.ground_size_factor = 0.9
        self.stu_size_factor = 0.7
        if col==7:
            return
        self.init_ui()
        self.colors_dict = {"green": 0, "yellow": 1, "blue": 2, "brown": 3, "red": 4, "black": 5, "gray": 6, "ice": 7,
                       "lava": 8}
        self.colors_list=["green","yellow","blue","brown","red","black","gray","ice","lava"]
        #   0      1     2    3    4    5     6   7    8
        # green,yellow,blue,brown,red,black,gray,ice,lava
        self.dis = [0, 6, 4, 1, 3, 5, 2]

    def distance_shape(self, now_shape, to_shape):
        tmp = abs(self.dis.index(now_shape) - self.dis.index(to_shape))
        return min(tmp, 7 - tmp)

    def init_ui(self):
        self.Grid = QGridLayout()  # 建立网格布局
        self.Grid.setSpacing(0)
        self.Grid.setContentsMargins(0, 0, 0, 0)
        self.build_background()
        self.setLayout(self.Grid)

    def build_background(self):
        # 7个地形
        image_path = os.path.join(BASE_PATH, 'images', 'terrains_hexes.png')
        full_pixmap = QPixmap(image_path)
        seven_shapes = []
        for i in range(7):
            org_pic = full_pixmap.copy(i * 137, 0, 136, full_pixmap.height())
            org_pic = org_pic.scaled(int(org_pic.width() * self.size_factor), int(org_pic.height() * self.size_factor))

            real_pic = QPixmap(self.real_width, self.real_height)
            real_pic.fill(QColor(Qt.transparent))  # 使用透明色填充作为背景

            painter = QPainter(real_pic)
            painter.drawPixmap((real_pic.width() - org_pic.width()) // 2, (real_pic.height() - org_pic.height()) // 2,
                               org_pic)
            painter.end()
            seven_shapes.append(real_pic)

        seven_shapes[0], seven_shapes[6] = seven_shapes[6], seven_shapes[0]
        seven_shapes[4], seven_shapes[1], seven_shapes[5], seven_shapes[2] = \
            seven_shapes[1], seven_shapes[2], seven_shapes[4], seven_shapes[5]

        # 添加背景地形
        background = QLabel()
        background.setScaledContents(True)
        background.setPixmap(seven_shapes[self.col])
        self.Grid.addWidget(background, 0, 0, 20, 20)

        # self.change_ground(random.randint(0 , 0))
        # self.build_landscape(random.randint(0,18))
        # self.build_sh()
        # self.build_tp()
        # self.build_d()

    def change_ground(self, col):
        # 9个转换地形图片
        self.col=col
        image_path = os.path.join(BASE_PATH, 'images', 'terrain_tiles.png')
        full_pixmap = QPixmap(image_path)
        transformed_shapes = []
        for i in range(9):
            org_pic = full_pixmap.copy(i * 128, 0, 128, full_pixmap.height())
            org_pic = org_pic.scaled(int(org_pic.width() * self.size_factor * self.ground_size_factor),
                                     int(org_pic.height() * self.size_factor * self.ground_size_factor))

            real_pic = QPixmap(self.real_width, self.real_height)
            real_pic.fill(QColor(Qt.transparent))  # 使用透明色填充作为背景

            painter = QPainter(real_pic)
            painter.drawPixmap((real_pic.width() - org_pic.width()) // 2, (real_pic.height() - org_pic.height()) // 2,
                               org_pic)
            painter.end()
            transformed_shapes.append(real_pic)
        transformed_shapes[0], transformed_shapes[1] = transformed_shapes[1], transformed_shapes[0]
        transformed_shapes[7], transformed_shapes[8] = transformed_shapes[8], transformed_shapes[7]
        transformed_shapes[5], transformed_shapes[4], transformed_shapes[2], transformed_shapes[6],transformed_shapes[3] = \
            transformed_shapes[2], transformed_shapes[3], transformed_shapes[4], transformed_shapes[5],transformed_shapes[6]

        change_shape = QLabel()
        change_shape.setScaledContents(True)
        change_shape.setPixmap(transformed_shapes[col])
        self.Grid.addWidget(change_shape, 0, 0, 20, 20)

    def build_d(self):
        self.stu = 'd'
        image_path = os.path.join(BASE_PATH, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_d_all = []
        for i in range(9):
            org_pic = full_pixmap.copy(i * 140, 0, 140, 140)
            org_pic = org_pic.scaled(int(org_pic.width() * self.size_factor * self.stu_size_factor),
                                     int(org_pic.height() * self.size_factor * self.stu_size_factor))

            real_pic = QPixmap(self.real_width, self.real_height)
            real_pic.fill(QColor(Qt.transparent))  # 使用透明色填充作为背景

            painter = QPainter(real_pic)
            painter.drawPixmap((real_pic.width() - org_pic.width()) // 2, (real_pic.height() - org_pic.height()) // 2,
                               org_pic)
            painter.end()
            stu_d_all.append(real_pic)

        self.stu_d = QLabel()
        self.stu_d.setScaledContents(True)
        self.stu_d.setPixmap(stu_d_all[self.col])
        self.Grid.addWidget(self.stu_d, 0, 0, 20, 20)

    def build_tp(self):
        self.stu = 'tp'
        self.stu_d.deleteLater()
        image_path = os.path.join(BASE_PATH, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_tp_all = []
        for i in range(9):
            org_pic = full_pixmap.copy(i * 140, 160, 140, 140)
            org_pic = org_pic.scaled(int(org_pic.width() * self.size_factor * self.stu_size_factor),
                                     int(org_pic.height() * self.size_factor * self.stu_size_factor))

            real_pic = QPixmap(self.real_width, self.real_height)
            real_pic.fill(QColor(Qt.transparent))  # 使用透明色填充作为背景

            painter = QPainter(real_pic)
            painter.drawPixmap((real_pic.width() - org_pic.width()) // 2, (real_pic.height() - org_pic.height()) // 2,
                               org_pic)
            painter.end()
            stu_tp_all.append(real_pic)

        self.stu_tp = QLabel()
        self.stu_tp.setScaledContents(True)
        self.stu_tp.setPixmap(stu_tp_all[self.col])
        self.Grid.addWidget(self.stu_tp, 0, 0, 20, 20)

    def build_te(self):
        self.stu = 'te'
        print(1)
        self.stu_tp.deleteLater()
        image_path = os.path.join(BASE_PATH, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_te_all = []
        for i in range(9):
            org_pic = full_pixmap.copy(i * 140, 480, 140, 140)
            org_pic = org_pic.scaled(int(org_pic.width() * self.size_factor * self.stu_size_factor),
                                     int(org_pic.height() * self.size_factor * self.stu_size_factor))

            real_pic = QPixmap(self.real_width, self.real_height)
            real_pic.fill(QColor(Qt.transparent))  # 使用透明色填充作为背景

            painter = QPainter(real_pic)
            painter.drawPixmap((real_pic.width() - org_pic.width()) // 2, (real_pic.height() - org_pic.height()) // 2,
                               org_pic)
            painter.end()
            stu_te_all.append(real_pic)

        self.stu_te = QLabel()
        self.stu_te.setScaledContents(True)
        self.stu_te.setPixmap(stu_te_all[self.col])
        self.Grid.addWidget(self.stu_te, 0, 0, 20, 20)

    def build_sh(self):
        self.stu = 'sh'
        self.stu_tp.deleteLater()
        image_path = os.path.join(BASE_PATH, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_sh_all = []
        for i in range(9):
            org_pic = full_pixmap.copy(i * 141, 310, 140, 160)
            org_pic = org_pic.scaled(int(org_pic.width() * self.size_factor * self.stu_size_factor),
                                     int(org_pic.height() * self.size_factor * self.stu_size_factor))

            real_pic = QPixmap(self.real_width, self.real_height)
            real_pic.fill(QColor(Qt.transparent))  # 使用透明色填充作为背景

            painter = QPainter(real_pic)
            painter.drawPixmap((real_pic.width() - org_pic.width()) // 2, (real_pic.height() - org_pic.height()) // 2,
                               org_pic)
            painter.end()
            stu_sh_all.append(real_pic)

        self.stu_sh = QLabel()
        self.stu_sh.setScaledContents(True)
        self.stu_sh.setPixmap(stu_sh_all[self.col])
        self.Grid.addWidget(self.stu_sh, 0, 0, 20, 20)

    def build_sa(self):
        self.stu = 'sa'
        self.stu_te.deleteLater()
        image_path = os.path.join(BASE_PATH, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_sa_all = []
        for i in range(9):
            org_pic = full_pixmap.copy(i * 141, 620, 140, 160)
            org_pic = org_pic.scaled(int(org_pic.width() * self.size_factor * self.stu_size_factor),
                                     int(org_pic.height() * self.size_factor * self.stu_size_factor))

            real_pic = QPixmap(self.real_width, self.real_height)
            real_pic.fill(QColor(Qt.transparent))  # 使用透明色填充作为背景

            painter = QPainter(real_pic)
            painter.drawPixmap((real_pic.width() - org_pic.width()) // 2, (real_pic.height() - org_pic.height()) // 2,
                               org_pic)
            painter.end()
            stu_sa_all.append(real_pic)

        self.stu_sa = QLabel()
        self.stu_sa.setScaledContents(True)
        self.stu_sa.setPixmap(stu_sa_all[self.col])
        self.Grid.addWidget(self.stu_sa, 0, 0, 20, 20)

    def build_landscape(self):
        # 20个景观地形图片
        self.stu = 'ls'
        image_path = os.path.join(BASE_PATH, 'images', 'landscape_tiles.png')
        full_pixmap = QPixmap(image_path)
        ls_shapes = []
        for i in range(20):
            org_pic = full_pixmap.copy(i * 128, 0, 128, full_pixmap.height())
            org_pic = org_pic.scaled(int(org_pic.width() * self.size_factor * self.ground_size_factor),
                                     int(org_pic.height() * self.size_factor * self.ground_size_factor))

            real_pic = QPixmap(self.real_width, self.real_height)
            real_pic.fill(QColor(Qt.transparent))  # 使用透明色填充作为背景

            painter = QPainter(real_pic)
            painter.drawPixmap((real_pic.width() - org_pic.width()) // 2, (real_pic.height() - org_pic.height()) // 2,
                               org_pic)
            painter.end()
            ls_shapes.append(real_pic)

        self.ls_shape = QLabel()
        self.ls_shape.setScaledContents(True)
        self.ls_shape.setPixmap(ls_shapes[1])
        self.Grid.addWidget(self.ls_shape, 0, 0, 20, 20)

    def upgrate1(self):
        if self.stu == None:
            self.build_d()
        elif self.stu == 'd':
            self.build_tp()
        elif self.stu == 'tp':
            self.build_sh()

    def upgrate2(self):
        if self.stu == None:
            self.build_landscape()
        elif self.stu == 'd':
            self.build_tp()
        elif self.stu == 'tp':
            self.build_te()
        elif self.stu == 'te':
            self.build_sa()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            menu = QMenu(self)
            if self.stu == 'd':
                action_upgrate1 = QAction('upgrate to tp', self)
                action_upgrate1.triggered.connect(lambda: self.upgrate1())
                menu.addAction(action_upgrate1)

            elif self.stu == 'tp':
                action_upgrate1 = QAction('upgrate to sh', self)
                action_upgrate1.triggered.connect(lambda: self.upgrate1())
                menu.addAction(action_upgrate1)

                action_upgrate2 = QAction('upgrate to te', self)
                action_upgrate2.triggered.connect(lambda: self.upgrate2())
                menu.addAction(action_upgrate2)
            elif self.stu == 'te':
                action_upgrate2 = QAction('upgrate to sa', self)
                action_upgrate2.triggered.connect(lambda: self.upgrate2())
                menu.addAction(action_upgrate2)


            elif self.stu == None:
                action_upgrate1 = QAction('build d', self)
                action_upgrate1.triggered.connect(lambda: self.upgrate1())
                menu.addAction(action_upgrate1)

                action_upgrate2 = QAction('build landscape', self)
                action_upgrate2.triggered.connect(lambda: self.upgrate2())
                menu.addAction(action_upgrate2)

                if self.col in [self.colors_dict['ice'], self.colors_dict['lava']]:
                    ...
                else:

                    key0='green'
                    action_transform = QAction(f'transform to {key0} in {self.distance_shape(self.col,self.colors_dict[key0])} spades', self)
                    action_transform.triggered.connect(lambda: self.change_ground(self.colors_dict[key0]))
                    menu.addAction(action_transform)

                    key1='yellow'
                    action_transform = QAction(f'transform to {key1} in {self.distance_shape(self.col,self.colors_dict[key1])} spades', self)
                    action_transform.triggered.connect(lambda: self.change_ground(self.colors_dict[key1]))
                    menu.addAction(action_transform)

                    key2='blue'
                    action_transform = QAction(f'transform to {key2} in {self.distance_shape(self.col,self.colors_dict[key2])} spades', self)
                    action_transform.triggered.connect(lambda: self.change_ground(self.colors_dict[key2]))
                    menu.addAction(action_transform)

                    key3='black'
                    action_transform = QAction(f'transform to {key3} in {self.distance_shape(self.col,self.colors_dict[key3])} spades', self)
                    action_transform.triggered.connect(lambda: self.change_ground(self.colors_dict[key3]))
                    menu.addAction(action_transform)

                    key4='brown'
                    action_transform = QAction(f'transform to {key4} in {self.distance_shape(self.col,self.colors_dict[key4])} spades', self)
                    action_transform.triggered.connect(lambda: self.change_ground(self.colors_dict[key4]))
                    menu.addAction(action_transform)

                    key5='red'
                    action_transform = QAction(f'transform to {key5} in {self.distance_shape(self.col,self.colors_dict[key5])} spades', self)
                    action_transform.triggered.connect(lambda: self.change_ground(self.colors_dict[key5]))
                    menu.addAction(action_transform)

                    key6='gray'
                    action_transform = QAction(f'transform to {key6} in {self.distance_shape(self.col,self.colors_dict[key6])} spades', self)
                    action_transform.triggered.connect(lambda: self.change_ground(self.colors_dict[key6]))
                    menu.addAction(action_transform)

                    # key7='ice'
                    # action_transform = QAction(f'transform to {key7} in {self.distance_shape(self.col,self.colors_dict[key7])} spades', self)
                    # action_transform.triggered.connect(lambda: self.change_ground(self.colors_dict[key7]))
                    # menu.addAction(action_transform)
                    #
                    # key8='lava'
                    # action_transform = QAction(f'transform to {key8} in {self.distance_shape(self.col,self.colors_dict[key8])} spades', self)
                    # action_transform.triggered.connect(lambda: self.change_ground(self.colors_dict[key8]))
                    # menu.addAction(action_transform)



            menu.exec_(event.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Piece = Piece(random.randint(0, 6))
    Piece.show()
    sys.exit(app.exec_())
