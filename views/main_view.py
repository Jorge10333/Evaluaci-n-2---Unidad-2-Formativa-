from views.utils import leer_numero

class MainView:
    """
    Vista del menú principal del sistema.
    """
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "="*40)
        print(" ECOTECH SOLUTIONS - MENÚ PRINCIPAL")
        print("="*40)
        print("1.- Gestión de Departamentos")
        print("2.- Gestión de Empleados")
        print("3.- Gestión de Proyectos")
        print("4.- Registro de Tiempo / Horas")
        print("0.- Salir")
        print("="*40)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"\n[SISTEMA] {mensaje}")