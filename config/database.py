import sqlite3
from sqlite3 import Connection, Cursor

class Database:
    """
    Clase Singleton que administra la conexión y creación de la BD SQLite.
    """
    _instance = None
    _db_path = "ecotech_solutions.db"

    def __new__(cls):
        # Garantiza que exista solo una instancia de la base de datos
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_connection(self) -> Connection:
        # Crea la conexión y habilita claves foráneas e iteración por nombre de columna
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def init_db(self) -> None:
        # Crea las tablas iniciales si no existen dentro de la BD
        conn = self.get_connection()
        try:
            cursor: Cursor = conn.cursor()

            # Tabla Departamento: almacena la estructura organizacional
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamento (
                    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    id_gerente INTEGER,
                    FOREIGN KEY(id_gerente) REFERENCES empleado(idUnico) ON DELETE SET NULL
                )
            """)

            # Tabla Empleado: datos personales y laborales
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleado (
                    idUnico INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    direccion TEXT,
                    telefono TEXT,
                    email TEXT NOT NULL,
                    fechaInicio TEXT NOT NULL,
                    salario REAL,
                    id_departamento INTEGER,
                    FOREIGN KEY(id_departamento) REFERENCES departamento(id_departamento) ON DELETE SET NULL
                )
            """)

            # Tabla Administrador: relación 1:1 especial para administradores
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS administrador (
                    id_empleado INTEGER PRIMARY KEY,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(idUnico) ON DELETE CASCADE
                )
            """)

            # Tabla Usuario: cuentas de acceso y autenticación
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombreUsuario TEXT NOT NULL,
                    contraseñaHash TEXT NOT NULL,
                    rol TEXT NOT NULL,
                    id_empleado INTEGER,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(idUnico) ON DELETE CASCADE
                )
            """)

            # Tabla Proyecto: proyectos asignables
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyecto (
                    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    fechaInicio TEXT NOT NULL
                )
            """)

            # Tabla Intermedia Empleado_Proyecto: relación N:M entre empleados y proyectos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleado_proyecto (
                    id_empleado_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_empleado INTEGER NOT NULL,
                    id_proyecto INTEGER NOT NULL,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(idUnico) ON DELETE CASCADE,
                    FOREIGN KEY(id_proyecto) REFERENCES proyecto(id_proyecto) ON DELETE CASCADE
                )
            """)

            # Tabla Registro_Tiempo: horas trabajadas vinculadas a un empleado y proyecto
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS registro_tiempo (
                    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT NOT NULL,
                    cantidadHoraTrabajada REAL NOT NULL,
                    descripcionTareaRealizada TEXT NOT NULL,
                    id_empleado INTEGER NOT NULL,
                    id_proyecto INTEGER NOT NULL,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(idUnico) ON DELETE CASCADE,
                    FOREIGN KEY(id_proyecto) REFERENCES proyecto(id_proyecto) ON DELETE CASCADE
                )
            """)

            conn.commit()  # Guarda las tablas creadas
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")
        finally:
            conn.close()  # Libera la conexión
