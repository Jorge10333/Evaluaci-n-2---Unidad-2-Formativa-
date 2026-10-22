from views.main_view import MainView
from controllers.departamento_controller import DepartamentoController
from controllers.empleado_controller import EmpleadoController
from controllers.proyecto_controller import ProyectoController
from controllers.registro_tiempo_controller import RegistroTiempoController

class MainController:
    """
    Controlador principal que coordina los subcontroladores del sistema.
    """
    def __init__(self):
        # Instancia la vista del menú principal y los demás controladores
        self.view = MainView()
        self.departamento_controller = DepartamentoController()
        self.empleado_controller = EmpleadoController()
        self.proyecto_controller = ProyectoController()
        self.registro_tiempo_controller = RegistroTiempoController()

    def ejecutar(self) -> None:
        # Ciclo que gestiona el menú global de opciones
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.departamento_controller.ejecutar()
            elif opcion == 2:
                self.empleado_controller.ejecutar()
            elif opcion == 3:
                self.proyecto_controller.ejecutar()
            elif opcion == 4:
                self.registro_tiempo_controller.ejecutar()
            elif opcion == 0:
                self.view.mostrar_mensaje("Gracias por usar el sistema EcoTech Solutions. ¡Hasta luego!")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida. Por favor, intente nuevamente.")