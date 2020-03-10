# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ArchivosUi/SplashScreen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.setWindowModality(QtCore.Qt.NonModal)
        SplashScreen.resize(375, 305)
        SplashScreen.setMaximumSize(QtCore.QSize(386, 396))
        SplashScreen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 255));")
        self.verticalLayoutWidget = QtWidgets.QWidget(SplashScreen)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 270, 381, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtstatusBar = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.txtstatusBar.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.txtstatusBar.setText("")
        self.txtstatusBar.setObjectName("txtstatusBar")
        self.verticalLayout.addWidget(self.txtstatusBar)
        self.label = QtWidgets.QLabel(SplashScreen)
        self.label.setGeometry(QtCore.QRect(0, 10, 371, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Recursos/LogoSplash.png"))
        self.label.setObjectName("label")

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QWidget()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())

