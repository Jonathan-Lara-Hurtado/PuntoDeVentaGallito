import sqlite3
class BD:
    def __init__(self, bd="./Recursos/tienda.db", tabla=""):
        self.__conexion = sqlite3.connect(bd)
        self.__tabla = tabla
        self.__estructura = self.obtenerEstructuraTabla(tabla)

    # region gett/sett
    @property
    def conexion(self):
        return self.__conexion

    @conexion.setter
    def conexion(self, value):
        self.__conexion = value

    @property
    def tabla(self):
        return self.__tabla

    @tabla.setter
    def tabla(self, value):
        self.__tabla = value

    @property
    def estructura(self):
        return self.__estructura

    @estructura.setter
    def estructura(self, value):
        self.__estructura = value

    # endregion

    def alta(self, valores, auto_increment=True):
        cursorObj = self.conexion.cursor()
        consulta = f"insert into {self.tabla} values("
        if auto_increment:
            consulta += f"null,"
            for i in range(1, len(valores)):
                consulta += f"{self.convertPyDatoBD(self.estructura[i][2], valores[i])},"
        else:
            for i in range(1, len(valores)):
                consulta += f"{self.convertPyDatoBD(self.estructura[i - 1][2], valores[i])},"
        consulta = consulta[:len(consulta) - 1]
        consulta += ")"
        cursorObj.execute(consulta)
        self.conexion.commit()

    def convertPyDatoBD(self, tipo, valor):
        if tipo == 'TEXT':
            return "'" + valor + "'"
        else:
            return valor

    def obtenerEstructuraTabla(self, tabla):
        cursorObj = self.conexion.cursor()
        cursorObj.execute(f"PRAGMA table_info({self.tabla})")
        return cursorObj.fetchall()

    def eliminar(self, valor):
        cursorObj = self.conexion.cursor()
        consulta = f"delete from {self.tabla} where {self.estructura[0][1]} = {valor}"
        cursorObj.execute(consulta)
        self.conexion.commit()

    def consulta(self):
        cursorObj = self.conexion.cursor()
        consulta = f"select * from {self.tabla}"
        cursorObj.execute(consulta)
        rows = cursorObj.fetchall()
        return rows

    def cerrarConexion(self):
        self.conexion.close()

