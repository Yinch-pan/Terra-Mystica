import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget

import piece

class Piece(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        Singlepiece=piece.Piece()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Piece = Piece()
    Piece.show()
    sys.exit(app.exec_())
