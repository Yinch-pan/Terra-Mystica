import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel


class NoSpacingInNestedGridLayout(QWidget):
    def __init__(self):
        super().__init__()

        # 创建主网格布局
        main_layout = QGridLayout(self)
        main_layout.setSpacing(0)  # 设置主布局的间隙为零

        # 创建第一个子网格布局
        layout1 = QGridLayout()
        label1 = QLabel('子布局1 - 行1列1')
        layout1.addWidget(label1, 0, 0)
        label2 = QLabel('子布局1 - 行1列2')
        layout1.addWidget(label2, 0, 1)
        main_layout.addLayout(layout1, 0, 0)

        # 创建第二个子网格布局
        layout2 = QGridLayout()
        label3 = QLabel('子布局2 - 行1列1')
        layout2.addWidget(label3, 0, 0)
        label4 = QLabel('子布局2 - 行2列1')
        layout2.addWidget(label4, 1, 0)
        main_layout.addLayout(layout2, 0, 1)

        # 设置主窗口大小
        self.setGeometry(100, 100, 400, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    no_spacing_in_nested_grid_layout = NoSpacingInNestedGridLayout()
    no_spacing_in_nested_grid_layout.setWindowTitle('取消两个嵌套网格布局之间的间隙')
    no_spacing_in_nested_grid_layout.show()

    sys.exit(app.exec_())
