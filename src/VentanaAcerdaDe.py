from PyQt5.QtWidgets import QMainWindow,QLayout

from PyQt5.QtWidgets import QApplication
from  PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget
from PyQt5.QtCore import Qt,QTimer


from VentanasGui.VentanaAcercaDeGui import Ui_VentanaAcercaDeGui


class VentanaAcercaDe(QMainWindow, Ui_VentanaAcercaDeGui):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnSalir.clicked.connect(self.cerrar)
        self.centrarPantalla()

    def cerrar(self):
        self.close()

    def centrarPantalla(self):
        """
        Referencia = https://pythonprogramminglanguage.com/pyqt5-center-window/
        """
        qtRect = self.frameGeometry()
        point = QDesktopWidget().availableGeometry().center()
        qtRect.moveCenter(point)
        self.move(qtRect.topLeft())