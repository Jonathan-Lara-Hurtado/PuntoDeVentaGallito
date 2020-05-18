from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget

from VentanasGui.VentanaAgregarEmpleado import Ui_VentanaAgregarEmpleadoGui
from Herramientas.Modelos import Producto
from PyQt5.QtCore import pyqtSignal
from Herramientas.Conector import ConexionBd
from datetime import date, datetime, timedelta


class VentanaAgregarEmpleado(QMainWindow, Ui_VentanaAgregarEmpleadoGui):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()
        self.btnACancelar.clicked.connect(self.eventoCancelar)
        self.btnAAgregar.clicked.connect(self.eventoAceptar)


    def iniciar(self):
        self.centrarPantalla()
        self.rellenarCombo()


    def rellenarCombo(self):
        for i in range(18,100):
            self.comboEdad.addItem(self.tr(str(i)))

    def centrarPantalla(self):
        """
        Referencia = https://pythonprogramminglanguage.com/pyqt5-center-window/
        """
        qtRect = self.frameGeometry()
        point = QDesktopWidget().availableGeometry().center()
        qtRect.moveCenter(point)

    def eventoCancelar(self):
        self.close()

    def eventoAceptar(self):
        edad = int(self.comboEdad.currentText())
        con = ConexionBd()
        con.insertarUsuario(self.txtNombre.text(),self.txtPaterno.text(),
                            self.txtMaterno.text(),edad,
                            self.txtTipoEmpleado.text(),self.txtPassword.text(),
                            datetime.today(),self.txtDireccion.text(),self.txtCorreo.text())
        self.close()