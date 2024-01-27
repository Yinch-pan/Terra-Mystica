import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class BlurredImageWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # 加载图片
        pixmap = QPixmap('E:\code\project\Terra-Mystica\images\landscape_tiles.png')  # 替换为你的图片路径

        # 创建包含图片的 QLabel
        image_label = QLabel(self)
        image_label.setPixmap(pixmap)

        # 添加羽化效果
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(2)  # 设置模糊半径，值越大越模糊
        image_label.setGraphicsEffect(blur_effect)

        layout.addWidget(image_label)

        # 创建包含图片的 QLabel
        image_label2 = QLabel(self)
        image_label2.setPixmap(pixmap)

        layout.addWidget(image_label2)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    blurred_image_widget = BlurredImageWidget()
    blurred_image_widget.setWindowTitle('图片羽化效果')
    blurred_image_widget.setGeometry(100, 100, 300, 300)
    blurred_image_widget.show()

    sys.exit(app.exec_())
