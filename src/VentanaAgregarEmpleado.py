from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget

from .VentanasGui.VentanaAgregarProductosGui import Ui_VentanaAgregarProductosGui
from Herramientas.Modelos import Producto
from PyQt5.QtCore import pyqtSignal
from Herramientas.Conector import ConexionBd


class VentanaAgregarProductos(QMainWindow, Ui_VentanaAgregarProductosGui):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()
        self.btnACancelar.clicked.connect(self.eventoCancelar)
        self.btnAAgregar.clicked.connect(self.eventoAceptar)

    def iniciar(self):
        self.centrarPantalla()

    def centrarPantalla(self):
        """
        Referencia = https://pythonprogramminglanguage.com/pyqt5-center-window/
        """
        qtRect = self.frameGeometry()
        point = QDesktopWidget().availableGeometry().center()
        qtRect.moveCenter(point)
