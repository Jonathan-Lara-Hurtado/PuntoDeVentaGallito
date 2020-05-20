from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget

from VentanasGui.VentanaAgregarProductosGui import Ui_VentanaAgregarProductosGui
from Herramientas.Modelos import Producto
from PyQt5.QtCore import pyqtSignal
from Herramientas.Conector import ConexionBd

class VentanaAgregarProductos(QMainWindow , Ui_VentanaAgregarProductosGui):

    senal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()
        self.btnACancelar.clicked.connect(self.eventoCancelar)
        self.categoria={}
        self.proveedor={}
        self.btnAAgregar.clicked.connect(self.eventoAceptar)

    def iniciar(self):
        self.centrarPantalla()

    def darCategoria(self,valor):
        self.categoria = valor
        for i in self.categoria:
            self.comboMarca.addItem(self.tr(i.marca))

    def darProvedor(self,valor):
        self.proveedor = valor
        for i in self.proveedor:
            self.comboProveedor.addItem(self.tr(i.nombreCompany))

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
        tmp = []
        tmp2 = []
        for i in self.categoria:
            if i.__str__() == self.comboMarca.currentText():
                tmp = i
#        print(tmp)
        for e in self.proveedor:
            if e.__str__() == self.comboProveedor.currentText():
                tmp2 = e
#        print(tmp2)
        con  = ConexionBd()

        p = con.insertarProducto(tmp.idMarca, tmp2.idproveedor,
                     self.txtANombre.text(), self.txtACodigoBarra.text(),
                     self.preciospin.value(), self.textEditADescripcion.toPlainText(),
                     self.stockspink.value())
        self.senal.emit()
        con.cerrarConexion()
        self.close()
#        p = Producto(self.txtANombre.text(),self.txtACodigoBarra.text(),
 #                    self.textEditADescripcion.toPlainText(),self.stockspink.value(),
  #                   self.preciospin.value(),tmp.idMarca)
#
 #       self.senal.emit()
  #      self.close()