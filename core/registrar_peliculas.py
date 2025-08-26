import os 
import csv
from config.my_globals import file
import pandas as pd

# Función para crear o agregar una película a un archivo CSV
def crear_csv(pelicula, id, file=file):
    # Crea el directorio si no existe
    os.makedirs(os.path.dirname(file), exist_ok=True)

    # Verifica si el archivo existe y tiene contenido
    if os.path.exists(file) and os.path.getsize(file) > 0:
        # Abre el archivo en modo lectura
        with open(file, mode='r', newline="", encoding='utf-8') as f:
            leer_archivo = csv.DictReader(f)
            # Verifica si ya existe una película con el mismo id
            verificar_integirad = any([lee for lee in leer_archivo if int(lee['id']) == id])
            if verificar_integirad:
                return "Ya exisite ese dato en nuestra base de datos"
        # Si no existe, continúa para agregar la película

    # Abre el archivo en modo agregar (append)
    with open(file, mode="a", newline="", encoding='utf-8') as f:
        campos = [
                    "id",
                    "fecha_guardado",  
                    "title", 
                    "popularidad", 
                    "votaciones", 
                    "sinopsis", 
                    "generos", 
                    'paises',
                    "fecha_emision",
                    "recaudo_usd",
                    "duracion_min"
                    
                    ]
        Escribiendo_archivo = csv.DictWriter(f, fieldnames=campos)
        # Si el archivo está vacío, escribe el encabezado
        if f.tell() == 0:
            Escribiendo_archivo.writeheader()      

        # Escribe la información de la película en el archivo CSV
        Escribiendo_archivo.writerow(pelicula)     

    df = pd.read_csv(file, parse_dates=["fecha_emision"])
    return df.set_index('id')