from typing import Any

from .ConexionBD import BD
from .Conector import ConexionBd

class Empleado:
    def __init__(self,idempleado,nombre,apellidopaterno,apellidomaterno,edad,tipoempleado,contrasena,fechaContratacion,direccion,correo):
        self.__idempleado =idempleado
        self.__nombre = nombre
        self.__apellidopaterno = apellidopaterno
        self.__apellidomaterno = apellidomaterno
        self.__edad = edad
        self.__tipoempleado = tipoempleado
        self.__contrasena = contrasena
        self.__fechaContratacion = fechaContratacion
        self.__direccion = direccion
        self.__correo = correo

    @property
    def idempleado(self):
        return self.__idempleado 
    
    @idempleado.setter
    def idempleado(self, value):
        self.__idempleado = value
    
    @property
    def nombre(self):
        return self.__nombre 
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @property
    def apellidopaterno(self):
        return self.__apellidopaterno 
    
    @apellidopaterno.setter
    def apellidopaterno(self, value):
        self.__apellidopaterno = value
        
    @property
    def apellidomaterno(self):
        return self.__apellidomaterno 
    
    @apellidomaterno.setter
    def apellidomaterno(self, value):
        self.__apellidomaterno = value
        
        
    @property
    def edad(self):
        return self.__edad 
    
    @edad.setter
    def edad(self, value):
        self.__edad = value
    
    @property
    def tipoempleado(self):
        return self.__tipoempleado 
    
    @tipoempleado.setter
    def tipoempleado(self, value):
        self.__tipoempleado = value
    
    @property
    def contrasena(self):
        return self.__contrasena 
    
    @contrasena.setter
    def contrasena(self, value):
        self.__contrasena = value
        
    @property
    def fechaContratacion(self):
        return self.__fechaContratacion 
    
    @fechaContratacion.setter
    def fechaContratacion(self, value):
        self.__fechaContratacion = value


    @property
    def direccion(self):
        return self.__direccion 
    
    @direccion.setter
    def direccion(self, value):
        self.__direccion = value
        
    @property
    def correo(self):
        return self.__correo 
    
    @correo.setter
    def correo(self, value):
        self.__correo = value

    def __str__(self):
        return str(self.correo)

    def listarAtributos(self):
        return [self.idempleado,self.nombre,
                self.apellidopaterno,self.apellidomaterno,
                self.edad, self.tipoempleado, self.contrasena,
                self.fechaContratacion,self.direccion,self.correo]

class Producto:

    def __init__(self, idproducto, idmarca, idProvedor, nombreproducto, codigoBarra, precioventa, descripcion,existencia):
        self.__idproducto = idproducto
        self.__idmarca = idmarca
        self.__idProvedor = idProvedor
        self.__nombreproducto = nombreproducto
        self.__codigoBarra = codigoBarra
        self.__precioventa = precioventa
        self.__descripcion = descripcion
        self.__existencia = existencia

    # region gett/sett

    @property
    def idproducto(self):
        return self.__idproducto 
    
    @idproducto.setter
    def idproducto(self, value):
        self.__idproducto = value
        
    @property
    def idmarca(self):
        return self.__idmarca 
    
    @idmarca.setter
    def idmarca(self, value):
        self.__idmarca = value
        
    @property
    def idProvedor(self):
        return self.__idProvedor 
    
    @idProvedor.setter
    def idProvedor(self, value):
        self.__idProvedor = value

    @property
    def nombreproducto(self):
        return self.__nombreproducto 
    
    @nombreproducto.setter
    def nombreproducto(self, value):
        self.__nombreproducto = value

    @property
    def codigoBarra(self):
        return self.__codigoBarra 
    
    @codigoBarra.setter
    def codigoBarra(self, value):
        self.__codigoBarra = value
        
    @property
    def precioventa(self):
        return self.__precioventa 
    
    @precioventa.setter
    def precioventa(self, value):
        self.__precioventa = value
    
    @property
    def descripcion(self):
        return self.__descripcion 
    
    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value

    @property
    def existencia(self):
        return self.__existencia 
    
    @existencia.setter
    def existencia(self, value):
        self.__existencia = value

    # endregion

    def __str__(self):
        return str(self.nombreproducto)

    def listarAtributos(self):
        return [self.idproducto,self.idmarca,
                self.idProvedor,self.nombreproducto,
                self.codigoBarra,self.precioventa,
                self.descripcion,self.existencia]



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


