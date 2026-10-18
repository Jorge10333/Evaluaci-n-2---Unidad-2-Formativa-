import sqlite3
from sqlite3 import Connection, Cursor

class Database:
    """
    Clase que gestiona la conexión a la base de datos implementando 
    el patrón Singleton para evitar múltiples instancias innecesarias.
    """
    _instance = None
    _db_path = "ecotech.db"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_connection(self) -> Connection:
        """
        Retorna una conexión a la base de datos SQLite.
        """
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def init_db(self) -> None:
        """
        Inicializa la base de datos creando las tablas necesarias si no existen.
        """
        conn = self.get_connection()
        try:
            cursor: Cursor = conn.cursor()          
            # Tabla Departamento
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamento (
                    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    id_gerente INTEGER NOT NULL,
                    FOREING KEY(id_gerente) REFERENCES empleado(idUnico) ON DELETE SET NULL
                )
            """)
            # Tabla Empleado
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleado (
                    idUnico INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    direccion TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    email TEXT NOT NULL,
                    fechaInicio TEXT NOT NULL,
                    salario INTEGER NOT NULL,
                    id_departamento INTEGER NOT NULL,
                    FOREIGN KEY(id_departamento) REFERENCES departamento(id_departamento) ON DELETE SET NULL
                )
            """)
            #Tabla administrador (especializacion de Empleado)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS administrador (
                    id_empleado INTEGER PRIMARY KEY,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(idUnico) ON DELETE CASCADE
                )
            """)
            #Tabla usuario
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombreUsuario TEXT NOT NULL,
                    contraseñaHash TEXT NOT NULL,
                    rol TEXT NOT NULL,
                    id_empleado INTEGER NOT NULL,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(idUnico) ON DELETE CASCADE
                )
            """)
            #Tabla Proyecto
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyecto (
                    id_proyecto INTEGER PRYMARI KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT NOT NULL,
                    fechaInicio TEXT NOT NULL,
                )
            """)
            #Tabla intermedia
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleado_proyecto (
                    id_empleado_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_empleado INTEGER NOT NULL,
                    id_proyecto INTEGER NOT NULL,
                    FOREIGN KEY(id_empleado) REFERENCES empleado(idUnico) ON DELETE CASCADE,
                    FOREIGN KEY(id_proyecto) REFERENCES proyecto(id_proyecto) ON DELETE CASCADE
                )
            """)
            #Tabla Registro-Tiempo
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS registro_tiempo(
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
            print(f"Error al inicializar la base de datos: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    db = Database()
    db.init_db()
    print("Base de datos inicializada correctamente.")
