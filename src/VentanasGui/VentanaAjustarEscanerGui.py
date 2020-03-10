# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ArchivosUi/VentanaAjustarEscanerGui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaAjustarEscanerGui(object):
    def setupUi(self, VentanaAjustarEscanerGui):
        VentanaAjustarEscanerGui.setObjectName("VentanaAjustarEscanerGui")
        VentanaAjustarEscanerGui.resize(505, 408)
        VentanaAjustarEscanerGui.setMinimumSize(QtCore.QSize(505, 408))
        VentanaAjustarEscanerGui.setMaximumSize(QtCore.QSize(505, 408))
        VentanaAjustarEscanerGui.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(VentanaAjustarEscanerGui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 0, 261, 41))
        self.label.setStyleSheet("color: rgb(238, 238, 236);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 161, 31))
        self.label_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 241, 31))
        self.label_3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 451, 31))
        self.label_4.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_4.setObjectName("label_4")
        self.txtDireccionSocket = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDireccionSocket.setGeometry(QtCore.QRect(30, 130, 421, 25))
        self.txtDireccionSocket.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDireccionSocket.setObjectName("txtDireccionSocket")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 481, 17))
        self.label_5.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_5.setObjectName("label_5")
        self.texEditBarras = QtWidgets.QTextEdit(self.centralwidget)
        self.texEditBarras.setGeometry(QtCore.QRect(20, 210, 471, 121))
        self.texEditBarras.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.texEditBarras.setObjectName("texEditBarras")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 461, 17))
        self.label_6.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_6.setObjectName("label_6")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(390, 350, 89, 25))
        self.btnAceptar.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.btnAceptar.setObjectName("btnAceptar")
        VentanaAjustarEscanerGui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VentanaAjustarEscanerGui)
        self.statusbar.setObjectName("statusbar")
        VentanaAjustarEscanerGui.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaAjustarEscanerGui)
        QtCore.QMetaObject.connectSlotsByName(VentanaAjustarEscanerGui)

    def retranslateUi(self, VentanaAjustarEscanerGui):
        _translate = QtCore.QCoreApplication.translate
        VentanaAjustarEscanerGui.setWindowTitle(_translate("VentanaAjustarEscanerGui", "EscanerApp"))
        self.label.setText(_translate("VentanaAjustarEscanerGui", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Conexion con la App Escaner</span></p></body></html>"))
        self.label_2.setText(_translate("VentanaAjustarEscanerGui", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Pasos a segir:</span></p></body></html>"))
        self.label_3.setText(_translate("VentanaAjustarEscanerGui", "1.Descague la app de la play store"))
        self.label_4.setText(_translate("VentanaAjustarEscanerGui", "2.Abra la app e ingrese en el primer cuadro la siguiente direccion"))
        self.label_5.setText(_translate("VentanaAjustarEscanerGui", "3.De click en el boton conectar de su Dispositivo y empieze a escanear"))
        self.label_6.setText(_translate("VentanaAjustarEscanerGui", "Si todo salio bien lo que escane aparecera en el siguiente recuadro"))
        self.btnAceptar.setText(_translate("VentanaAjustarEscanerGui", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaAjustarEscanerGui = QtWidgets.QMainWindow()
    ui = Ui_VentanaAjustarEscanerGui()
    ui.setupUi(VentanaAjustarEscanerGui)
    VentanaAjustarEscanerGui.show()
    sys.exit(app.exec_())

