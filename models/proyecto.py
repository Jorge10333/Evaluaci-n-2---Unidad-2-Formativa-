class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio
        self.__empleados = []

    def guardar_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre

    def guardar_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def obtener_descripcion(self):
        return self.__descripcion

    def guardar_fechaInicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def obtener_fechaInicio(self):
        return self.__fecha_inicio

    def asignarEmpleado(self, empleado):
        self.__empleados.append(empleado)
        return f"{empleado.obtener_nombre()} asignado a {self.__nombre}"

    def desasignarEmpleado(self, empleado):
        if empleado in self.__empleados:
            self.__empleados.remove(empleado)
            return f"{empleado.obtener_nombre()} desasignado de {self.__nombre}"
        return "El empleado no está asignado a este proyecto"

    def imprimir_Proyecto(self):
        print(f"Proyecto: {self.__nombre} | Empleados: {len(self.__empleados)}")