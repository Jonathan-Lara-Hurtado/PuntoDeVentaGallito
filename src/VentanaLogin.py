from PyQt5.QtWidgets import QMainWindow,QLayout

from PyQt5.QtWidgets import QApplication
from  PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget
from PyQt5.QtCore import Qt,QTimer



from VentanasGui.VentanaLogin import Ui_VentanaUiLogi

class VentanaLogin(QDialog, Ui_VentanaUiLogi):
    def __init__(self, *args, **kwargs):
        QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
