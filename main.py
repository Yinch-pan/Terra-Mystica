import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('My PyQt5 App')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyApplication()
    sys.exit(app.exec_())
'''
E:\code\project\Terra-Mystica\venv\Scripts\activate.bat pip install PyQt5

'''