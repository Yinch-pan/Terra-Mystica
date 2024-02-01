import os.path
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor, QPainter
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QApplication

BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR = os.path.dirname(BASE_DIR)


class Token(QWidget):
    def __init__(self):
        super().__init__()
        self.num=0
        self.size_factor = 1
        self.real_width = 100*self.size_factor
        self.real_height = 100*self.size_factor
        self.initUI()
        self.setFixedSize(70,70)
        # self.show()

    def initUI(self):
        self.token_layout = QGridLayout()
        self.setLayout(self.token_layout)
        # self.set_p()
        # self.set_token()
        # self.show()

    def del_token(self):
        self.token_layout.deleteLater()

    def set_token(self,col):
        self.num += 1
        self.stu = 'tk'
        image_path = os.path.join(BASE_DIR, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_tk_all = []
        for i in range(9):
            org_pic = full_pixmap.copy(i * 140+40, 980, 70, 90)
            org_pic = org_pic.scaled(int(org_pic.width() * self.size_factor),
                                     int(org_pic.height() * self.size_factor))

            real_pic = QPixmap(self.real_width, self.real_height)
            real_pic.fill(QColor(Qt.transparent))  # 使用透明色填充作为背景

            painter = QPainter(real_pic)
            painter.drawPixmap((real_pic.width() - org_pic.width()) // 2,
                               (real_pic.height() - org_pic.height()) // 2,
                               org_pic)
            painter.end()
            stu_tk_all.append(real_pic)

        self.tk = QLabel()
        self.tk.setScaledContents(True)
        self.tk.setPixmap(stu_tk_all[col])
        self.token_layout.addWidget(self.tk,0,0)

    def set_p(self,col):
        self.num+=1
        self.stu = 'p'
        image_path = os.path.join(BASE_DIR, 'images', 'structures.png')
        full_pixmap = QPixmap(image_path)
        stu_p_all = []
        for i in range(9):
            org_pic = full_pixmap.copy(i * 140, 800, 140, 140)
            org_pic = org_pic.scaled(int(org_pic.width() * self.size_factor),
                                     int(org_pic.height() * self.size_factor))

            real_pic = QPixmap(self.real_width, self.real_height)
            real_pic.fill(QColor(Qt.transparent))  # 使用透明色填充作为背景

            painter = QPainter(real_pic)
            painter.drawPixmap((real_pic.width() - org_pic.width()) // 2,
                               (real_pic.height() - org_pic.height()) // 2,
                               org_pic)
            painter.end()
            stu_p_all.append(real_pic)

        self.p = QLabel()
        self.p.setScaledContents(True)
        self.p.setPixmap(stu_p_all[col])
        self.token_layout.addWidget(self.p,0,self.num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Token(2)
    sys.exit(app.exec_())
