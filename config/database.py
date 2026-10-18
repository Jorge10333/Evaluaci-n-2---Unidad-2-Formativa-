import sqlite3

class Conexion:
    def __init__(self, nombre_bd="Ecotech.db"):
        self.__nombre_bd = nombre_bd
        self.__conexion = None

    def conectar(self):
        try:
            self.__conexion = sqlite3.connect(self.__nombre_bd)
            print("Conexión exitosa a la base de datos")
            return self.__conexion
        except sqlite3.Error as error:
            print(f"Error de conexión: {error}")
            return None

    def cerrar(self):
        if self.__conexion:
            self.__conexion.close()
            print("Conexión cerrada") 