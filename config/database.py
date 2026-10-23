import sqlite3
from sqlite3 import Connection, Cursor

class Database:
    """
    Clase Singleton que administra la conexión y creación de la BD SQLite.
    """
    _instance = None
    _db_path = "ecotech_solutions.db"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_connection(self) -> Connection:
        """
        Retorna una conexión a SQLite habilitando soporte para foreign keys.
        """
        try:
            conn = sqlite3.connect(self._db_path)
            conn.row_factory = sqlite3.Row
            conn.execute("PRAGMA foreign_keys = ON;")
            return conn
        except sqlite3.Error as e:
            print(f"❌ Error al conectar con la base de datos: {e}")
            raise

    def init_db(self) -> None:
        """
        Inicializa la estructura de las tablas en la base de datos.
        Garantiza el cierre seguro de la conexión mediante un bloque finally.
        """
        conn = None
        try:
            conn = self.get_connection()
            cursor: Cursor = conn.cursor()

            # Tabla Departamento
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamento (
                    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    id_gerente INTEGER,
                    FOREIGN KEY(id_gerente) REFERENCES empleado(idUnico) ON DELETE SET NULL
                )
            """)

            # Tabla Empleado
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

            # Tabla Usuario
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

            # Tabla Proyecto
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyecto (
                    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT,
                    fechaInicio TEXT NOT NULL
                )
            """)

            # Tabla Intermedia Empleado_Proyecto (Con restricción UNIQUE)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleado_proyecto (
                    id_empleado_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_empleado INTEGER NOT NULL,
                    id_proyecto INTEGER NOT NULL,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(idUnico) ON DELETE CASCADE,
                    FOREIGN KEY(id_proyecto) REFERENCES proyecto(id_proyecto) ON DELETE CASCADE,
                    UNIQUE(id_empleado, id_proyecto)
                )
            """)

            # Tabla Registro_Tiempo
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

            conn.commit()
        except sqlite3.Error as e:
            print(f"❌ Error al inicializar la base de datos: {e}")
        finally:
            if conn:
                conn.close()