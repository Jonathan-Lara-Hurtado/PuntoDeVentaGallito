from PyQt5.QtCore import *
from .Redes import Redes
import socket

class HiloBarra(QThread):
    sinal = pyqtSignal(str)
    def __init__(self):
        QThread.__init__(self)
        self.direccion = Redes()
        self.host = str(self.direccion.get_DireccionIp())
        self.port = 12345
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))


    def run(self):
        while True:
            self.s.listen(1)
            c,addr = self.s.accept()
            data = c.recv(1024)
            self.sinal.emit(data.decode('utf-8'))