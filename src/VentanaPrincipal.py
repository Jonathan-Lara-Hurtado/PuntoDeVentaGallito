from PyQt5.QtWidgets import QApplication
from  PyQt5.QtWidgets import QMainWindow,QAction,QMenu
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget
from PyQt5.QtCore import Qt
from  PyQt5.QtCore import QTimer
import os
import platform
import random
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QTableWidgetItem


from VentanasGui.VentanaPricipalGui import Ui_VentanaPricipal
from VentanaAcerdaDe import VentanaAcercaDe
from VentanaDocumentacion import VentanaDocumentacion
from VentanaConexionEscaner import VentanaConexionEscaner
from VentanaAgregarProducto import VentanaAgregarProductos
from VentanaAgregarMarca import VentanaAgregarMarca
from VentanaOpcionesProductos import VentanaOpcionesProductos
from Herramientas.ListaObjeto import ListaObjetos
from PyQt5.QtWidgets import QPushButton


class VentanaPrincipal(QMainWindow,Ui_VentanaPricipal):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.listaMarca = ListaObjetos(tabla="marca")
        self.listaMarca.listarObjetos()
        self.listaProductos = ListaObjetos(tabla="productos")
        self.listaProductos.listarObjetos()
        self.listaBusqueda =[]
        self.botenesDescripcion = []
        #region Menubar
        self.BarraMenu.triggered[QAction].connect(self.eventoBarraMenu)
        #endregion
        self.tablaProductos.cellClicked.connect(self.clickTablaProductos)
        self.tablaProductos.clicked.connect(self.senaltabla)
        self.txtBusquedaProductos.textChanged.connect(self.eventoBusqueda)
        self.inicio()


    def clickTablaProductos(self,t,r):
        print(t,r)

    def senaltabla(self,s):
        print(s)

    def inicio(self):
        self.cargarDatosTablaProductos()


    def eventoBarraMenu(self,t):
        res = t.objectName()
        if res == "actionproductoalta":
            self.vAlta =VentanaAgregarProductos()
            self.vAlta.darCategoria(self.listaMarca.lista)
            self.vAlta.senal.connect(self.eventoActualizar)
            self.vAlta.show()
        elif res == "actionMarcaalta":
            self.vMarca = VentanaAgregarMarca()
            self.vMarca.senal.connect(self.eventoActualizar)
            self.vMarca.show()
        elif res == "actionAcerca_de":
            self.d = VentanaAcercaDe()
            self.d.show()
        elif res == "actionDocumentacion":
            self.documentacion = VentanaDocumentacion()
            SO = platform.system()
            if SO == 'Linux':
                self.url = os.path.join(os.getcwd(), "Documentacion", "index.html")
                self.url = "file://" + self.url
            elif SO == 'Windows':
                self.url = "file:///" + os.getcwd() + "/Documentacion" + "/index.html"
                self.url = self.url.replace(chr(92), chr(47))
            self.documentacion.NavegadorVisor.load(QUrl(self.url))
            self.documentacion.show()
        elif res == "actionEscanerApp":
            self.vHA = VentanaConexionEscaner()
            self.vHA.show()
        else:
            print("nada")

    def eventoActualizar(self):
        self.listaMarca.actualizarListaBD()
        self.listaProductos.actualizarListaBD()
        self.cargarDatosTablaProductos()

    def eventoBusqueda(self,r):
        self.listaBusqueda = self.listaProductos.busqueda(r)
        self.cargarDatosTablaProductos(lista=self.listaBusqueda)


    def cargarDatosTablaProductos(self, lista = ""):
        if lista == "":
            lista = self.listaProductos.lista
        else:
            lista = lista
        self.botenesDescripcion.clear()
        self.tablaProductos.setRowCount(0)
        contadorR = 0
        for row in lista:
            b = QPushButton()
            b.setText("Opciones")
            b.setObjectName("btn"+str(contadorR))
            b.clicked.connect(self.check_clicked)
            self.botenesDescripcion.append([b,contadorR])
            self.tablaProductos.insertRow(contadorR)
            self.tablaProductos.setItem(contadorR,0,QTableWidgetItem(str(row.id)))
            self.tablaProductos.setItem(contadorR, 1, QTableWidgetItem(str(row.nombre)))
            self.tablaProductos.setItem(contadorR, 2, QTableWidgetItem(str(row.stock)))
            self.tablaProductos.setItem(contadorR, 3, QTableWidgetItem(str(row.precio)))
            self.tablaProductos.setCellWidget(contadorR, 4, b)
            contadorR += 1
        self.repaint()
        self.update()

    """
    def cargarDatosTablaProductos(self):
        self.tablaProductos.setRowCount(0)
        self.botenesDescripcion.clear()
        contadorR =0
        for row in self.listaProductos.lista:
            b = QPushButton()
            b.setText("Opciones")
            b.setObjectName("btn"+str(contadorR))
            b.clicked.connect(self.check_clicked)
            self.botenesDescripcion.append([b,contadorR])
            self.tablaProductos.insertRow(contadorR)
            self.tablaProductos.setItem(contadorR,0,QTableWidgetItem(str(row.id)))
            self.tablaProductos.setItem(contadorR, 1, QTableWidgetItem(str(row.nombre)))
            self.tablaProductos.setItem(contadorR, 2, QTableWidgetItem(str(row.stock)))
            self.tablaProductos.setItem(contadorR, 3, QTableWidgetItem(str(row.precio)))
            self.tablaProductos.setCellWidget(contadorR, 4, b)
            contadorR += 1
        self.repaint()
        self.update()
    """

    def check_clicked(self):
#        print("{}%".format(self.sender().objectName()))
        if self.txtBusquedaProductos.text() == "":
            for i in self.botenesDescripcion:
                if i[0].objectName() == self.sender().objectName():
                    self.vOP = VentanaOpcionesProductos()
                    self.vOP.darValores(self.listaProductos.lista[i[1]])
                    self.vOP.show()
        else:
            for i in self.botenesDescripcion:
                if i[0].objectName() == self.sender().objectName():
                    self.vOP = VentanaOpcionesProductos()
                    self.vOP.darValores(self.listaBusqueda[i[1]])
                    self.vOP.show()




        """
        res = t.text()
        if res == "Acerca de":
            self.d = VentanaAcercaDe()
            self.d.show()
        elif res =="Documentacion":
            self.documentacion = VentanaDocumentacion()
            SO = platform.system()
            if SO == 'Linux':
                self.url = os.path.join(os.getcwd(), "Documentacion", "index.html")
                self.url = "file://"+self.url
            elif SO == 'Windows':
                self.url = "file:///" + os.getcwd() + "/Documentacion" + "/index.html"
                self.url = self.url.replace(chr(92), chr(47))
            self.documentacion.NavegadorVisor.load(QUrl(self.url))
            self.documentacion.show()
        elif res == "EscanerApp":
            self.vHA = VentanaConexionEscaner()
            self.vHA.show()
        """
