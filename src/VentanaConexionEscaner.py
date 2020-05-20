from PyQt5.QtWidgets import QMainWindow,QDesktopWidget
from VentanasGui.VentanaAjustarEscanerGui import Ui_VentanaAjustarEscanerGui
from Herramientas.DireccionIp import DireccionIp
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class VentanaConexionEscaner(QMainWindow, Ui_VentanaAjustarEscanerGui):
    senal = pyqtSignal()
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()

    def iniciar(self):
        self.centrarPantalla()
        self.conectoresEventos()
#        self.objIp = DireccionIp()
        self.txtDireccionSocket.setText(DireccionIp().get_DirrecionIp())



    def algo(self):
        print("adios")

    def conectoresEventos(self):
        self.btnAceptar.clicked.connect(self.cerrar)

    def centrarPantalla(self):
        """
        Referencia = https://pythonprogramminglanguage.com/pyqt5-center-window/
        """
        qtRect = self.frameGeometry()
        point = QDesktopWidget().availableGeometry().center()
        qtRect.moveCenter(point)
        self.move(qtRect.topLeft())

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.senal.emit()

    def cerrar(self):
        self.senal.emit()
        self.close()