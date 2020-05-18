from PyQt5.QtCore import *


class HiloTiempo(QThread):
    signal = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)
        self.i=0


    def run(self):
        while self.i < 2:
            self.i = self.i +1
            self.signal.emit(self.i)
            QThread.sleep(1)
