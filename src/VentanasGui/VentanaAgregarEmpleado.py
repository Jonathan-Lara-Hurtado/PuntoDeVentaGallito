# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ArchivosUi/VentanaAgregarEmpleado.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaAgregarEmpleadoGui(object):
    def setupUi(self, VentanaAgregarEmpleadoGui):
        VentanaAgregarEmpleadoGui.setObjectName("VentanaAgregarEmpleadoGui")
        VentanaAgregarEmpleadoGui.resize(463, 406)
        VentanaAgregarEmpleadoGui.setMinimumSize(QtCore.QSize(463, 406))
        VentanaAgregarEmpleadoGui.setMaximumSize(QtCore.QSize(463, 406))
        VentanaAgregarEmpleadoGui.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(VentanaAgregarEmpleadoGui)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtNombre.setObjectName("txtNombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtNombre)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtPaterno = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPaterno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPaterno.setObjectName("txtPaterno")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtPaterno)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtMaterno = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMaterno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtMaterno.setObjectName("txtMaterno")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtMaterno)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboEdad = QtWidgets.QComboBox(self.centralwidget)
        self.comboEdad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboEdad.setObjectName("comboEdad")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboEdad)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtTipoEmpleado = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTipoEmpleado.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtTipoEmpleado.setObjectName("txtTipoEmpleado")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtTipoEmpleado)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtPassword)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txtDireccion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDireccion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDireccion.setObjectName("txtDireccion")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txtDireccion)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.txtCorreo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCorreo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCorreo.setObjectName("txtCorreo")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txtCorreo)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAAgregar.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"")
        self.btnAAgregar.setObjectName("btnAAgregar")
        self.horizontalLayout_2.addWidget(self.btnAAgregar)
        self.btnACancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnACancelar.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.btnACancelar.setObjectName("btnACancelar")
        self.horizontalLayout_2.addWidget(self.btnACancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        VentanaAgregarEmpleadoGui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VentanaAgregarEmpleadoGui)
        self.statusbar.setObjectName("statusbar")
        VentanaAgregarEmpleadoGui.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaAgregarEmpleadoGui)
        QtCore.QMetaObject.connectSlotsByName(VentanaAgregarEmpleadoGui)

    def retranslateUi(self, VentanaAgregarEmpleadoGui):
        _translate = QtCore.QCoreApplication.translate
        VentanaAgregarEmpleadoGui.setWindowTitle(_translate("VentanaAgregarEmpleadoGui", "Agregar Producto"))
        self.label.setText(_translate("VentanaAgregarEmpleadoGui", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">AGREGAR EMPLEADO</span></p></body></html>"))
        self.label_3.setText(_translate("VentanaAgregarEmpleadoGui", "Nombre:"))
        self.label_4.setText(_translate("VentanaAgregarEmpleadoGui", "Apellido Paterno:"))
        self.label_2.setText(_translate("VentanaAgregarEmpleadoGui", "Apellido Materno:"))
        self.label_5.setText(_translate("VentanaAgregarEmpleadoGui", "Edad:"))
        self.label_6.setText(_translate("VentanaAgregarEmpleadoGui", "tipo Empleado:"))
        self.label_7.setText(_translate("VentanaAgregarEmpleadoGui", "Contraseña:"))
        self.label_9.setText(_translate("VentanaAgregarEmpleadoGui", "Direccion:"))
        self.label_10.setText(_translate("VentanaAgregarEmpleadoGui", "Correo:"))
        self.btnAAgregar.setText(_translate("VentanaAgregarEmpleadoGui", "Agregar"))
        self.btnACancelar.setText(_translate("VentanaAgregarEmpleadoGui", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaAgregarEmpleadoGui = QtWidgets.QMainWindow()
    ui = Ui_VentanaAgregarEmpleadoGui()
    ui.setupUi(VentanaAgregarEmpleadoGui)
    VentanaAgregarEmpleadoGui.show()
    sys.exit(app.exec_())

