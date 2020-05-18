from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget
from PyQt5.QtCore import pyqtSignal

from VentanasGui.VentanaOpcionesProductosGui import Ui_VentanaOpcionesProductosGui

class VentanaOpcionesProductos(QMainWindow,Ui_VentanaOpcionesProductosGui):
    senal = pyqtSignal()
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()
        self.categoria= {}
        self.btnACancelar.clicked.connect(self.eventoCancelar)

    def iniciar(self):
        self.centrarPantalla()

    def darValores(self,valor):
        self.txtACodigoBarra.setText(valor.codigoBarra)
        self.txtANombre.setText(str(valor.nombreproducto))
        self.textEditADescripcion.setText(str(valor.descripcion))
        self.stockspink.setValue(valor.existencia)
        self.preciospin.setValue(valor.precioventa)
#        self.txtACodigoBarra.setText()


    def darMarca(self,valor):
        self.categoria = valor
        for i in self.categoria:
            self.comboMarca.addItem(self.tr(i.marca))

    def darProvedor(self, valor):
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