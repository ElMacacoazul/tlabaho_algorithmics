from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QLineEdit
from PyQt5.QtGui import QFont
from random import randint
from final_win import FinalWin


class secondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarUI()
        self.conexiones()
        self.aparecer()
        self.show()
    def iniciarUI(self):
        self.texto1 = QLabel("Nombre y apellido")
        self.texto2 = QLabel("Edad")
        self.texto3 = QLabel("Descansa y toma tu pulso por 15 segundos Clickea \nel botón y escribe tu resultado")
        self.texto4 = QLabel("Realiza 30 sentadillas en 45 segundos y presiona el botón")
        self.texto5 = QLabel("Descansa y toma tu pulso por 15 segundos")
        self.tiempo = QLabel("00:00:00")
        self.tiempo.setFont(QFont("Times",36,QFont.Bold))

        self.boton1 = QPushButton("Empezar a contar")
        self.boton2 = QPushButton("Empezar sentadillas")
        self.boton3 = QPushButton("Empezar prueba final")
        self.boton4 = QPushButton("Enviar resultados")

        self.le1 = QLineEdit(placeholderText="Nombre y apellido")
        self.le2 = QLineEdit(placeholderText="0")
        self.le3 = QLineEdit(placeholderText="0")
        self.le4 = QLineEdit(placeholderText="0")
        self.le5 = QLineEdit(placeholderText="0")

        self.horizontal = QHBoxLayout()
        self.vertical=QVBoxLayout()
        self.vertical.addWidget(self.texto1,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.le1,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.texto2,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.le2,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.texto3,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.boton1,alignment=Qt.AlignLeft)
        self.horizontal.addWidget(self.le3,alignment=Qt.AlignLeft)
        self.horizontal.addWidget(self.tiempo,alignment=Qt.AlignRight)
        self.vertical.addLayout(self.horizontal)
        self.vertical.addWidget(self.texto4,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.boton2,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.texto5,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.boton3,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.le4,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.le5,alignment=Qt.AlignLeft)
        self.vertical.addWidget(self.boton4,alignment=Qt.AlignCenter)
        self.setLayout(self.vertical)
    def ventana3(self):
        self.tercera = FinalWin()
        self.hide()
    def conexiones(self):
        self.boton4.clicked.connect(self.ventana3)

    def aparecer(self):
        self.setWindowTitle("teeest")
        self.resize(1000,800)
        self.move(200,200)