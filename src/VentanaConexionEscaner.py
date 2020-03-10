from PyQt5.QtWidgets import QMainWindow,QDesktopWidget
from VentanasGui.VentanaAjustarEscanerGui import Ui_VentanaAjustarEscanerGui
from Herramientas.DireccionIp import DireccionIp

class VentanaConexionEscaner(QMainWindow, Ui_VentanaAjustarEscanerGui):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()

    def iniciar(self):
        self.centrarPantalla()
        self.conectoresEventos()
#        self.objIp = DireccionIp()
        self.txtDireccionSocket.setText(DireccionIp().get_DirrecionIp())

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

    def cerrar(self):
        self.close()