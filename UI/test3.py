import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt, QPoint


class GridPositionExample(QWidget):
    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout(self)

        button1 = QPushButton('Button 1', self)
        self.grid_layout.addWidget(button1, 0, 0)

        button2 = QPushButton('Button 2', self)
        self.grid_layout.addWidget(button2, 1, 1)

        self.label = QLabel(self)
        self.grid_layout.addWidget(self.label, 2, 2)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            relative_pos = self.mapFromGlobal(event.globalPos())
            item = self.grid_layout.itemAtPosition(relative_pos.y(), relative_pos.x())

            if item is not None:
                widget = item.widget()
                if widget:
                    self.label.setText(f'Clicked on: {widget.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    grid_position_example = GridPositionExample()
    grid_position_example.setWindowTitle('获取鼠标相对位置的示例')
    grid_position_example.setGeometry(100, 100, 300, 200)
    grid_position_example.show()

    sys.exit(app.exec_())
