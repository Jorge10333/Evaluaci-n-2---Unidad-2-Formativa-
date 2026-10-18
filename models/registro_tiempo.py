class RegistroTiempo:
    """
    Modelo DTO para la entidad Registro de Tiempo.
    """
    def __init__(
        self,
        fecha: str,
        cantidad_hora_trabajada: float,
        descripcion_tarea_realizada: str,
        id_empleado: int,
        id_proyecto: int,
        id_registro: int | None = None
    ):
        self.id_registro = id_registro
        self.fecha = fecha
        self.cantidad_hora_trabajada = cantidad_hora_trabajada
        self.descripcion_tarea_realizada = descripcion_tarea_realizada
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto

    @property
    def cantidad_hora_trabajada(self) -> float:
        return self._cantidad_hora_trabajada

    @cantidad_hora_trabajada.setter
    def cantidad_hora_trabajada(self, valor: float | int) -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("La cantidad de horas trabajadas debe ser mayor a 0.")
        self._cantidad_hora_trabajada = float(valor)

    def __str__(self) -> str:
        id_str = self.id_registro if self.id_registro is not None else 'Sin asignar'
        return f"Registro [ID: {id_str}] | Fecha: {self.fecha} | Horas: {self.cantidad_hora_trabajada} hrs | Empleado ID: {self.id_empleado}"