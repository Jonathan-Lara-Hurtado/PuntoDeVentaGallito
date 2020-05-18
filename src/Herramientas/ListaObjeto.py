from .ConexionBD import BD
from .Conector import ConexionBd
from .Modelos import *

class ListaObjetos:

    def __init__(self, tabla):
        self.__tabla = tabla
        self.__lista = []

    @property
    def tabla(self):
        return self.__tabla 
    
    @tabla.setter
    def tabla(self, value):
        self.__tabla = value
    
    @property
    def lista(self):
        return self.__lista 
    
    @lista.setter
    def lista(self, value):
        self.__lista = value

    def listarObjetos(self):
        self.lista.clear()
        if self.tabla is "marca":
            bd = ConexionBd()
            for i in bd.datos("select * from "+self.tabla):
                self.lista.append(Marca(idMarca=i[0],marca=i[1]))
        elif self.tabla is "producto":
            bd = ConexionBd()
            for i in bd.datos("select * from " + self.tabla):
                self.lista.append(Producto(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
        elif self.tabla is "proveedor":
            bd = ConexionBd()
            for i in bd.datos("select * from " + self.tabla):
                self.lista.append(Proveedor(i[0],i[1],i[2],i[3],
                                            i[4],i[5],i[6],i[7],
                                            i[8],i[9]))
        elif self.tabla is "addDetalleCompar":
            self.lista = list()

    def busqueda(self,valor):
        listatmp = []
        if valor is "":
            return self.lista
        else:
            for li in self.lista:
                if valor == str(li.idproducto) or valor == str(li.nombreproducto) or valor == str(li.codigoBarra):
                    listatmp.append(li)
        return listatmp


    def busquedaProducto(self,valor):
        if valor is "":
            return -1
        else:
            for li in self.lista:
                if valor == str(li.idproducto) or valor == str(li.codigoBarra):
                    return li


    def busquedaDetalle(self,valor):
        index = -1
        indexAprobatorio = -1
        for li in self.lista:
            index = index + 1
            if valor == li.idproducto:
                indexAprobatorio = index

        return indexAprobatorio


    def addCompra(self,ltmp):
        if self.lista == []:
            self.lista.append(DetalleCompra(ltmp[0], ltmp[1], ltmp[2], ltmp[3]))
        else:
            index =self.busquedaDetalle(ltmp[1])
            if index != -1:
                existenciA =self.lista[index].cantidad
                self.lista[index] = DetalleCompra(ltmp[0],ltmp[1],ltmp[2],existenciA+ltmp[3])
            else:
                self.lista.append(DetalleCompra(ltmp[0], ltmp[1], ltmp[2], ltmp[3]))



    def totalPrecio(self):
        suma=0
        for li in self.lista:
            suma = suma + li.subtotal
        return suma

    def actualizarListaBD(self):
        self.listarObjetos()

    def limpiar(self):
        self.lista.clear()

