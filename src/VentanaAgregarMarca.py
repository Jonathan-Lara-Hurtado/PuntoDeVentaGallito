from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget
from PyQt5.QtCore import *

from VentanasGui.VentanaAgregarMarcaGui import Ui_VentanaAgregarMarcaGui
from Herramientas.Modelos import Marca

from Herramientas.Conector import ConexionBd

class VentanaAgregarMarca(QMainWindow , Ui_VentanaAgregarMarcaGui):
    senal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()
        self.btnCancelar.clicked.connect(self.eventoCancelar)
        self.marca={}
        self.btnAgregar.clicked.connect(self.eventoAceptar)
        self.con = ConexionBd()

    def iniciar(self):
        self.centrarPantalla()

    def darCategoria(self,valor):
        self.categoria = valor
        for i in self.categoria:
            self.comboMarca.addItem(self.tr(i.marca))

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
        self.con.insertarMarca(self.txtMarca.text())
        self.senal.emit()
        self.close()
      #  m = Marca(marca=self.txtMarca.text())
       # m.alta()
        #self.senal.emit()
        #self.close()