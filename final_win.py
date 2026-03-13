from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QLineEdit
from PyQt5.QtGui import QFont
from random import randint


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarUI()
        self.conexiones()
        self.aparecer()
        self.show()
    def iniciarUI(self):
        self.texto1 = QLabel("Indice de Roufier")
        self.texto2 = QLabel("Estado cardiaco:")

        self.vertical=QVBoxLayout()
        self.vertical.addWidget(self.texto1,alignment=Qt.AlignCenter)
        self.vertical.addWidget(self.texto2,alignment=Qt.AlignCenter)
        self.setLayout(self.vertical)

    def conexiones(self):
        pass
    def aparecer(self):
        self.setWindowTitle("teeest")
        self.resize(1000,800)
        self.move(200,200)