# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ArchivosUi/VentanaLogin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaUiLogi(object):
    def setupUi(self, VentanaUiLogi):
        VentanaUiLogi.setObjectName("VentanaUiLogi")
        VentanaUiLogi.resize(594, 164)
        self.verticalLayout = QtWidgets.QVBoxLayout(VentanaUiLogi)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(VentanaUiLogi)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtUsuario = QtWidgets.QLineEdit(VentanaUiLogi)
        self.txtUsuario.setObjectName("txtUsuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtUsuario)
        self.label_2 = QtWidgets.QLabel(VentanaUiLogi)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtpass = QtWidgets.QLineEdit(VentanaUiLogi)
        self.txtpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtpass.setObjectName("txtpass")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtpass)
        self.mensajeError = QtWidgets.QLabel(VentanaUiLogi)
        self.mensajeError.setText("")
        self.mensajeError.setAlignment(QtCore.Qt.AlignCenter)
        self.mensajeError.setObjectName("mensajeError")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.mensajeError)
        self.btnAceptar = QtWidgets.QPushButton(VentanaUiLogi)
        self.btnAceptar.setObjectName("btnAceptar")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.btnAceptar)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(VentanaUiLogi)
        QtCore.QMetaObject.connectSlotsByName(VentanaUiLogi)

    def retranslateUi(self, VentanaUiLogi):
        _translate = QtCore.QCoreApplication.translate
        VentanaUiLogi.setWindowTitle(_translate("VentanaUiLogi", "Iniciar Sesion"))
        self.label.setText(_translate("VentanaUiLogi", "Correo:"))
        self.label_2.setText(_translate("VentanaUiLogi", "Constraseña:"))
        self.btnAceptar.setText(_translate("VentanaUiLogi", "Acceder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaUiLogi = QtWidgets.QDialog()
    ui = Ui_VentanaUiLogi()
    ui.setupUi(VentanaUiLogi)
    VentanaUiLogi.show()
    sys.exit(app.exec_())

