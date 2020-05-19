import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class GraficaVentas:

    def __init__(self, N= 31, datos = [], titulo="",etiquetaIzquierda="Numero Compras", etiquetaAbajo="Dias"):

        self.N = N
        self.ind = np.arange(self.N)  # the x locations for the groups
        self.width = 0.35  # the width of the bars
        self.fig, self.ax = plt.subplots()
        self.fig.canvas.set_window_title('Ventas')
        self.ax.set_ylabel(etiquetaIzquierda)
        self.ax.set_title(titulo)
        self.ax.set_xlabel(etiquetaAbajo)
        self.ax.set_xticks(self.ind + self.width / 2)
        self.datos = datos
        self.ejeX()
        self.barra()


    def barra(self):
        lista = []
        for i in range(1, self.N+1):
            lista.append(1)
        lista2 = []
        for i in range(1, self.N+1):
            lista2.append(i)
        rectangulo = self.ax.bar(self.ind,self.datos,self.width,color='b',yerr=lista)


    def ejeX(self):
        lista = []
        for i in range(1,self.N+1):
            lista.append(i)
        self.ax.set_xticklabels(lista)


    def show(self):
        red_patch = mpatches.Patch(color='blue', label='Ventas')
        plt.legend(handles=[red_patch])
        plt.show()



"""
lista = []
for i in range(1,32):
    lista.append(i)

v = GraficaVentas(datos=lista)

v.show()
"""