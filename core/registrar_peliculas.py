import os 
import csv
from config.my_globals import file

def crear_csv(pelicula, id, file=file):
    os.makedirs(os.path.dirname(file), exist_ok=True)

    if os.path.exists(file) and os.path.getsize(file) > 0:
        with open(file, mode='r', newline="", encoding='utf-8') as f:
            leer_archivo = csv.DictReader(f)
            verificar_integirad = any([lee for lee in leer_archivo if int(lee['id']) == id])
            if verificar_integirad:
                return "Ya exisite ese dato en nuestra base de datos"
        #Agrega la pelicula selccionada en el CSV
    with open(file, mode="a", newline="", encoding='utf-8') as f:
        campos = ["id", "title", "popularidad", "votaciones", "sinopsis", "Generos"]
        Escribiendo_archivo = csv.DictWriter(f, fieldnames=campos)
        if f.tell() == 0:
            Escribiendo_archivo.writeheader()      


        Escribiendo_archivo.writerow(pelicula)     