import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QGridLayout
from PyQt5.QtCore import Qt, QPoint


class ResizableGridLayout(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QGridLayout())
        self.setCursor(Qt.PointingHandCursor)

        # self.mouse_press_position = QPoint(0, 0)
        # self.offset = QPoint(0, 0)


        for i in range(3):  # 3x3 grid example
            for j in range(3):
                label = QLabel(f'Cell {i+1}-{j+1}', self)
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet('border: 1px solid black;')  # Optional: Add borders for better visibility
                self.layout().addWidget(label, i, j)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_press_position = event.globalPos()
    #         self.offset = self.mouse_press_position - self.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            now_pos = event.globalPos()
            moved = now_pos - self.mouse_press_position
            self.move(moved+self.mouse_press_position)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        resizable_grid_layout = ResizableGridLayout(central_widget)
        layout.addWidget(resizable_grid_layout)

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('可拖动和缩放的网格布局')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
