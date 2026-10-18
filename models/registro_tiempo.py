class RegistroDeTiempo:
    def __init__(self, fecha, cantidad_hora_trabajada, descripcion_tarea, proyecto=None):
        self.__fecha = fecha
        self.__cantidad_hora_trabajada = cantidad_hora_trabajada
        self.__descripcion_tarea = descripcion_tarea
        self.__proyecto = proyecto

    def guardar_fecha(self, fecha):
        self.__fecha = fecha

    def obtener_fecha(self):
        return self.__fecha

    def guardar_cantidadHoraTrabajada(self, cantidad_hora_trabajada):
        self.__cantidad_hora_trabajada = cantidad_hora_trabajada

    def obtener_cantidadHoraTrabajada(self):
        return self.__cantidad_hora_trabajada

    def guardar_descripcionTareaRealizada(self, descripcion_tarea):
        self.__descripcion_tarea = descripcion_tarea

    def obtener_descripcionTareaRealizada(self):
        return self.__descripcion_tarea

    def calcularHoras(self):
        return float(self.__cantidad_hora_trabajada)

    def imprimir_RegistroDeTiempo(self):
        print(f"Fecha: {self.__fecha} | Horas: {self.__cantidad_hora_trabajada} | Tarea: {self.__descripcion_tarea}")