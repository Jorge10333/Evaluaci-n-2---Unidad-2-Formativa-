class DepartamentoView:
    """
    Interface de consola para la gestión de Departamentos.
    """
    @staticmethod
    def menu_departamentos() -> str:
        print("\n" + "="*40)
        print("     GESTIÓN DE DEPARTAMENTOS")
        print("="*40)
        print("1. Crear Departamento")
        print("2. Listar Departamentos")
        print("3. Buscar Departamento por ID")
        print("4. Actualizar Departamento")
        print("5. Eliminar Departamento")
        print("0. Volver al Menú Principal")
        return input("Seleccione una opción: ").strip()

    @staticmethod
    def pedir_datos_creacion() -> tuple[str, int | None]:
        print("\n--- Registrar Departamento ---")
        nombre = input("Nombre del Departamento: ").strip()
        gerente_input = input("ID del Gerente Asignado (presione Enter si no tiene): ").strip()
        id_gerente = int(gerente_input) if gerente_input.isdigit() else None
        return nombre, id_gerente

    @staticmethod
    def pedir_id() -> int | None:
        try:
            return int(input("Ingrese el ID del Departamento: ").strip())
        except ValueError:
            print("❌ El ID debe ser un número entero válido.")
            return None

    @staticmethod
    def mostrar_departamento(dep) -> None:
        if dep:
            print(f"👉 {dep}")
        else:
            print("⚠️ Departamento no encontrado.")

    @staticmethod
    def mostrar_lista(departamentos: list) -> None:
        print("\n--- Lista de Departamentos ---")
        if not departamentos:
            print("No hay departamentos registrados.")
        else:
            for dep in departamentos:
                print(f" • {dep}")

    @staticmethod
    def mostrar_mensaje(exito: bool, accion: str) -> None:
        if exito:
            print(f"✅ Departamento {accion} con éxito.")
        else:
            print(f"❌ Error al {accion} el departamento.")