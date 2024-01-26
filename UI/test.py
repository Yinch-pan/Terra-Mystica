import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QPointF, QSizeF


class ResizableGridLayout(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QVBoxLayout())
        self.setCursor(Qt.PointingHandCursor)

        self.mouse_press_position = QPointF(0, 0)
        self.offset = QPointF(0, 0)
        self.scale_factor = 1.0

        for i in range(3):  # 3x3 grid example
            for j in range(3):
                label = QLabel(f'Cell {i+1}-{j+1}', self)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setStyleSheet('border: 1px solid black;')  # Optional: Add borders for better visibility
                self.layout().addWidget(label)

    def wheelEvent(self, event):
        # 缩放因子
        factor = 1.2

        # 根据滚轮方向调整缩放因子
        if event.angleDelta().y() < 0:
            self.scale_factor /= factor
        else:
            self.scale_factor *= factor

        # 设置缩放变换
        self.setTransformOriginPoint(self.width() / 2, self.height() / 2)
        self.setScaledContents(True)
        self.setFixedSize(QSizeF(self.size()) * self.scale_factor)
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_press_position = event.globalPos()
            self.offset = self.mouse_press_position - self.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            global_pos = event.globalPos()
            moved = global_pos - self.mouse_press_position
            self.move(moved + self.offset)


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
    sys.exit(app.exec())
