from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QLineEdit
from random import randint

app = QApplication([])
ventana = QWidget()
ventana.setWindowTitle("Prueba tu suerte!")
ventana.show()
texto1 = QLabel("Nombre y apellido")
texto2 = QLabel("Edad")
texto3 = QLabel("Descansa y toma tu pulso por 15 segundos Clickea \n el botón y escribe tu resultado")
texto4 = QLabel("Realiza 30 sentadillas en 45 segundos y presiona el botón")
texto5 = QLabel("Descansa y toma tu pulso por 15 segundos")

boton1 = QPushButton("Empezar a contar")
boton2 = QPushButton("Empezar sentadillas")
boton3 = QPushButton("Empezar prueba final")
boton4 = QPushButton("Enviar resultados")

le1 = QLineEdit()
le2 = QLineEdit()
le3 = QLineEdit()
le4 = QLineEdit()
le5 = QLineEdit()

app.exec_()