from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget

from VentanasGui.VentanaAgregarProductosGui import Ui_VentanaAgregarProductosGui
from Herramientas.Modelos import Producto
from PyQt5.QtCore import pyqtSignal
from Herramientas.Conector import ConexionBd
from Herramientas.ListaObjeto import ListaObjetos
from PyQt5.QtWidgets import QTableWidgetItem
from VentanasGui.VentanaEmpleadosGui import Ui_VentanaEmpleados


class VentanaListaEmpleados(QMainWindow,Ui_VentanaEmpleados):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.listaEmpleado = ListaObjetos(tabla="empleado")
        self.listaEmpleado.listarObjetos()
        self.rellenarTabla()

    def rellenarTabla(self):
        self.tablaEmpleado.setRowCount(0)
        contadorR = 0
        for row in self.listaEmpleado.lista:
            self.tablaEmpleado.insertRow(contadorR)
            self.tablaEmpleado.setItem(contadorR, 0, QTableWidgetItem(str(row.idempleado)))
            self.tablaEmpleado.setItem(contadorR, 1, QTableWidgetItem(str(row.nombre)))
            self.tablaEmpleado.setItem(contadorR, 2, QTableWidgetItem(str(row.apellidopaterno)))
            self.tablaEmpleado.setItem(contadorR, 3, QTableWidgetItem(str(row.apellidomaterno)))
            self.tablaEmpleado.setItem(contadorR, 4, QTableWidgetItem(str(row.edad)))
            self.tablaEmpleado.setItem(contadorR, 5, QTableWidgetItem(str(row.tipoempleado)))
            self.tablaEmpleado.setItem(contadorR, 6, QTableWidgetItem(str(row.contrasena)))
            self.tablaEmpleado.setItem(contadorR, 7, QTableWidgetItem(str(row.fechaContratacion)))
            self.tablaEmpleado.setItem(contadorR, 8, QTableWidgetItem(str(row.direccion)))
            self.tablaEmpleado.setItem(contadorR, 9, QTableWidgetItem(str(row.correo)))

            contadorR += 1
        self.repaint()
        self.update()
