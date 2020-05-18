from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget

from VentanasGui.VentanaAgregarProvedor import Ui_VentanaAgregarProveedorGui
from Herramientas.Modelos import Producto
from PyQt5.QtCore import pyqtSignal
from Herramientas.Conector import ConexionBd

class VentanaAgregarProveedor(QMainWindow , Ui_VentanaAgregarProveedorGui):
    senal = pyqtSignal()
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
        self.move(qtRect.topLeft())


    def eventoCancelar(self):
        self.close()

    def eventoAceptar(self):
        con = ConexionBd()
        con.insertarProvedor(self.txtCompania.text(),self.txtContacto.text(),self.txtDireccion.text(),self.txtCiudad.text(),
                             self.txtRegion.text(),int(self.txtCodigoPostal.text()),
                             self.txtPais.text(),int(self.txtTelefono.text()),
                             self.txtFax.text())
        con.cerrarConexion()
        self.senal.emit()
        self.close()