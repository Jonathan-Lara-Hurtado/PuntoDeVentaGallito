# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ArchivosUi/VentanaAgregarMarcaGui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaAgregarMarcaGui(object):
    def setupUi(self, VentanaAgregarMarcaGui):
        VentanaAgregarMarcaGui.setObjectName("VentanaAgregarMarcaGui")
        VentanaAgregarMarcaGui.resize(369, 125)
        VentanaAgregarMarcaGui.setMaximumSize(QtCore.QSize(369, 125))
        VentanaAgregarMarcaGui.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(VentanaAgregarMarcaGui)
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
        self.txtMarca = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMarca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtMarca.setObjectName("txtMarca")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtMarca)
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
        VentanaAgregarMarcaGui.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaAgregarMarcaGui)
        QtCore.QMetaObject.connectSlotsByName(VentanaAgregarMarcaGui)

    def retranslateUi(self, VentanaAgregarMarcaGui):
        _translate = QtCore.QCoreApplication.translate
        VentanaAgregarMarcaGui.setWindowTitle(_translate("VentanaAgregarMarcaGui", "Agregar Marca"))
        self.label_2.setText(_translate("VentanaAgregarMarcaGui", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">AGREGAR MARCA</span></p></body></html>"))
        self.label.setText(_translate("VentanaAgregarMarcaGui", "Marca:"))
        self.btnAgregar.setText(_translate("VentanaAgregarMarcaGui", "Agregar"))
        self.btnCancelar.setText(_translate("VentanaAgregarMarcaGui", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaAgregarMarcaGui = QtWidgets.QMainWindow()
    ui = Ui_VentanaAgregarMarcaGui()
    ui.setupUi(VentanaAgregarMarcaGui)
    VentanaAgregarMarcaGui.show()
    sys.exit(app.exec_())

