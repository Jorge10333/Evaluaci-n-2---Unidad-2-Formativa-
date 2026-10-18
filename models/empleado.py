class Empleado:
    """
    Modelo DTO para la entidad Empleado.
    """
    def __init__(
        self,
        nombre: str,
        direccion: str,
        telefono: str,
        email: str,
        fecha_inicio: str,
        salario: float,
        id_departamento: int | None = None,
        id_unico: int | None = None
    ):
        self.id_unico = id_unico
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.id_departamento = id_departamento

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ValueError("El nombre del empleado no es válido.")
        self._nombre = valor.strip().title()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str) -> None:
        if "@" not in valor or "." not in valor:
            raise ValueError("Formato de correo electrónico inválido.")
        self._email = valor.strip().lower()

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, valor: float | int) -> None:
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El salario debe ser un número positivo.")
        self._salario = float(valor)

    def __str__(self) -> str:
        id_str = self.id_unico if self.id_unico is not None else 'Sin asignar'
        return f"Empleado [ID: {id_str}] | Nombre: {self.nombre} | Email: {self.email} | Salario: ${self.salario:,.2f}"

    def __repr__(self) -> str:
        return f"Empleado(id_unico={self.id_unico}, nombre='{self.nombre}', email='{self.email}')"