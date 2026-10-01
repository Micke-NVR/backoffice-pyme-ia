"""Prueba que Python puede conectarse a PostgreSQL usando las credenciales del .env."""

# 1. Importar las librerías necesarias
import os                          # para leer variables del entorno
import psycopg                     # para hablar con PostgreSQL
from dotenv import load_dotenv     # para cargar el archivo .env

# 2. Cargar el archivo .env (sus valores quedan disponibles para os.getenv)
load_dotenv()

# 3. Leer las cinco variables de conexión
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Si falta alguna, detenerse con un mensaje claro (no se muestra ningún valor)
if not all([DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD]):
    raise SystemExit("Faltan variables en el archivo .env")

# 4. Conectarse a PostgreSQL (with cierra la conexión sola al terminar)
with psycopg.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
) as conexion:
    with conexion.cursor() as cursor:
        # 5. Ejecutar la consulta
        cursor.execute("SELECT version();")
        resultado = cursor.fetchone()

        # 6. Mostrar solo el texto (resultado es una tupla; [0] es su primer elemento)
        print(resultado[0])