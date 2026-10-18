import hashlib

class Usuario:
    def __init__(self, id_usuario, nombre_usuario, contraseña, rol):
        self.__id_usuario = id_usuario
        self.__nombre_usuario = nombre_usuario
        self.__contraseña_hash = self.__hashear(contraseña)
        self.__rol = rol

    def __hashear(self, contraseña):
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def guardar_nombreUsuario(self, nombre_usuario):
        self.__nombre_usuario = nombre_usuario

    def obtener_nombreUsuario(self):
        return self.__nombre_usuario

    def guardar_contraseña(self, contraseña):
        self.__contraseña_hash = self.__hashear(contraseña)

    def autenticar(self, contraseña):
        return self.__hashear(contraseña) == self.__contraseña_hash

    def guardar_rol(self, rol):
        self.__rol = rol

    def obtener_rol(self):
        return self.__rol

    def verificarPermiso(self, modulo):
        if self.__rol == "admin":
            return True
        return modulo in ["proyectos", "registro_tiempo"]