from sqlite3 import Cursor
from config.database import Database
from .empleado import Empleado

class EmpleadoDAO:
    """
    DAO para operaciones CRUD de la entidad Empleado.
    """
    @staticmethod
    def crear(empleado: Empleado) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO empleado (nombre, direccion, telefono, email, fechaInicio, salario, id_departamento)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    empleado.nombre,
                    empleado.direccion,
                    empleado.telefono,
                    empleado.email,
                    empleado.fecha_inicio,
                    empleado.salario,
                    empleado.id_departamento
                )
            )
            conn.commit()
            empleado.id_unico = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear empleado: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_todos() -> list[Empleado]:
        conn = Database().get_connection()
        empleados = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT * FROM empleado")
            filas = cursor.fetchall()
            for fila in filas:
                empleados.append(
                    Empleado(
                        nombre=fila['nombre'],
                        direccion=fila['direccion'],
                        telefono=fila['telefono'],
                        email=fila['email'],
                        fecha_inicio=fila['fechaInicio'],
                        salario=fila['salario'],
                        id_departamento=fila['id_departamento'],
                        id_unico=fila['idUnico']
                    )
                )
        except Exception as e:
            print(f"Error al obtener empleados: {e}")
        finally:
            conn.close()
        return empleados

    @staticmethod
    def obtener_por_id(id_unico: int) -> Empleado | None:
        conn = Database().get_connection()
        empleado = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT * FROM empleado WHERE idUnico = ?", (id_unico,))
            fila = cursor.fetchone()
            if fila:
                empleado = Empleado(
                    nombre=fila['nombre'],
                    direccion=fila['direccion'],
                    telefono=fila['telefono'],
                    email=fila['email'],
                    fecha_inicio=fila['fechaInicio'],
                    salario=fila['salario'],
                    id_departamento=fila['id_departamento'],
                    id_unico=fila['idUnico']
                )
        except Exception as e:
            print(f"Error al obtener empleado por ID: {e}")
        finally:
            conn.close()
        return empleado

    @staticmethod
    def actualizar(empleado: Empleado) -> bool:
        if empleado.id_unico is None:
            return False
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE empleado
                SET nombre = ?, direccion = ?, telefono = ?, email = ?, fechaInicio = ?, salario = ?, id_departamento = ?
                WHERE idUnico = ?
                """,
                (
                    empleado.nombre,
                    empleado.direccion,
                    empleado.telefono,
                    empleado.email,
                    empleado.fecha_inicio,
                    empleado.salario,
                    empleado.id_departamento,
                    empleado.id_unico
                )
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_unico: int) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM empleado WHERE idUnico = ?", (id_unico,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            return False
        finally:
            conn.close()