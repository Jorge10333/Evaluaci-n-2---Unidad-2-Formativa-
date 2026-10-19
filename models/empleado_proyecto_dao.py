# --- DAO de la tabla intermedia (Relación N:M) ---
from sqlite3 import Cursor
from config.database import Database

class EmpleadoProyectoDAO:
    @staticmethod
    def asignar(asignacion: EmpleadoProyecto) -> bool:
        # Crea la vinculación entre un empleado y un proyecto
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
        # Elimina la asignación específica entre un empleado y un proyecto
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