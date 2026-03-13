from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout
from random import randint
from second_win import secondWin

app = QApplication([])
ventana = QWidget()
ventana.setWindowTitle("Prueba tu suerte!")
ventana.show()
texto1 = QLabel("Bienvenido al sistema de detección de salud")
texto2 = QLabel("""This application allows you to use the Rufier test to make an initial diagnosis of your health.
The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.
The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;
then, within 45 seconds, the subject performs 30 squats.
When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds
and then for the last 15 seconds of the first minute of the recovery period.
Important! If you feel unwell during the test (dizziness,
tinnitus, shortness of breath, etc.), stop the test and consult a physician.""")

boton1 = QPushButton("Comenzar")

lineav1 = QVBoxLayout()
lineav1.addWidget(texto1,alignment = Qt.AlignLeft)
lineav1.addWidget(texto2,alignment = Qt.AlignLeft)
lineav1.addWidget(boton1,alignment = Qt.AlignCenter)

def ventana2():
    # import second_win
    ventana.segunda_ventana=secondWin()
    ventana.hide()


boton1.clicked.connect(ventana2)


ventana.setLayout(lineav1)


app.exec_()