from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget

from VentanasGui.VentanaAgregarProductosGui import Ui_VentanaAgregarProductosGui
from Herramientas.Modelos import Producto
from PyQt5.QtCore import pyqtSignal

class VentanaAgregarProductos(QMainWindow , Ui_VentanaAgregarProductosGui):
    senal = pyqtSignal()
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()
        self.btnACancelar.clicked.connect(self.eventoCancelar)
        self.categoria={}
        self.btnAAgregar.clicked.connect(self.eventoAceptar)

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
        tmp = []
        for i in self.categoria:
            if i.__str__() == self.comboMarca.currentText():
                tmp = i
        print(tmp)
        p = Producto(self.txtANombre.text(),self.txtACodigoBarra.text(),
                     self.textEditADescripcion.toPlainText(),self.stockspink.value(),
                     self.preciospin.value(),tmp.idMarca)
        p.alta()
        self.senal.emit()
        self.close()