import platform
if platform.system() == 'Linux':
    from VentanasGui.linux.VentanaNavegadorDocumentacionGui import Ui_NavegadorDocumentacion
elif platform.system() == 'Windows':
    from VentanasGui.windows.VentanaNavegadorDocumentacionGui import Ui_NavegadorDocumentacion
from PyQt5.QtWidgets import QMainWindow,QDesktopWidget

class VentanaDocumentacion(QMainWindow, Ui_NavegadorDocumentacion):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.iniciar()

    def iniciar(self):
        self.centrarPantalla()

    def centrarPantalla(self):
        """
        Referencia = https://pythonprogramminglanguage.com/pyqt5-center-window/
        """
        qtRect = self.frameGeometry()
        point = QDesktopWidget().availableGeometry().center()
        qtRect.moveCenter(point)
        self.move(qtRect.topLeft())
