from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget
from PyQt5.QtCore import *

from VentanasGui.VentanaAgregarIvaGui import Ui_VentanaAgregarIvaGui
from Herramientas.Modelos import Marca

from Herramientas.Conector import ConexionBd

class VentanaAgregarIva(QMainWindow , Ui_VentanaAgregarIvaGui):
    senal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()
        self.btnCancelar.clicked.connect(self.eventoCancelar)
        self.btnAgregar.clicked.connect(self.eventoAceptar)
        self.con = ConexionBd()

    def iniciar(self):
        self.centrarPantalla()

    def centrarPantalla(self):
        """
        Referencia = https://pythonprogramminglanguage.com/pyqt5-center-window/
        """
        qtRect = self.frameGeometry()
        point = QDesktopWidget().availableGeometry().center()
        qtRect.moveCenter(point)
        self.move(qtRect.topLeft())

    def eventoCancelar(self):
        self.close()

    def eventoAceptar(self):
        self.con.insertarIva(int(self.txtIva.text()))
        self.senal.emit()
        self.close()