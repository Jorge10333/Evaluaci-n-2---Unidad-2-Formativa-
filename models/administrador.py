from models.empleado import Empleado

class Administrador(Empleado):
    def __init__(self, id_usuario, nombre_usuario, contraseña, rol,
                 nombre, direccion, telefono, email, fecha_inicio, salario, id_unico):
        super().__init__(id_usuario, nombre_usuario, contraseña, rol,
                         nombre, direccion, telefono, email, fecha_inicio, salario, id_unico)

    def generarInforme(self, tipo):
        return f"Informe de tipo '{tipo}' generado por {self.obtener_nombre()}"

    def exportarInforme(self, formato):
        return f"Informe exportado en formato {formato}"

    def verificarPermiso(self, modulo):
        return True