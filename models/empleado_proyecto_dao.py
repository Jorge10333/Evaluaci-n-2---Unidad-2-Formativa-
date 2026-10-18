from sqlite3 import Cursor
from config.database import Database
from .empleado_proyecto import EmpleadoProyecto

class EmpleadoProyectoDAO:
    """
    DAO para gestionar la asignación y desasignación de Empleados a Proyectos.
    """
    @staticmethod
    def asignar(asignacion: EmpleadoProyecto) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO empleado_proyecto (id_empleado, id_proyecto) VALUES (?, ?)",
                (asignacion.id_empleado, asignacion.id_proyecto)
            )
            conn.commit()
            asignacion.id_empleado_proyecto = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al asignar empleado a proyecto: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def desasignar(id_empleado: int, id_proyecto: int) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM empleado_proyecto WHERE id_empleado = ? AND id_proyecto = ?",
                (id_empleado, id_proyecto)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al desasignar empleado del proyecto: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_proyectos_por_empleado(id_empleado: int) -> list[int]:
        conn = Database().get_connection()
        proyectos_ids = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_proyecto FROM empleado_proyecto WHERE id_empleado = ?", (id_empleado,))
            filas = cursor.fetchall()
            proyectos_ids = [fila['id_proyecto'] for fila in filas]
        except Exception as e:
            print(f"Error al obtener proyectos asignados: {e}")
        finally:
            conn.close()
        return proyectos_ids