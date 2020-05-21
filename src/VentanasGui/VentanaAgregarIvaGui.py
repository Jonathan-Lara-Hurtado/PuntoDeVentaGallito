# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ArchivosUi/VentanaAgregarIvaGui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaAgregarIvaGui(object):
    def setupUi(self, VentanaAgregarIvaGui):
        VentanaAgregarIvaGui.setObjectName("VentanaAgregarIvaGui")
        VentanaAgregarIvaGui.resize(369, 125)
        VentanaAgregarIvaGui.setMaximumSize(QtCore.QSize(369, 125))
        VentanaAgregarIvaGui.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(VentanaAgregarIvaGui)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtIva = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIva.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtIva.setObjectName("txtIva")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtIva)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.btnAgregar.setObjectName("btnAgregar")
        self.horizontalLayout_2.addWidget(self.btnAgregar)
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout_2.addWidget(self.btnCancelar)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        VentanaAgregarIvaGui.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaAgregarIvaGui)
        QtCore.QMetaObject.connectSlotsByName(VentanaAgregarIvaGui)

    def retranslateUi(self, VentanaAgregarIvaGui):
        _translate = QtCore.QCoreApplication.translate
        VentanaAgregarIvaGui.setWindowTitle(_translate("VentanaAgregarIvaGui", "Agregar Marca"))
        self.label_2.setText(_translate("VentanaAgregarIvaGui", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Iva</span></p></body></html>"))
        self.label.setText(_translate("VentanaAgregarIvaGui", "Porcentaje:"))
        self.btnAgregar.setText(_translate("VentanaAgregarIvaGui", "Agregar"))
        self.btnCancelar.setText(_translate("VentanaAgregarIvaGui", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaAgregarIvaGui = QtWidgets.QMainWindow()
    ui = Ui_VentanaAgregarIvaGui()
    ui.setupUi(VentanaAgregarIvaGui)
    VentanaAgregarIvaGui.show()
    sys.exit(app.exec_())

