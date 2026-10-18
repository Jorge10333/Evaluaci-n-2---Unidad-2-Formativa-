from config.database import Conexion

bd = Conexion()
bd.conectar()
bd.cerrar()