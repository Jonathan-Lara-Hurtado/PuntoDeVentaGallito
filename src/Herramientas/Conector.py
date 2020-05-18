import mysql.connector
from datetime import date, datetime, timedelta


class ConexionBd:
    def __init__(self,user='gallito',passw='12345',host='127.0.0.1',db='gallitonegro'):
        self.cnx = mysql.connector.connect(
            user=user,
            password =passw,
            host=host,
            database=db,
        )



    def insertarProducto(self,idmarca,idProvedor,nombreproducto,codigoBarra,precioventa,descripcion,existencia):
        cursor = self.cnx.cursor()
        add_producto = ("Insert into producto"
                       "(idmarca,idProvedor,nombreproducto,codigoBarra,precioventa,descripcion,existencia)"
                       "values (%s, %s, %s, %s, %s, %s, %s)")
        data_producto = (idmarca, idProvedor, nombreproducto, codigoBarra, precioventa, descripcion, existencia)
        cursor.execute(add_producto, data_producto)
        self.cnx.commit()
        cursor.close()


    def insertarProvedor(self,nombreCompany,nombreContacto,direccion,ciudad,region,codigopostal,pais,telefono,fax):
        cursor = self.cnx.cursor()
        add_provedor = ("Insert into proveedor"
                       "(nombreCompany,nombreContacto,direccion,ciudad,region,codigopostal,pais,telefono,fax)"
                       "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_provedor = (nombreCompany, nombreContacto, direccion, ciudad, region, codigopostal, pais, telefono, fax)
        cursor.execute(add_provedor, data_provedor)
        self.cnx.commit()
        cursor.close()

    def insertarMarca(self,nombre):
        cursor = self.cnx.cursor()
        add_marca= ("Insert into marca"
                    "(Marca)"
                    "values ('"+nombre+"')")
        cursor.execute(add_marca)
        self.cnx.commit()
        cursor.close()


    def insertarUsuario(self, nombre, aP, aM, edad, tipoEmple, passw, fechaCon, direcc,correo):
        cursor = self.cnx.cursor()
        add_usuario = ("Insert into empleado"
                     "(nombre,apellidopaterno,apellidomaterno,edad,tipoempleado,contraseña,fechaContratacion,direccion,correo)"
                     "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_usuario = (nombre,aP,aM, edad,tipoEmple,passw, fechaCon,direcc,correo)
        cursor.execute(add_usuario, data_usuario)
        self.cnx.commit()
        cursor.close()

    def insertarIva(self,iva):
        r = self.datos("select * from iva");
        if r.fetchall() == []:
            cursor = self.cnx.cursor()
            add_marca = ("Insert into iva"
                     "(iva)"
                     "values ('" +str(iva) + "')")
            cursor.execute(add_marca)
            self.cnx.commit()
            cursor.close()
        else:
            cursor = self.cnx.cursor()
            add_marca = ("update iva set iva ="+str(iva)+" where idiva = 1")
            cursor.execute(add_marca)
            self.cnx.commit()
            cursor.close()


    def usuarioValidacion(self,correo,password):
        query = ("select * from empleado"
                 " where correo = %s and contraseña = %s ")
        data = (correo, password)
        resultado = self.retornaDatos(query,data)
        if resultado == []:
            return [False,[]]
        else:
            return [True, resultado]

    def retornaDatos(self,query,data):
        cursor = self.cnx.cursor()
        cursor.execute(query,data)
        datos = cursor
        return datos.fetchall()

    def datos(self, query):
        cursor = self.cnx.cursor()
        cursor.execute(query)
        return cursor

    def imprimirDatos(self,query):
        cursor = self.cnx.cursor()
        cursor.execute(query)
        for i in cursor:
            print(i)

    def cerrarConexion(self):
        self.cnx.close()

#usuario
#con = ConexionBd()
#con.insertarUsuario("Jonathan", "Lara", "Hurtado", 18, "Gerente", "12345", date(1997,7,31), "Av.Francisco Villa Mz.933 Lt.8","jonabimael@hotmail.com")
#con.datos("select * from empleado")
#print(con.usuarioValidacion("jonabimael@hotmail.com", "1234"))
#con.cerrarConexion()

#marca
#con = ConexionBd()
#con.insertarMarca("Yakult")
#con.datos("select * from marca")
#con.cerrarConexion()


#provedor
#con = ConexionBd()
#con.insertarProvedor("laracorp","Jonathan Lara","av.siempre viva","valle","edomex",56615,"Mexico",59786363,"56565666")
#con.imprimirDatos("select * from proveedor")
#con.cerrarConexion()

#producto
#con = ConexionBd()
#con.insertarProducto(1,1,"Yakult","3312323",32,"Yakul con shirota",100)
#con.imprimirDatos("select * from producto")
#con.cerrarConexion()

#iva
#con = ConexionBd()
#con.insertarIva(3)
#r = con.datos("select * from iva").fetchall()[0][1]
#print(r)
#con.insertarIva(6)
#r = con.datos("select * from iva").fetchall()[0][1]
#print(r)