#создай тут фоторедактор Easy Editor!
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFileDialog,QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QGroupBox, QHBoxLayout,QTextEdit, QListWidget, QLineEdit, QInputDialog
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import ImageFilter

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = list()
    for i in files:
        for j in extensions:
            if i.endswith(j) == True:
                result.append(i)
    return result    

def showFilenamesList():
    chooseWorkdir()
    extensions = ['.png', '.jpg', 'jpeg', 'bmp']
    files = os.listdir(workdir)
    filename = filter(files,extensions)
    pics.clear()
    for k in filename:
        pics.addItem(k)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.pdp = "pic"

    def saveImage(self):
        path = os.path.join(workdir, self.pdp)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.pdp, self.filename)
        self.showImage(image_path)
    
    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path1 = os.path.join(workdir, self.pdp, self.filename)
        self.showImage(image_path1)
    
    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path1 = os.path.join(workdir, self.pdp, self.filename)
        self.showImage(image_path1)
    
    def zer(self):
        self.image = self.image.transpose(Image.ROTATE_180)
        self.saveImage()
        image_path1 = os.path.join(workdir, self.pdp, self.filename)
        self.showImage(image_path1)
    
    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path1 = os.path.join(workdir, self.pdp, self.filename)
        self.showImage(image_path1)

    def loadImage(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        pic.hide()
        pixmapimage = QPixmap(path)
        w, h = pic.width(), pic.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        pic.setPixmap(pixmapimage)
        pic.show()

workimage = ImageProcessor()

def showChosenImage():
    if pics.currentRow() >= 0:
        filename = pics.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)



app = QApplication([])
win = QWidget()
win.setWindowTitle('Easy Editor')

b_papka = QPushButton('Папка')
b_inter1 = QPushButton('Влево')
b_inter2 = QPushButton('Вправо')
b_inter3 = QPushButton('Зеркально')
b_inter4 = QPushButton('Размытие')
b_inter5 = QPushButton('Ч/Б')
pics = QListWidget()
pic = QLabel('картинка')
pics.currentRowChanged.connect(showChosenImage)
win.resize(700,400)

vert1 = QVBoxLayout()
vert2 = QVBoxLayout()
osn = QHBoxLayout()
hor = QHBoxLayout()

vert1.addWidget(b_papka)
vert1.addWidget(pics)
vert2.addWidget(pic)
hor.addWidget(b_inter1)
hor.addWidget(b_inter2)
hor.addWidget(b_inter3)
hor.addWidget(b_inter4)
hor.addWidget(b_inter5)
vert2.addLayout(hor)
osn.addLayout(vert1,20)
osn.addLayout(vert2,80)

b_inter1.clicked.connect(workimage.left)
b_inter2.clicked.connect(workimage.right)
b_inter3.clicked.connect(workimage.zer)
b_inter4.clicked.connect(workimage.blur)
b_inter5.clicked.connect(workimage.do_bw)
b_papka.clicked.connect(showFilenamesList)
win.setLayout(osn)

win.show()
app.exec()