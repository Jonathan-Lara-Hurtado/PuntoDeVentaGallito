import mysql.connector
from datetime import date, datetime, timedelta
import calendar

class ConexionBd:
    def __init__(self,user='gallito',passw='12345',host='127.0.0.1',db='gallitonegro'):
        self.cnx = mysql.connector.connect(
            user=user,
            password =passw,
            host=host,
            database=db,
        )


    def insertarVenta(self,idventa,idempleado,fechaventa,subtotal,iva,total):
        try:
            cursor = self.cnx.cursor()
            add_Venta = ("Insert into venta"
                         "(idventa,idempleado,fechaventa,subtotal,iva,total)"
                         "values (%s ,%s , %s, %s, %s, %s)")
            data_Venta = (idventa, idempleado, fechaventa, subtotal, iva, total)
            cursor.execute(add_Venta, data_Venta)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
            return False
        except mysql.connector.Error as err:
            return True


    def insertardetalleventa(self, idventa, idproducto, precio, cantidad):
        cursor = self.cnx.cursor()
        add_DetalleVenta = ("Insert into detalleventa"
                     "(idventa,idproducto,precio,cantidad)"
                     "values (%s , %s, %s, %s)")
        data_detalleVenta = (idventa, idproducto, precio, cantidad)
        cursor.execute(add_DetalleVenta, data_detalleVenta)
        self.cnx.commit()
        cursor.close()
        self.cnx.close()

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

    def ventasMensuales(self):
        cursor = self.cnx.cursor()
        query = ("select * from venta"
                 " where  year(fechaventa)="+str(date.today().year)+" and month(fechaventa)="+str(date.today().month))
        cursor.execute(query)
        datos = cursor

        self.datos = datos.fetchall()

        mesRango = calendar.monthrange(date.today().year, date.today().month)
        self.tmp = []
        self.contarVentas = 0

        for i in range(1,mesRango[1]+1):
            self.contarVentas = 0
            for e in self.datos:
                if i == e[2].day:
                    self.contarVentas = self.contarVentas + 1
            self.tmp.append(self.contarVentas)

        return [self.tmp,mesRango[1],self.nombreMesEspañol(date.today().month)]

    def nombreMesEspañol(self,m):
        if m == 1:
            return "Enero"
        elif m == 2:
            return "Febrero"
        elif m == 3:
            return "Marzo"
        elif m == 4:
            return "Abril"
        elif m == 5:
            return "Mayo"
        elif m == 6:
            return "Junio"
        elif m == 7:
            return "Julio"
        elif m == 8:
            return "Agosto"
        elif m == 9:
            return "Septiembre"
        elif m == 10:
            return "Octubre"
        elif m == 11:
            return "Noviembre"
        else:
            return "Diciembre"


    def imprimirDatos(self,query):
        cursor = self.cnx.cursor()
        cursor.execute(query)
        for i in cursor:
            print(i)

    def cerrarConexion(self):
        self.cnx.close()

#usuario
#con = ConexionBd()
#con.insertarUsuario("Jonathan", "Lara", "Hurtado", 18, "Gerente", "12345", date(1997,7,31), "Av.Francisco Villa Mz.933 Lt.8","root")
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


#detalle
#con = ConexionBd()
#con.insertardetalleventa(1,2,32,11)
#con.cerrarConexion()

#fecha = date.today()
#print(fecha.month)
#con = ConexionBd()
#con.ventasMensuales()
#con.cerrarConexion()