# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ArchivosUi/VentanaAcercaDeGui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaAcercaDeGui(object):
    def setupUi(self, VentanaAcercaDeGui):
        VentanaAcercaDeGui.setObjectName("VentanaAcercaDeGui")
        VentanaAcercaDeGui.resize(511, 327)
        VentanaAcercaDeGui.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(VentanaAcercaDeGui)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtAcercaDe = QtWidgets.QLabel(self.centralwidget)
        self.txtAcercaDe.setStyleSheet("color: rgb(238, 238, 236);")
        self.txtAcercaDe.setObjectName("txtAcercaDe")
        self.verticalLayout.addWidget(self.txtAcercaDe)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.btnSalir.setObjectName("btnSalir")
        self.horizontalLayout.addWidget(self.btnSalir)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        VentanaAcercaDeGui.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaAcercaDeGui)
        QtCore.QMetaObject.connectSlotsByName(VentanaAcercaDeGui)

    def retranslateUi(self, VentanaAcercaDeGui):
        _translate = QtCore.QCoreApplication.translate
        VentanaAcercaDeGui.setWindowTitle(_translate("VentanaAcercaDeGui", "AcercaDe"))
        self.txtAcercaDe.setText(_translate("VentanaAcercaDeGui", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Univesirad Autonoma de México</span></p><p align=\"center\"><span style=\" font-weight:600;\">Integrantes:</span></p><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">*Lopez Huerta Brando Yosue</span></p><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">*Ramirez Guzman Yalser Isaac</span></p><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">*Flores Alvares Ulises Alberto</span></p><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">*Lara Hurtado Jonathan Abimael</span></p><p align=\"right\"><span style=\" font-weight:600; font-style:italic;\">Version 0.1</span></p><p align=\"right\"><span style=\" font-weight:600; font-style:italic;\">by larahurtadocorp</span></p></body></html>"))
        self.btnSalir.setText(_translate("VentanaAcercaDeGui", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaAcercaDeGui = QtWidgets.QMainWindow()
    ui = Ui_VentanaAcercaDeGui()
    ui.setupUi(VentanaAcercaDeGui)
    VentanaAcercaDeGui.show()
    sys.exit(app.exec_())

