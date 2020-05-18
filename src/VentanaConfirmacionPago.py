from PyQt5.QtWidgets import QMainWindow,QLayout

from PyQt5.QtWidgets import QApplication
from  PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtCore import pyqtSignal

from VentanasGui.VentanaConfirmacionPago import Ui_VentanaConfirmacionUi

class VentanaConfirmacionPago(QDialog, Ui_VentanaConfirmacionUi):

    senal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnCancelar.clicked.connect(self.cerrar)
        self.btnAceptar.clicked.connect(self.eventoAceptar)

    def eventoAceptar(self):
        self.senal.emit()
        self.close()

    def cerrar(self):
        self.close()