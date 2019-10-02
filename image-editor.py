import sys
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QAction, QMainWindow, QFileDialog, QHBoxLayout, QToolButton, \
    QToolBar

from PyQt5.QtGui import QIcon, QPixmap

from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt


# from PyQt5.QtGui import QPixmap, QImage, qRgb


class ImageEditor(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.initUI()

    def initUI(self):


        openFile = QAction(QIcon('assets/open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('&Open file')
        openFile.triggered.connect(self.show_image_load_dialog)

        hbox = QHBoxLayout(self)


        self.setLayout(hbox)

        self.menubar = self.menuBar()
        file_menu = self.menubar.addMenu('&File')
        file_menu.addAction(openFile)

        self.label = QLabel()

        self.toolbar = QToolBar()
        self.toolbar.addAction(openFile)
        self.addToolBar(self.toolbar)
        # hbox.addWidget(self.menubar)
        hbox.addWidget(self.label)
        self.resize(640, 480)
        self.set_pos_to_center_of_screen()
        self.setWindowTitle('Simple Image Editor')
        self.show()

    def show_image_load_dialog(self):
        file_dialog = QFileDialog()
        file_name = file_dialog.getOpenFileName(self, 'Load image', '', 'Image files (*.jpg *.png *.bmp)')[0]
        if file_name:
            self.setWindowTitle(f'Image editor - {file_name}')
            self.image = Image.open(file_name)
            # draw = ImageDraw.Draw(self.image)
            img_tmp = ImageQt(self.image.convert('RGBA'))
            pixmap = QPixmap.fromImage(img_tmp)
            w, h = pixmap.width(), pixmap.height()
            # self.label.move(w, self.toolbar.height())
            self.label.move()

            self.label.resize(w, h)
            # self.adjustSize()
            self.resize(w, h)
            self.set_pos_to_center_of_screen()
            self.label.setPixmap(pixmap)

    def get_screen_size(self):
        screen = self.app.primaryScreen()
        screen_size = screen.size()
        screen_width = screen_size.width()
        screen_height = screen_size.height()
        return screen_width, screen_height

    def set_pos_to_center_of_screen(self):
        screen_width, screen_height = self.get_screen_size()
        window_width = self.width()
        window_height = self.height()
        self.move((screen_width - window_width) / 2, (screen_height - window_height) / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    image_editor = ImageEditor(app)
    sys.exit(app.exec_())
