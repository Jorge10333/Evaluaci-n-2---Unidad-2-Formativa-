import os  # Importa el módulo del sistema operativo para leer variables de entorno
from pathlib import Path  # Importa Path para construir rutas de archivos de forma segura y multiplataforma

try:  # Intenta importar y cargar el archivo .env si python-dotenv está instalado
    from dotenv import load_dotenv  # Importa la función que carga variables desde un archivo .env
    # Calcula la ruta absoluta hasta la raíz del proyecto (subiendo dos niveles desde config/settings.py)
    env_path = Path(__file__).resolve().parent.parent / ".env"  # Construye la ruta completa al archivo .env
    load_dotenv(dotenv_path=env_path)  # Carga las variables del archivo .env en el entorno de ejecución
except ImportError:  # Si la librería python-dotenv no está instalada, evita que el programa falle
    pass  # Continúa la ejecución utilizando los valores por defecto definidos abajo


class Settings:  # Define la clase central de configuración de la aplicación
    """
    Centraliza las variables de configuración del sistema EcoTech Solutions.
    """
    # Lee la URL de geocodificación desde el entorno; si no existe, usa la URL pública de Open-Meteo
    GEO_API_URL: str = os.getenv("GEO_API_URL", "https://geocoding-api.open-meteo.com/v1/search")  # URL para buscar coordenadas de ciudades
    # Lee la URL del pronóstico desde el entorno; si no existe, usa la URL de Open-Meteo
    WEATHER_API_URL: str = os.getenv("WEATHER_API_URL", "https://api.open-meteo.com/v1/forecast")  # URL para obtener clima actual
    # Lee el tiempo máximo de espera en segundos y lo convierte a número entero
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "5"))  # Límite de espera HTTP para evitar bloqueos
    # Lee si el modo de respaldo sin internet está activado y lo convierte a booleano (True/False)
    ENABLE_OFFLINE_FALLBACK: bool = os.getenv("ENABLE_OFFLINE_FALLBACK", "True").lower() in ("true", "1", "yes")  # Activa contingencia offline

    # Lee los parámetros iniciales de autenticación para crear el primer administrador sin escribir claves en duro
    ADMIN_INITIAL_USER: str = os.getenv("ADMIN_INITIAL_USER", "admin")  # Nombre de usuario administrador por defecto
    ADMIN_INITIAL_CLAVE: str = os.getenv("ADMIN_INITIAL_CLAVE", "admin1234")  # Contraseña inicial que será encriptada con SHA-256
    MAX_LOGIN_ATTEMPTS: int = int(os.getenv("MAX_LOGIN_ATTEMPTS", "3"))  # Cantidad máxima de intentos fallidos de login