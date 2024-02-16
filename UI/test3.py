from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextBrowser
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # 创建Qt界面元素
        self.label = QLabel('Hello, PyQt!')
        self.button = QPushButton('Click Me')
        self.text_browser = QTextBrowser()

        # 将元素添加到垂直布局中
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.text_browser)

        # 创建一个窗口部件，将布局设置为主窗口的中央部分
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 为按钮连接信号和槽
        self.button.clicked.connect(self.update_text_browser)

    def update_text_browser(self):
        # 当按钮被点击时，更新TextBrowser的内容
        self.text_browser.append('Button Clicked!')

if __name__ == "__main__":
    app = QApplication([])

    # 创建主窗口
    window = MyWindow()
    window.show()

    # 创建QWebEngineView
    web_engine_view = QWebEngineView()
    web_engine_view.setHtml('<html><body><h1>Hello, HTML!</h1></body></html>')

    # 显示QWebEngineView
    web_engine_view.show()

    app.exec_()
