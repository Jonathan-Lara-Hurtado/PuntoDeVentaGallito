from .ConexionBD import BD

class Producto:

    def __init__(self, nombre, codigoBarra, descripcion, stock, precio, marca, id="null"):
        self.__id = id
        self.__nombre = nombre
        self.__codigoBarra = codigoBarra
        self.__descripcion = descripcion
        self.__stock = stock
        self.__precio = precio
        self.__marca = marca

    # region gett/sett

    @property
    def id(self):
        return self.__id 
    
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nombre(self):
        return self.__nombre 
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def codigoBarra(self):
        return self.__codigoBarra

    @codigoBarra.setter
    def codigoBarra(self, value):
        self.__codigoBarra = value

    @property
    def descripcion(self):
        return self.__descripcion 
    
    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value
    
    @property
    def stock(self):
        return self.__stock 
    
    @stock.setter
    def stock(self, value):
        self.__stock = value
    
    @property
    def precio(self):
        return self.__precio 
    
    @precio.setter
    def precio(self, value):
        self.__precio = value
    
    @property
    def marca(self):
        return self.__marca 
    
    @marca.setter
    def marca(self, value):
        self.__marca = value

    # endregion

    def __str__(self):
        return self.nombre

    def listarAtributos(self):
        return [self.id, self.nombre, self.codigoBarra, self.descripcion,
                self.stock, self.precio, self.marca]

    def alta(self):
        bd = BD(tabla="productos")
        bd.alta(self.listarAtributos())
        bd.cerrarConexion()


class Marca:
    def __init__(self, idMarca=1, marca=""):
        self.__idMarca = idMarca
        self.__marca = marca
        self.__tabla = "marca"

    # region gett/sett
    @property
    def idMarca(self):
        return self.__idMarca

    @idMarca.setter
    def idMarca(self, value):
        self.__idMarca = value

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        self.__marca = value

    @property
    def tabla(self):
        return self.__tabla

    @tabla.setter
    def tabla(self, value):
        self.__tabla = value

    # endregion

    def __str__(self):
        return str(self.marca)

    def listarAtributos(self):
        return [self.idMarca, self.marca]

    def alta(self):
        bd = BD(tabla="marca")
        bd.alta(self.listarAtributos())
        bd.cerrarConexion()

    def eliminar(self):
        bd = BD(tabla="marca")
        bd.eliminar(self.idMarca)
        bd.cerrarConexion()
