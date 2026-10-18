class Departamento:
    def __init__(self, nombre, gerente_asociado=None):
        self.__nombre = nombre
        self.__gerente_asociado = gerente_asociado
        self.__empleados = []

    def guardar_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre

    def guardar_gerenteAsociado(self, gerente_asociado):
        self.__gerente_asociado = gerente_asociado

    def obtener_gerenteAsociado(self):
        return self.__gerente_asociado

    def agregarEmpleado(self, empleado):
        self.__empleados.append(empleado)
        return f"{empleado.obtener_nombre()} agregado a {self.__nombre}"

    def imprimir_Departamento(self):
        print(f"Departamento: {self.__nombre} | Empleados: {len(self.__empleados)}")