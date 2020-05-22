# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ArchivosUi/VentanaEmpleadosGui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaEmpleados(object):
    def setupUi(self, VentanaEmpleados):
        VentanaEmpleados.setObjectName("VentanaEmpleados")
        VentanaEmpleados.resize(979, 471)
        self.centralwidget = QtWidgets.QWidget(VentanaEmpleados)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tablaEmpleado = QtWidgets.QTableWidget(self.centralwidget)
        self.tablaEmpleado.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.tablaEmpleado.setObjectName("tablaEmpleado")
        self.tablaEmpleado.setColumnCount(10)
        self.tablaEmpleado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEmpleado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEmpleado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEmpleado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEmpleado.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEmpleado.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEmpleado.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEmpleado.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEmpleado.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEmpleado.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaEmpleado.setHorizontalHeaderItem(9, item)
        self.verticalLayout.addWidget(self.tablaEmpleado)
        VentanaEmpleados.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VentanaEmpleados)
        self.statusbar.setObjectName("statusbar")
        VentanaEmpleados.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaEmpleados)
        QtCore.QMetaObject.connectSlotsByName(VentanaEmpleados)

    def retranslateUi(self, VentanaEmpleados):
        _translate = QtCore.QCoreApplication.translate
        VentanaEmpleados.setWindowTitle(_translate("VentanaEmpleados", "ListaEmpleados"))
        item = self.tablaEmpleado.horizontalHeaderItem(0)
        item.setText(_translate("VentanaEmpleados", "Id Empleado"))
        item = self.tablaEmpleado.horizontalHeaderItem(1)
        item.setText(_translate("VentanaEmpleados", "Nombre"))
        item = self.tablaEmpleado.horizontalHeaderItem(2)
        item.setText(_translate("VentanaEmpleados", "Apellido Paterno"))
        item = self.tablaEmpleado.horizontalHeaderItem(3)
        item.setText(_translate("VentanaEmpleados", "Apellido Materno"))
        item = self.tablaEmpleado.horizontalHeaderItem(4)
        item.setText(_translate("VentanaEmpleados", "Edad"))
        item = self.tablaEmpleado.horizontalHeaderItem(5)
        item.setText(_translate("VentanaEmpleados", "Tipo Empleado"))
        item = self.tablaEmpleado.horizontalHeaderItem(6)
        item.setText(_translate("VentanaEmpleados", "Contraseña"))
        item = self.tablaEmpleado.horizontalHeaderItem(7)
        item.setText(_translate("VentanaEmpleados", "Fecha de Contratacion"))
        item = self.tablaEmpleado.horizontalHeaderItem(8)
        item.setText(_translate("VentanaEmpleados", "Direccion"))
        item = self.tablaEmpleado.horizontalHeaderItem(9)
        item.setText(_translate("VentanaEmpleados", "Usuario Sistema"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaEmpleados = QtWidgets.QMainWindow()
    ui = Ui_VentanaEmpleados()
    ui.setupUi(VentanaEmpleados)
    VentanaEmpleados.show()
    sys.exit(app.exec_())

