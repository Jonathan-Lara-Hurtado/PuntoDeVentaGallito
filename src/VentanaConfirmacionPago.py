from PyQt5.QtWidgets import QMainWindow,QLayout

from PyQt5.QtWidgets import QApplication
from  PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtCore import pyqtSignal

from VentanasGui.VentanaConfirmacionPago import Ui_VentanaConfirmacionUi
from Herramientas.Conector import ConexionBd
from datetime import date, datetime, timedelta

class VentanaConfirmacionPago(QDialog, Ui_VentanaConfirmacionUi):

    senal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnCancelar.clicked.connect(self.cerrar)
        self.btnAceptar.clicked.connect(self.eventoAceptar)
        self.listaDetalles = []
        self.User = ""

    def darListaDetalles(self,v):
        self.listaDetalles = v
    def darUsuario(self,v):
        self.User = v

    def eventoAceptar(self):
        con = ConexionBd()
        subtotal =  self.listaDetalles.totalPrecio() / (1+(self.listaDetalles.iva/100))
        i=0
        r = True
        while(r):
            r =con.insertarVenta(i,self.User[0],date.today(),subtotal,self.listaDetalles.iva,self.listaDetalles.totalPrecio())
            i = i+1

        for e in self.listaDetalles.lista:
            con2 = ConexionBd()
            con2.insertardetalleventa(i-1,idproducto= e.idproducto,precio= e.precio,cantidad= e.cantidad)

        self.senal.emit()
        self.close()

    def cerrar(self):
        self.close()