from PyQt5.QtWidgets import QApplication
from  PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget
from PyQt5.QtCore import Qt,QTimer,QThread
import os
import random

from SplashScreen import Ui_SplashScreen
from Herramientas.hilotiempo import HiloTiempo
from VentanaPrincipal import VentanaPrincipal

class VentanaSplash(QMainWindow , Ui_SplashScreen):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()
        self.i=0

    def iniciar(self):
        self.centrarPantalla()
        self.quitarBarraTitulo()
#        self.principal = VentanaPrincipal()
        #region hiloTiempo
        self.hilotiempo = HiloTiempo()
        self.hilotiempo.signal.connect(self.contador)
        self.hilotiempo.start()
        #endregion


    def contador(self,s):
        listaCargaDatos = ["Cargando Aplicacion",
                           "Configurando Redes",
                           "Hackeando bitacora de la uaem",
                           ".............................."
                           ]
        if(s != 2):
            self.txtstatusBar.setText(random.choice(listaCargaDatos))
        else:
            self.hide()
            self.principal = VentanaPrincipal()
            #self.principal.showFullScreen()
            self.principal.show()

    def centrarPantalla(self):
        """
        Referencia = https://pythonprogramminglanguage.com/pyqt5-center-window/
        """
        qtRect = self.frameGeometry()
        point = QDesktopWidget().availableGeometry().center()
        qtRect.moveCenter(point)
        self.move(qtRect.topLeft())

    def quitarBarraTitulo(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)


if __name__ == "__main__":
    app = QApplication([])
    ven = VentanaSplash()
    ven.show()
    app.exec_()
