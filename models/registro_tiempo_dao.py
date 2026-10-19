from sqlite3 import Cursor
from config.database import Database

class RegistroTiempoDAO:
    @staticmethod
    def crear(registro: RegistroTiempo) -> bool:
        # Inserta un nuevo reporte de horas
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO registro_tiempo (fecha, cantidadHoraTrabajada, descripcionTareaRealizada, id_empleado, id_proyecto)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    registro.fecha,
                    registro.cantidad_hora_trabajada,
                    registro.descripcion_tarea_realizada,
                    registro.id_empleado,
                    registro.id_proyecto
                )
            )
            conn.commit()
            registro.id_registro = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al registrar tiempo: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_por_empleado(id_empleado: int) -> list[RegistroTiempo]:
        # Filtra todas las horas trabajadas ingresadas por un empleado
        conn = Database().get_connection()
        registros = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT * FROM registro_tiempo WHERE id_empleado = ?", (id_empleado,))
            filas = cursor.fetchall()
            for fila in filas:
                registros.append(
                    RegistroTiempo(
                        fecha=fila['fecha'],
                        cantidad_hora_trabajada=fila['cantidadHoraTrabajada'],
                        descripcion_tarea_realizada=fila['descripcionTareaRealizada'],
                        id_empleado=fila['id_empleado'],
                        id_proyecto=fila['id_proyecto'],
                        id_registro=fila['id_registro']
                    )
                )
        except Exception as e:
            print(f"Error al obtener registros de tiempo por empleado: {e}")
        finally:
            conn.close()
        return registros

    @staticmethod
    def eliminar(id_registro: int) -> bool:
        # Borra una entrada específica de horas
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM registro_tiempo WHERE id_registro = ?", (id_registro,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar registro de tiempo: {e}")
            return False
        finally:
            conn.close()