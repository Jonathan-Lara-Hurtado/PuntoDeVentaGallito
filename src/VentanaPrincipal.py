from PyQt5.QtWidgets import QApplication
from  PyQt5.QtWidgets import QMainWindow,QAction,QMenu
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout,QWidget,QDesktopWidget
from PyQt5.QtCore import Qt
from  PyQt5.QtCore import QTimer
import os
import subprocess
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
from Herramientas.Conector import ConexionBd
from PyQt5.QtWidgets import QPushButton
from VentanaLogin import VentanaLogin
from VentanaConfirmacionPago import VentanaConfirmacionPago
from VentanaProveedor import VentanaAgregarProveedor
from VentanaAgregarEmpleado import VentanaAgregarEmpleado
from Herramientas.ListaObjeto import ListaObjetos
from Herramientas.Modelos import DetalleCompra
from VentanaIva import VentanaAgregarIva


class VentanaPrincipal(QMainWindow,Ui_VentanaPricipal):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.UsuarioInformacion = []

        self.listaMarca = ListaObjetos(tabla="marca")
        self.listaMarca.listarObjetos()
        self.listaProductos = ListaObjetos(tabla="producto")
        self.listaProductos.listarObjetos()
        self.listaProveedor = ListaObjetos(tabla="proveedor")
        self.listaProveedor.listarObjetos()
        self.listaCarrito = ListaObjetos(tabla="addDetalleCompar")
        self.listaCarrito.listarObjetos()
        self.listaTmp = []




        self.listaBusqueda =[]
        self.botenesDescripcion = []
        self.btnBloquear.clicked.connect(self.bloquearTerminal)
        self.btnAddProducto.clicked.connect(self.eventoAgregarCarrito)
        self.btnQuitarProducto.clicked.connect(self.eventoQuitarCarrito)
        self.btnCancelarPago.clicked.connect(self.eventoCancelarCarrito)
        self.btnPago.clicked.connect(self.eventoPagar)
        #region Menubar
        self.BarraMenu.triggered[QAction].connect(self.eventoBarraMenu)
        #endregion
        # region EventoClickTablaProductos
        self.tablaProductos.cellClicked.connect(self.clickTablaProductos)
        self.tablaProductosFila = -1
        self.estadoTablaProducto = True
        #self.tablaProductos.clicked.connect(self.senaltabla)
        self.tablaProductosVenta.cellClicked.connect(self.clicktablaProductosVenta)
        # endregion
        self.txtBusquedaProductos.textChanged.connect(self.eventoBusqueda)
        self.vl = VentanaLogin()
        self.vl.setWindowFlag(Qt.WindowCloseButtonHint, True)
        self.vl.btnAceptar.clicked.connect(self.eventoLogin)
        self.inicio()

    def actualizaIva(self):
        self.conexion = ConexionBd()
        ivatmp = int(self.conexion.datos("select * from iva").fetchall()[0][1])
        print(ivatmp)
        self.listaCarrito.iva = ivatmp
        self.txtIva.setText("<html>" + "<body>" + "<p>" + "<span style=" + "font-weight:600;>" + str(
            self.listaCarrito.iva) + "% </span>" + "</p>" + "</body>" + "</html>")


    def eventoTicket(self):
        self.eventoCancelarCarrito()
        self.vTicke = VentanaDocumentacion()
        SO = platform.system()
        if SO == 'Linux':
            self.url = os.path.join(os.getcwd(),"Ticket.pdf")
            self.url = "file://" + self.url
            self.libreria = os.path.join(os.getcwd(), "Documentacion","pdfjs" ,"web","viewer.html")
            self.libreria = "file://" + self.libreria
        elif SO == 'Windows':
            self.url = "file:///" + os.getcwd() + "/Documentacion" + "/index.html"
            self.url = self.url.replace(chr(92), chr(47))

        self.vTicke.setWindowTitle("Ticket de Compra")
        self.vTicke.NavegadorVisor.load(QUrl.fromUserInput('%s?file=%s' % (self.libreria, self.url)))

        self.vTicke.show()


    def eventoPagar(self):
        vConfirmacion = VentanaConfirmacionPago()
        vConfirmacion.senal.connect(self.eventoTicket)
        vConfirmacion.darListaDetalles(self.listaCarrito)
        vConfirmacion.darUsuario(self.UsuarioInformacion)
        vConfirmacion.exec_()


    def eventoAgregarCarrito(self):
        if self.estadoTablaProducto:
            tmp = [0,self.listaTmp.idproducto,
                   self.listaTmp.precioventa,1]
            self.listaCarrito.addCompra(tmp)
            self.cargarDatosTablaVentas(lista = self.listaCarrito.lista)
        else:
            tmp = [0, self.listaTmp.idproducto,
                   self.listaTmp.precioventa, 1]
            self.listaCarrito.addCompra(tmp)
            self.cargarDatosTablaVentas(lista=self.listaCarrito.lista)


    def eventoCancelarCarrito(self):
        self.listaCarrito.limpiar()
        self.tablaProductosVenta.setRowCount(0)
        self.txtPrecioFinal.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">-------------</span></p></body></html>")

    def eventoQuitarCarrito(self):
        if self.estadoTablaProducto == False:
            tmp = [0, self.listaTmp.idproducto,
                   self.listaTmp.precioventa, 1]
            self.listaCarrito.quitarCompra(tmp)
            self.cargarDatosTablaVentas(lista=self.listaCarrito.lista)

    def bloquearTerminal(self,t):
        self.sesiones()

    def sesiones(self):
        if self.UsuarioInformacion != []:
            self.UsuarioInformacion = []
            self.BarraMenu.hide()
            self.botonesSistema(False)
            self.vl.exec_()
            self.limpiarLogin()
        else:

            self.vl.exec_()
            self.limpiarLogin()


    def limpiarLogin(self):
        self.vl.txtUsuario.setText("")
        self.vl.txtpass.setText("")
        self.vl.mensajeError.setText("")


    def eventoLogin(self):
        correo = self.vl.txtUsuario.text()
        passw = self.vl.txtpass.text()
        con = ConexionBd()
        resultado = con.usuarioValidacion(correo=correo, password=passw)
        if resultado[0]:
            self.vl.hide()
            self.botonesSistema(True)
            self.UsuarioInformacion = resultado[1][0]
            self.cargarDatosTablaProductos()
            self.actualizaIva()
            if self.UsuarioInformacion[5] == "Gerente":
                self.BarraMenu.show()
        else:
            self.vl.mensajeError.setText("Error de autentificacion")

    def clickTablaProductos(self,t,r):
        self.tablaProductosVenta.clearSelection()
        id = self.tablaProductos.item(t,0).text()
        self.listaTmp= self.listaProductos.busquedaProducto(id)
        self.estadoTablaProducto = True

    def clicktablaProductosVenta(self,t,r):
        self.tablaProductos.clearSelection()
        id = self.tablaProductosVenta.item(t, 1).text()
        self.listaTmp= self.listaProductos.busquedaProducto(id)
        self.estadoTablaProducto = False



    def senaltabla(self,s):
        print(s)

    def inicio(self):
        self.BarraMenu.hide()
        self.botonesSistema(False)
        #self.eventoTicket()

    def eventoBarraMenu(self,t):
        res = t.objectName()
        if res == "actionproductoalta":
            self.vAlta =VentanaAgregarProductos()
            self.vAlta.darCategoria(self.listaMarca.lista)
            self.vAlta.darProvedor(self.listaProveedor.lista)
            self.vAlta.senal.connect(self.eventoActualizar)
            self.vAlta.show()
        elif res == "actionMarcaalta":
            self.vMarca = VentanaAgregarMarca()
            self.vMarca.senal.connect(self.eventoActualizar)
            self.vMarca.show()
        elif res == "actionProveedor":
            self.vProveedor = VentanaAgregarProveedor()
            self.vProveedor.senal.connect(self.eventoActualizar)
            self.vProveedor.show()
        elif res == "actionEmpleado":
            self.vEmpleado = VentanaAgregarEmpleado()
            self.vEmpleado.show()
        elif res == "actionIva":
            self.vIva = VentanaAgregarIva()
            self.vIva.senal.connect(self.actualizaIva)
            self.vIva.show()
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
        self.listaProveedor.actualizarListaBD()
        self.cargarDatosTablaProductos()


    def eventoBusqueda(self,r):
        self.listaBusqueda = self.listaProductos.busqueda(r)
        self.cargarDatosTablaProductos(lista=self.listaBusqueda)


    def cargarDatosTablaVentas(self, lista =""):
        lista = lista
        self.tablaProductosVenta.setRowCount(0)
        contadorR = 0
        for row in lista:
            self.tablaProductosVenta.insertRow(contadorR)
            self.tablaProductosVenta.setItem(contadorR, 0, QTableWidgetItem(str(row.idventa)))
            self.tablaProductosVenta.setItem(contadorR, 1, QTableWidgetItem(str(row.idproducto)))
            self.tablaProductosVenta.setItem(contadorR, 2, QTableWidgetItem(str(row.cantidad)))
            self.tablaProductosVenta.setItem(contadorR, 3, QTableWidgetItem(str(row.precio)))
            self.tablaProductosVenta.setItem(contadorR, 4, QTableWidgetItem(str(row.subtotal)))

            contadorR += 1

        self.repaint()
        self.update()
        costoFinal = self.listaCarrito.totalPrecio()


        if costoFinal > 0:
            texto ="<html>"+"<body>"+"<p>"+"<span style="+ "font-weight:600;>"+str(costoFinal) +"</span>"+"</p>"+"</body>"+"</html>"
            self.txtPrecioFinal.setText(texto)
        else:
            self.txtPrecioFinal.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">-------------</span></p></body></html>")
         #   self.txtIva.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">-------------</span></p></body></html>")

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
            self.tablaProductos.setItem(contadorR,0,QTableWidgetItem(str(row.idproducto)))
            self.tablaProductos.setItem(contadorR, 1, QTableWidgetItem(str(row.nombreproducto)))
            self.tablaProductos.setItem(contadorR, 2, QTableWidgetItem(str(row.existencia)))
            self.tablaProductos.setItem(contadorR, 3, QTableWidgetItem(str(row.precioventa)))
            self.tablaProductos.setCellWidget(contadorR, 4, b)
            contadorR += 1
        self.repaint()
        self.update()



    def check_clicked(self):
#        print("{}%".format(self.sender().objectName()))
        if self.txtBusquedaProductos.text() == "":
            for i in self.botenesDescripcion:
                if i[0].objectName() == self.sender().objectName():
                    self.vOP = VentanaOpcionesProductos()
                    self.vOP.darValores(self.listaProductos.lista[i[1]])
                    self.vOP.darMarca(self.listaMarca.lista)
                    self.vOP.darProvedor(self.listaProveedor.lista)
                    self.vOP.show()
        else:
            for i in self.botenesDescripcion:
                if i[0].objectName() == self.sender().objectName():
                    self.vOP = VentanaOpcionesProductos()
                    self.vOP.darValores(self.listaBusqueda[i[1]])
                    self.vOP.darMarca(self.listaMarca.lista)
                    self.vOP.darProvedor(self.listaProveedor.lista)
                    self.vOP.show()

    def botonesSistema(self,f):
        self.btnPago.setEnabled(f)
        self.btnCancelarPago.setEnabled(f)
        self.btnAddProducto.setEnabled(f)
        self.btnQuitarProducto.setEnabled(f)



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
