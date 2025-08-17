from core.api_handler import pelis_info_by_name, pelis_info_by_id
from core.registrar_peliculas import crear_csv
from tabulate import tabulate
from config import my_globals
import csv
from auditoria.logs_auditoria import crear_lista_logs
# Mostrar información de películas por título
def mostrar_peliculas(titulo_peli):
    resultado  = pelis_info_by_name(titulo_peli)
    if not resultado['ok']:
        print(f"{resultado['error']}")
    print(tabulate(resultado["data"], headers='keys', tablefmt="grid"))
    return resultado["data"]

# Elegir una película por ID de una lista y guardarla en CSV
def elegir_peli(id):
    info_movie  = pelis_info_by_id(id)
    add_movie = info_movie['data']
    crear_lista_logs(add_movie, "agregar", id)
    return crear_csv(add_movie, id)

# Eliminar una película del archivo CSV por ID
def eliminar_pelicula(id):
    print(id)
    # Leer todas las filas excepto la que coincide con el ID a eliminar
    with open(my_globals.file, mode='r', newline="") as f:
        leyendo = csv.DictReader(f)
        contacto_eliminado = [lee_fila for lee_fila in leyendo if int(lee_fila['id']) != id]
        
    # Escribir el archivo CSV sin la película eliminada
    with open(my_globals.file, mode="w", newline="") as f: 
         campos = ["id", "title", "popularidad", "votaciones", "sinopsis"]
         escribir_nueva_lista = csv.DictWriter(f, fieldnames=campos)
         escribir_nueva_lista.writeheader()
         escribir_nueva_lista.writerows(contacto_eliminado)
    
    #return f"Esta fue la pelicula eliminada{contacto_eliminado}"

# Reemplazar una película en el CSV por otra usando sus IDs
def reemplazar_pelicula_csv(old_id, new_id=None):
    # 1) Leer el archivo CSV a memoria
    with open(my_globals.file, mode="r", newline="", encoding="utf-8") as f:
        leyendo = csv.DictReader(f)
        leyendo_persistencia = list(leyendo)

    # Verificar si el old_id existe en el archivo
    existe_old_id = [fila for fila in leyendo_persistencia if fila.get("id") and int(fila["id"]) == old_id]
    if not existe_old_id:
        return "Este ID no se encuentra en nuestro archivo."

    # 2) Solicitar o normalizar el new_id si no se proporciona
    if new_id is None:
        try:
            new_id = int(input("Coloque el nuevo ID: ").strip())
        except (TypeError, ValueError):
            return "El nuevo ID no es válido."
    else:
        new_id = int(new_id)

    # Validar que el nuevo ID no sea igual al anterior y que no exista ya en el archivo
    if new_id == old_id:
        return "El ID colocado ya existe en nuestros archivos; nada que cambiar."

    if any(fila.get("id") and int(fila["id"]) == new_id for fila in leyendo_persistencia):
        return f"El ID {new_id} ya está en nuestros archivos."

    # 3) Obtener la información de la nueva película por ID
    res = pelis_info_by_id(new_id)  # {"ok": True, "data": {...}} / {"ok": False, "error": "..."}
    if not res.get("ok"):
        return f"No se pudo obtener el nuevo ID: {res.get('error', 'Error desconocido.')}"

    pelicula_nueva = res["data"]  # dict con keys: id, title, popularidad, votaciones, sinopsis

    # 4) Construir la lista final en memoria: eliminar old_id y agregar la nueva película
    reemplazo = [fila for fila in leyendo_persistencia if fila.get("id") and int(fila["id"]) != old_id]
    # Asegurar que los campos coincidan
    nueva_fila = {
        "id": int(pelicula_nueva.get("id", new_id)),
        "title": pelicula_nueva.get("title", ""),
        "popularidad": float(pelicula_nueva.get("popularidad", 0)),
        "votaciones": float(pelicula_nueva.get("votaciones", 0)),
        "sinopsis": pelicula_nueva.get("sinopsis", ""),
        "generos": pelicula_nueva.get("Generos", ""),
        "paises" : pelicula_nueva.get("Country", ""),
        "fecha_de_emision": pelicula_nueva.get("Fecha_de_emision", "N/A"),
        "recaudo_usd": float(pelicula_nueva.get("Reacaudo", "")),
        "duracion_min": pelicula_nueva.get( "Duracion", "")

    }
    reemplazo.append({
        "id": nueva_fila["id"],
        "title": nueva_fila["title"],
        "popularidad": nueva_fila["popularidad"],
        "votaciones": nueva_fila["votaciones"],
        "sinopsis": nueva_fila["sinopsis"],
        "generos": nueva_fila["Generos"],
        'paises' : nueva_fila['Country'],
        "fecha_de_emision": nueva_fila["Fecha_de_emision"],
        "reacaudo_usd" : nueva_fila["Reacaudo"],
        "duracion_min" : nueva_fila['Duracion']

    })

    # 5) Escribir el archivo CSV actualizado (header + filas)
    campos = ["id", "title", "popularidad", "votaciones", "sinopsis", "generos", "paises", "fecha_de_emision", 'recaudo_usd', 'duracion_min']
    with open(my_globals.file, mode="w", newline="", encoding="utf-8") as new_file:
        escribiendo_archivo = csv.DictWriter(new_file, fieldnames=campos)
        escribiendo_archivo.writeheader()
        escribiendo_archivo.writerows(reemplazo)

    return f"Reemplazado {old_id} → {new_id}"
