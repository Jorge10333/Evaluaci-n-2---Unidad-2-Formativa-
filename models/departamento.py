class Departamento:
    """
    Modelo DTO para la entidad Departamento.
    """
    def __init__(self, nombre: str, id_gerente: int | None = None, id_departamento: int | None = None):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.id_gerente = id_gerente

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("El nombre del departamento debe tener al menos 3 caracteres.")
        self._nombre = valor.strip().title()

    @property
    def id_gerente(self) -> int | None:
        return self._id_gerente

    @id_gerente.setter
    def id_gerente(self, valor: int | None) -> None:
        if valor is not None and not isinstance(valor, int):
            raise TypeError("El ID del gerente debe ser un entero.")
        self._id_gerente = valor

    def __str__(self) -> str:
        id_str = self.id_departamento if self.id_departamento is not None else 'Sin asignar'
        gerente_str = self.id_gerente if self.id_gerente is not None else 'Sin gerente'
        return f"Departamento [ID: {id_str}] | Nombre: {self.nombre} | Gerente ID: {gerente_str}"

    def __repr__(self) -> str:
        return f"Departamento(id_departamento={self.id_departamento}, nombre='{self.nombre}', id_gerente={self.id_gerente})"