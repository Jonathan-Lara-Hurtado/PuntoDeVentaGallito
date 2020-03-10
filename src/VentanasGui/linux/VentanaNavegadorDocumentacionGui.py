# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ArchivosUi/VentanaNavegadorDocumentacionGui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebKitWidgets import *

class Ui_NavegadorDocumentacion(object):
    def setupUi(self, NavegadorDocumentacion):
        NavegadorDocumentacion.setObjectName("NavegadorDocumentacion")
        NavegadorDocumentacion.resize(787, 561)
        NavegadorDocumentacion.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(NavegadorDocumentacion)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.NavegadorVisor = QWebView(self.centralwidget)
        self.NavegadorVisor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NavegadorVisor.setUrl(QtCore.QUrl("about:blank"))
        self.NavegadorVisor.setObjectName("NavegadorVisor")
        self.gridLayout.addWidget(self.NavegadorVisor, 0, 0, 1, 1)
        NavegadorDocumentacion.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NavegadorDocumentacion)
        self.statusbar.setObjectName("statusbar")
        NavegadorDocumentacion.setStatusBar(self.statusbar)

        self.retranslateUi(NavegadorDocumentacion)
        QtCore.QMetaObject.connectSlotsByName(NavegadorDocumentacion)

    def retranslateUi(self, NavegadorDocumentacion):
        _translate = QtCore.QCoreApplication.translate
        NavegadorDocumentacion.setWindowTitle(_translate("NavegadorDocumentacion", "Documentacion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NavegadorDocumentacion = QtWidgets.QMainWindow()
    ui = Ui_NavegadorDocumentacion()
    ui.setupUi(NavegadorDocumentacion)
    NavegadorDocumentacion.show()
    sys.exit(app.exec_())

