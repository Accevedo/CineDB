from datetime import datetime
import math
import os
import csv
from config.my_globals import file_logs


def generar_batch_id() -> str:
    fecha_actual =  datetime.now().strftime("%Y%m%d_%H%M%S")
    return fecha_actual

def procesar_detalle_pelicula(data):
    if data == "":
        return 1
    if isinstance(data, float) and math.isnan(data):
        return 1  # faltante
    return 0  # todo bien
    

def crear_lista_logs(log, accion, id=id):

    print(log)
    
    logs = {
        "batch_id" : generar_batch_id(),
        "accion" : "agrgear" if accion == "agregar" else "Remplazar",
        "id" : id,
        "titulo": log.get("title"),
        "faltante_recaudo" : procesar_detalle_pelicula(log['recaudo_usd']),
        "faltante_generos" : procesar_detalle_pelicula(log['generos']),
        "faltante_paises"  : procesar_detalle_pelicula(log['paises']),
        "faltante_sinopsis": procesar_detalle_pelicula(log['sinopsis'])
        
    }

    return registrar_logs(logs)
    
def registrar_logs(pelicula):
    os.makedirs(os.path.dirname(file_logs), exist_ok=True)

    with open(file_logs, mode='a', newline="", encoding="utf-8") as f:
        campos_logs = [
    "batch_id",
    "accion",
    "id",
    "titulo",
    "faltante_recaudo",
    "faltante_generos",
    "faltante_paises",
    "faltante_sinopsis"
    ]
        
        
        escribiendo =  csv.DictWriter(f, fieldnames=campos_logs)
        
        if f.tell() == 0:
            escribiendo.writeheader()
        
        escribiendo.writerow(pelicula)


