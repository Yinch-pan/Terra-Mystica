import os.path
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QDesktopWidget
import grid


BASE_DIR = os.path.realpath(sys.argv[0])
while not BASE_DIR.endswith('Terra-Mystica'):
    BASE_DIR=os.path.dirname(BASE_DIR)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        screen = QDesktopWidget().screenGeometry()
        self.screen_width, self.screen_height = screen.width(), screen.height()

        self.initUI()

    def initUI(self):

        self.setGeometry(0, 0, 1920//2, 1080//2)  # 设置窗口的位置和大小
        self.setWindowTitle('Terra Mystica')  # 设置窗口标题

        main_layout=QGridLayout()
        grid_content=grid.Grid()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.addWidget(grid_content)
        self.setLayout(main_layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
