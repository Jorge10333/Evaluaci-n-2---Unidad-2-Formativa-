from models.registro_tiempo import RegistroDeTiempo
from models.usuario import Usuario

class Empleado(Usuario):
    def __init__(self, id_usuario, nombre_usuario, contraseña, rol,
                 nombre, direccion, telefono, email, fecha_inicio, salario, id_unico):
        super().__init__(id_usuario, nombre_usuario, contraseña, rol)
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__fecha_inicio = fecha_inicio
        self.__salario = salario
        self.__id_unico = id_unico
        self.__registros = []

    def guardar_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre

    def guardar_direccion(self, direccion):
        self.__direccion = direccion

    def obtener_direccion(self):
        return self.__direccion

    def guardar_telefono(self, telefono):
        self.__telefono = telefono

    def obtener_telefono(self):
        return self.__telefono

    def guardar_email(self, email):
        self.__email = email

    def obtener_email(self):
        return self.__email

    def guardar_fechaInicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def obtener_fechaInicio(self):
        return self.__fecha_inicio

    def guardar_salario(self, salario):
        self.__salario = salario

    def obtener_salario(self):
        return self.__salario

    def guardar_idUnico(self, id_unico):
        self.__id_unico = id_unico

    def obtener_idUnico(self):
        return self.__id_unico

    def registrarHoras(self, fecha, horas, descripcion, proyecto=None):
        registro = RegistroDeTiempo(fecha, horas, descripcion, proyecto)
        self.__registros.append(registro)
        return f"{horas} horas registradas para {self.__nombre}"
    
    def imprimir_Empleado(self):
        print(f"Empleado: {self.__nombre} | Email: {self.__email}")