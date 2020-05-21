# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ArchivosUi/VentanaConfirmacionPago.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaConfirmacionUi(object):
    def setupUi(self, VentanaConfirmacionUi):
        VentanaConfirmacionUi.setObjectName("VentanaConfirmacionUi")
        VentanaConfirmacionUi.resize(585, 134)
        self.verticalLayout = QtWidgets.QVBoxLayout(VentanaConfirmacionUi)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(VentanaConfirmacionUi)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAceptar = QtWidgets.QPushButton(VentanaConfirmacionUi)
        self.btnAceptar.setObjectName("btnAceptar")
        self.horizontalLayout.addWidget(self.btnAceptar)
        self.btnCancelar = QtWidgets.QPushButton(VentanaConfirmacionUi)
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(VentanaConfirmacionUi)
        QtCore.QMetaObject.connectSlotsByName(VentanaConfirmacionUi)

    def retranslateUi(self, VentanaConfirmacionUi):
        _translate = QtCore.QCoreApplication.translate
        VentanaConfirmacionUi.setWindowTitle(_translate("VentanaConfirmacionUi", "Confirmacion Pago"))
        self.label.setText(_translate("VentanaConfirmacionUi", "Esta seguro de su compra!!"))
        self.btnAceptar.setText(_translate("VentanaConfirmacionUi", "Aceptar"))
        self.btnCancelar.setText(_translate("VentanaConfirmacionUi", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaConfirmacionUi = QtWidgets.QDialog()
    ui = Ui_VentanaConfirmacionUi()
    ui.setupUi(VentanaConfirmacionUi)
    VentanaConfirmacionUi.show()
    sys.exit(app.exec_())

