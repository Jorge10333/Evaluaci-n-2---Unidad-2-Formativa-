class Usuario:
    """
    Modelo (DTO) para la entidad Usuario (Autenticación y Cuentas).
    """
    def __init__(
        self,
        nombre_usuario: str,
        contrasena_hash: str,
        rol: str,
        id_empleado: int | None = None,
        id_usuario: int | None = None
    ):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena_hash = contrasena_hash
        self.rol = rol
        self.id_empleado = id_empleado

    @property
    def nombre_usuario(self) -> str:
        return self._nombre_usuario

    @nombre_usuario.setter
    def nombre_usuario(self, valor: str) -> None:
        # Validación de nombre de usuario mínimo de 3 caracteres
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
        self._nombre_usuario = valor.strip()

    @property
    def rol(self) -> str:
        return self._rol

    @rol.setter
    def rol(self, valor: str) -> None:
        # Valida que el rol no quede en blanco
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El rol no puede estar vacío.")
        self._rol = valor.strip().title()

    def __str__(self) -> str:
        id_str = self.id_usuario if self.id_usuario is not None else 'Sin asignar'
        emp_str = self.id_empleado if self.id_empleado is not None else 'Sin empleado'
        return f"Usuario [ID: {id_str}] | Username: {self.nombre_usuario} | Rol: {self.rol} | Empleado ID: {emp_str}"

    def __repr__(self) -> str:
        return f"Usuario(id_usuario={self.id_usuario}, nombre_usuario='{self.nombre_usuario}', rol='{self.rol}')"