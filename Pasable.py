


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Respuesta_Pasable(object):
    def setupUi(self, Form,total):
        self.total = total
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setMinimumSize(QtCore.QSize(1920, 1080))
        Form.setMaximumSize(QtCore.QSize(1920, 1080))
        Form.setBaseSize(QtCore.QSize(1920, 1080))
        self.Bannerfondo = QtWidgets.QFrame(Form)
        self.Bannerfondo.setGeometry(QtCore.QRect(0, 0, 1931, 141))
        self.Bannerfondo.setStyleSheet("  background: #7C90DF;")
        self.Bannerfondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Bannerfondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Bannerfondo.setObjectName("Bannerfondo")
        self.label = QtWidgets.QLabel(self.Bannerfondo)
        self.label.setGeometry(QtCore.QRect(510, 30, 861, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")

        self.frameLog1 = QtWidgets.QLabel(Form)
        self.frameLog1.setGeometry(QtCore.QRect(350, -20, 200, 160))
        self.frameLog1.setPixmap(QtGui.QPixmap('imagenes/logo.png'))
        self.frameLog1.setScaledContents(True)
        self.frameLog1.setObjectName("frameLog1")

        self.frameLog1_2 = QtWidgets.QLabel(Form)
        self.frameLog1_2.setGeometry(QtCore.QRect(1240, 0, 200, 160))
        self.frameLog1_2.setPixmap(QtGui.QPixmap('imagenes/logo invertido.png'))
        self.frameLog1_2.setScaledContents(True)
        self.frameLog1_2.setObjectName("frameLog1_2")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 2000, 121))  # Ajusta los valores de posición (50, 160) y ancho (1421)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(660, 230, 671, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(780, 370, 361, 161))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Emoji = QtWidgets.QLabel(Form)
        self.Emoji.setGeometry(QtCore.QRect(770, 510, 371, 350))

        # Cargar la imagen "pesimo.jpeg" y establecerla como fondo
        print("Cargando la imagen...")
        pixmap = QtGui.QPixmap('imagenes/Pasable.png')
        print("Imagen cargada")

        self.Emoji.setPixmap(pixmap)
        self.Emoji.setScaledContents(True)

        self.Emoji.setObjectName("Emoji")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Evaluación de Productos Ganadores"))
        self.label_2.setText(_translate("Form", f"No está mal, pero no te aseguro exelentes resultados con este producto. La puntuacion de tu producto es de {self.total}"))
        self.label_3.setText(_translate("Form", "lo que significa que tu producto es:"))
        self.label_4.setText(_translate("Form", "PASABLE"))
