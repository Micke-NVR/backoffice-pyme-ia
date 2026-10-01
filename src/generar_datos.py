"""Genera proveedores y facturas FICTICIOS e inserta los datos en PostgreSQL."""

# 1. Imports y carga del .env
import os
import random
from datetime import date, timedelta

import psycopg
from dotenv import load_dotenv

load_dotenv()

# 2. Semilla fija: el azar da siempre los mismos datos (resultados repetibles)
random.seed(42)

# 3. Leer las variables de conexión
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

if not all([DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD]):
    raise SystemExit("Faltan variables en el archivo .env")

# Parámetros de los datos ficticios
CANTIDAD_FACTURAS = 200
PROBABILIDAD_ERROR = 0.10           # ~10% de facturas con el total mal calculado
FECHA_BASE = date(2026, 9, 30)      # fecha fija para que los datos sean repetibles

RAZONES_SOCIALES = [
    "Ferretería Andina SAC",
    "Distribuidora Pacífico SRL",
    "Importaciones Lima EIRL",
    "Servicios Generales Norte SAC",
    "Comercial Los Andes SAC",
    "Textiles del Sur SRL",
    "Tecnología Huacho SAC",
    "Abarrotes El Progreso EIRL",
    "Transportes Rápidos SAC",
    "Papelería Central SRL",
]

with psycopg.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
) as conexion:
    with conexion.cursor() as cursor:

        # 4. Vaciar las tablas y reiniciar la numeración de los id
        cursor.execute("TRUNCATE TABLE facturas, proveedores RESTART IDENTITY;")

        # 5. Insertar proveedores ficticios
        rucs_usados = set()
        for razon_social in RAZONES_SOCIALES:
            # RUC: "20" + 9 dígitos al azar (con ceros a la izquierda), sin repetir
            ruc = "20" + f"{random.randint(0, 999_999_999):09d}"
            while ruc in rucs_usados:
                ruc = "20" + f"{random.randint(0, 999_999_999):09d}"
            rucs_usados.add(ruc)

            cursor.execute(
                "INSERT INTO proveedores (ruc, razon_social) VALUES (%s, %s)",
                (ruc, razon_social),
            )

        # 6. Obtener los id de los proveedores insertados
        cursor.execute("SELECT id FROM proveedores ORDER BY id")
        proveedor_ids = [fila[0] for fila in cursor.fetchall()]

        # 7. Insertar facturas ficticias
        correlativos = {pid: 0 for pid in proveedor_ids}   # contador por proveedor
        facturas_con_error = 0

        for _ in range(CANTIDAD_FACTURAS):
            proveedor_id = random.choice(proveedor_ids)

            # Número: serie propia de cada proveedor + correlativo creciente
            correlativos[proveedor_id] += 1
            numero = f"F{proveedor_id:03d}-{correlativos[proveedor_id]:04d}"

            # Fecha: al azar dentro de los 90 días anteriores a la fecha base
            fecha = FECHA_BASE - timedelta(days=random.randint(0, 90))

            # Montos: IGV = 18% del subtotal; total = subtotal + IGV
            subtotal = round(random.uniform(50, 5000), 2)
            igv = round(subtotal * 0.18, 2)
            total = round(subtotal + igv, 2)

            # A propósito, algunas facturas quedan con el total mal calculado (excepciones)
            if random.random() < PROBABILIDAD_ERROR:
                total = round(total + random.uniform(1, 20), 2)
                facturas_con_error += 1

            cursor.execute(
                "INSERT INTO facturas (proveedor_id, numero, fecha, subtotal, igv, total) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (proveedor_id, numero, fecha, subtotal, igv, total),
            )

        # 8. Mostrar cuántas filas se insertaron
        print(f"Proveedores insertados: {len(proveedor_ids)}")
        print(f"Facturas insertadas: {CANTIDAD_FACTURAS}")
        print(f"Facturas con total mal calculado (a propósito): {facturas_con_error}")