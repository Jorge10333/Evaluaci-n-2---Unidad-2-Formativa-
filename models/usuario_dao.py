from sqlite3 import Cursor
from config.database import Database
from .usuario import Usuario

class UsuarioDAO:
    """
    Data Access Object para la entidad Usuario.
    Maneja las operaciones de persistencia en la base de datos.
    """
    @staticmethod
    def crear(usuario: Usuario) -> bool:
        # Registra un nuevo usuario asociándolo a un empleado
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuario (nombreUsuario, contraseñaHash, rol, id_empleado) VALUES (?, ?, ?, ?)",
                (usuario.nombre_usuario, usuario.contrasena_hash, usuario.rol, usuario.id_empleado)
            )
            conn.commit()
            usuario.id_usuario = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear usuario en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_por_username(nombre_usuario: str) -> Usuario | None:
        # Busca una cuenta de usuario por su nombre de usuario
        conn = Database().get_connection()
        usuario = None
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE nombreUsuario = ?", (nombre_usuario.strip(),))
            fila = cursor.fetchone()
            if fila:
                usuario = Usuario(
                    nombre_usuario=fila['nombreUsuario'],
                    contrasena_hash=fila['contraseñaHash'],
                    rol=fila['rol'],
                    id_empleado=fila['id_empleado'],
                    id_usuario=fila['idUsuario']
                )
        except Exception as e:
            print(f"Error al buscar usuario: {e}")
        finally:
            conn.close()
        return usuario

    @staticmethod
    def obtener_todos() -> list[Usuario]:
        # Lista todas las cuentas del sistema
        conn = Database().get_connection()
        usuarios = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario")
            filas = cursor.fetchall()
            for fila in filas:
                usuarios.append(
                    Usuario(
                        nombre_usuario=fila['nombreUsuario'],
                        contrasena_hash=fila['contraseñaHash'],
                        rol=fila['rol'],
                        id_empleado=fila['id_empleado'],
                        id_usuario=fila['idUsuario']
                    )
                )
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
        finally:
            conn.close()
        return usuarios

    @staticmethod
    def actualizar(usuario: Usuario) -> bool:
        # Actualiza las credenciales o el rol del usuario
        if usuario.id_usuario is None:
            return False
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE usuario 
                SET nombreUsuario = ?, contraseñaHash = ?, rol = ?, id_empleado = ? 
                WHERE idUsuario = ?
                """,
                (usuario.nombre_usuario, usuario.contrasena_hash, usuario.rol, usuario.id_empleado, usuario.id_usuario)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_usuario: int) -> bool:
        # Elimina una cuenta de usuario por su ID
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("DELETE FROM usuario WHERE idUsuario = ?", (id_usuario,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False
        finally:
            conn.close()