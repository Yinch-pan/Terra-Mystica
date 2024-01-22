import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QApplication, QScrollArea, QDesktopWidget
import map

def chtype(a):
    pass

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        screen = QDesktopWidget().screenGeometry()
        self.screen_width, self.screen_height = screen.width(), screen.height()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 1080)  # 设置窗口的位置和大小

        self.setWindowTitle('Terra Mystica')  # 设置窗口标题

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)


        main_widget = QWidget(scroll_area)
        scroll_area.setGeometry(0,0,1920,1080)
        scroll_area.setWidget(main_widget)


        main_layout = QGridLayout(main_widget)

        map_area = map.map_area(self, "map12.txt")
        main_layout.addWidget(map_area, 0, 0, 20, 20)

        cult_board = QLabel(self)
        cult_board_pic = QPixmap('..\\images\\cult_board.jpg')
        cult_board.setScaledContents(True)
        cult_board.setPixmap(cult_board_pic)
        main_layout.addWidget(cult_board, 0, 20, 20, 10)

        function1 = QLabel(self)
        function1_pic = QPixmap('..\\images\\functions\\base\\black\\Darklings.jpg')
        function1_pic = function1_pic.scaledToHeight(function1_pic.height() // 2)
        function1.setScaledContents(True)
        function1.setPixmap(function1_pic)
        main_layout.addWidget(function1, 20, 0, 4, 15)

        function2 = QLabel(self)
        function2_pic = QPixmap('..\\images\\functions\\base\\black\\Darklings.jpg')
        function2_pic = function2_pic.scaledToHeight(function2_pic.height() // 2)
        function2.setScaledContents(True)
        function2.setPixmap(function2_pic)
        main_layout.addWidget(function2, 20, 16, 10, 15)

        scroll_area.setVerticalScrollBarPolicy(0x2)  # 始终显示垂直滚动条

        self.show()  # 显示窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
