class EmpleadoProyecto:
    """
    Modelo DTO para la asignación entre Empleado y Proyecto (Relación N:M).
    """
    def __init__(self, id_empleado: int, id_proyecto: int, id_empleado_proyecto: int | None = None):
        self.id_empleado_proyecto = id_empleado_proyecto
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto

    def __str__(self) -> str:
        return f"Asignacion [ID: {self.id_empleado_proyecto}] | Empleado ID: {self.id_empleado} -> Proyecto ID: {self.id_proyecto}"