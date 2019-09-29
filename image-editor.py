import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QAction, QMainWindow, QFileDialog, QHBoxLayout, QToolButton, QToolBar

from PyQt5.QtGui import QIcon, QPixmap


# from PyQt5.QtGui import QPixmap, QImage, qRgb


class ImageEditor(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Открыть файл')
        openFile.triggered.connect(self.showImageLoadDialog)

        hbox = QHBoxLayout(self)

        hbox.addWidget(self.label)
        self.setLayout(hbox)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(openFile)



        toolbar = QToolBar()
        tbSepia = QToolButton()
        toolbar.addWidget(tbSepia)
        self.addToolBar(toolbar)

        self.resize(640, 480)
        self.move(300, 200)
        self.setWindowTitle('Simple Image Editor')
        self.show()

    def showImageLoadDialog(self):
        fileDialog = QFileDialog()
        fileName = fileDialog.getOpenFileName(self, 'Load image', '', 'Image files (*.jpg *.png *.bmp)')[0]

        pixmap = QPixmap(fileName)
        w, h = pixmap.width(), pixmap.height()
        self.label.resize(w, h)

        self.resize(w, h)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    image_editor = ImageEditor()
    sys.exit(app.exec_())
