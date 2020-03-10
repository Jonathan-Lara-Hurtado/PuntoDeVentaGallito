from .ConexionBD import BD
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
            bd = BD(tabla=self.tabla)
            for i in bd.consulta():
                self.lista.append(Marca(idMarca=i[0],marca=i[1]))
        elif self.tabla is "productos":
            bd = BD(tabla=self.tabla)
            for i in bd.consulta():
                self.lista.append(Producto(i[1],i[2],i[3],i[4],i[5],i[6],i[0]))

    def busqueda(self,valor):
        listatmp = []
        if valor is "":
            return self.lista
        else:
            for li in self.lista:
                for li2 in li.__dict__:
                    if valor == str(li.__dict__[li2]):
                        listatmp.append(li)
        return listatmp

    def actualizarListaBD(self):
        self.listarObjetos()


