import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Диалог открытия файлов (и папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)


from PyQt5.QtCore import Qt # нужна константа Qt.KeepAspectRatio для изменения размеров с сохранением пропорций
from PyQt5.QtGui import QPixmap # оптимизированная для показа на экране картинка


from PIL import Image

app = QApplication([])
window = QWidget()
window.setWindowTitle('Easy Editor')
window.resize(700, 500)

# create LayOuts
row_main = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
row_tools = QHBoxLayout()

# create widgets
btnOpenFolder = QPushButton('Папка')
listImages = QListWidget()

btnRight = QPushButton('Право')
btnLeft = QPushButton('Лево')
btnMirror = QPushButton('Зеркало')
btnShapeness = QPushButton('Резкость')
lbImage = QLabel()
btnBW = QPushButton('Ч\Б')

# assembly
col1.addWidget(btnOpenFolder)
col1.addWidget(listImages)
col2.addWidget(lbImage)

row_tools.addWidget(btnRight)
row_tools.addWidget(btnLeft)
row_tools.addWidget(btnMirror)
row_tools.addWidget(btnShapeness)
row_tools.addWidget(btnBW)
col2.addLayout(row_tools)

row_main.addLayout(col1)
row_main.addLayout(col2)

window.setLayout(row_main)


workdir = ''
window.show()

def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result

def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
   listImages.clear()
   for filename in filenames:
       listImages.addItem(filename)

btnOpenFolder.clicked.connect(showFilenamesList)
class ImageProcessor():
    def __init__(self):
       self.image = None
       self.dir = None
       self.filename = None
       self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        ''' при загрузке запоминаем путь и имя файла '''
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        lbImage.hide()
        pixmapimage = QPixmap(path)
        w, h = lbImage.width(), lbImage.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lbImage.setPixmap(pixmapimage)
        lbImage.show()

def showChosenImage():
    if listImages.currentRow() >= 0:
        filename = listImages.currentItem().text()
        workimage.loadImage(workdir, filename)
        imagePath = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(imagePath)

workimage = ImageProcessor()
listImages.currentRowChanged.connect(showChosenImage)


app.exec_()