class Proveedor:
    def __init__(self,idproveedor, nombreCompany, nombreContacto,direccion,ciudad,region,codigopostal,pais,telefono,fax):
        self.__idproveedor =idproveedor
        self.__nombreCompany = nombreCompany
        self.__nombreContacto =nombreContacto
        self.__direccion =direccion
        self.__ciudad = ciudad
        self.__region = region
        self.__codigopostal = codigopostal
        self.__pais = pais
        self.__telefono = telefono
        self.__fax = fax

    @property
    def idproveedor(self):
        return self.__idproveedor 
    
    @idproveedor.setter
    def idproveedor(self, value):
        self.__idproveedor = value
        
    @property
    def nombreCompany(self):
        return self.__nombreCompany 
    
    @nombreCompany.setter
    def nombreCompany(self, value):
        self.__nombreCompany = value

    @property
    def nombreContacto(self):
        return self.__nombreContacto 
    
    @nombreContacto.setter
    def nombreContacto(self, value):
        self.__nombreContacto = value
    
    @property
    def direccion(self):
        return self.__direccion 
    
    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @property
    def ciudad(self):
        return self.__ciudad 
    
    @ciudad.setter
    def ciudad(self, value):
        self.__ciudad = value

    @property
    def region(self):
        return self.__region 
    
    @region.setter
    def region(self, value):
        self.__region = value

    @property
    def codigopostal(self):
        return self.__codigopostal 
    
    @codigopostal.setter
    def codigopostal(self, value):
        self.__codigopostal = value

    @property
    def pais(self):
        return self.__pais 
    
    @pais.setter
    def pais(self, value):
        self.__pais = value
        
    @property
    def telefono(self):
        return self.__telefono 
    
    @telefono.setter
    def telefono(self, value):
        self.__telefono = value
    
    @property
    def fax(self):
        return self.__fax 
    
    @fax.setter
    def fax(self, value):
        self.__fax = value
    
    def __str__(self):
        return str(self.__nombreCompany)

    def listarAtributos(self):
        return [self.idproveedor,self.nombreCompany,
                self.nombreContacto,
                self.direccion,self.ciudad,
                self.region,self.codigopostal,
                self.pais,self.telefono,
                self.fax]


class DetalleCompra:
    def __init__(self,idventa,idproducto,precio,cantidad):
        self.__idventa = idventa
        self.__idproducto = idproducto
        self.__precio = precio
        self.__cantidad = cantidad
        self.__subtotal = self.__precio * self.__cantidad
    
    @property
    def subtotal(self):
        return self.__subtotal 
    
    @subtotal.setter
    def subtotal(self, value):
        self.__subtotal = value
    
    @property
    def idventa(self):
        return self.__idventa 
    
    @idventa.setter
    def idventa(self, value):
        self.__idventa = value
        
    @property
    def idproducto(self):
        return self.__idproducto 
    
    @idproducto.setter
    def idproducto(self, value):
        self.__idproducto = value
    
    @property
    def precio(self):
        return self.__precio 
    
    @precio.setter
    def precio(self, value):
        self.__precio = value
    
    @property
    def cantidad(self):
        return self.__cantidad 
    
    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = value

    def __str__(self):
        return str(self.idproducto)

    def listarAtributos(self):
        return [self.idventa,self.idproducto,
                self.precio,self.cantidad]