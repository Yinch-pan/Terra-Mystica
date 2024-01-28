import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QAction, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class PopupMenuExample(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # 创建一个 QLabel 用于显示消息
        self.message_label = QLabel('右键点击以弹出菜单', self)
        layout.addWidget(self.message_label)

    def contextMenuEvent(self, event):
        # 鼠标右键点击事件，弹出菜单
        menu = QMenu(self)

        # 创建菜单项
        action1 = QAction('选项1', self)
        action1.triggered.connect(lambda: self.show_message('选项1被点击'))

        action2 = QAction('选项2', self)
        action2.triggered.connect(lambda: self.show_message('选项2被点击'))

        action3 = QAction('选项3', self)
        action3.triggered.connect(lambda: self.show_message('选项3被点击'))

        # 将菜单项添加到菜单
        menu.addAction(action1)
        menu.addAction(action2)
        menu.addAction(action3)

        # 显示菜单
        menu.exec_(event.globalPos())

    def show_message(self, text):
        # 在 QLabel 中显示消息
        self.message_label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    popup_menu_example = PopupMenuExample()
    popup_menu_example.setWindowTitle('鼠标左键弹出列表选项')
    popup_menu_example.setGeometry(100, 100, 400, 200)
    popup_menu_example.show()

    sys.exit(app.exec_())
