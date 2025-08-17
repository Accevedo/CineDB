import requests
from config import my_globals
from core.get_gnere import genre_map
from helper import limpieza
import math
import json


# Obtiene información de una película por su ID desde la API de TMDB
def pelis_info_by_id(id):
    pass
    try:
        # Construye la URL y los parámetros para la petición
        url = f"https://api.themoviedb.org/3/movie/{id}"
        params = {
            "id": id,
            "api_key": my_globals.api_key,
            "Language": my_globals.language
        }

        # Realiza la petición GET con tiempo de espera de 5 segundos
        respuesta = requests.get(url, params=params, timeout=5)
        respuesta.raise_for_status()  # Lanza excepción si el código HTTP es error
        formato_json = respuesta.json()  # Convierte la respuesta a JSON

        # Obtiene la sinopsis y la trunca si es muy larga
        sinopsis_original  = formato_json.get("overview", "Sin sinopsis disponible")
        sinopsis_truncada = (sinopsis_original[:60] + '...' if len(sinopsis_original) > 100 else sinopsis_original)

        # Extrae los nombres de los géneros
        nombres_genre_id = [genre.get('name') for genre in formato_json.get('genres')]
        country_name = [country.get("name") for country in formato_json.get('production_countries')]


        #Aplicando pipeline desde la fuentes de datos 
        recaudo = limpieza.limpiar_formatear_datos_numericos(formato_json.get('revenue'))
        duracion = limpieza.limpiar_formatear_datos_numericos(formato_json.get('runtime'))
        votaciones = limpieza.limpiar_formatear_datos_numericos(formato_json.get('vote_average'))
        popularidad = limpieza.limpiar_formatear_datos_numericos(formato_json.get('popularity'))
        title = formato_json.get('title', "")
        sinopsis = sinopsis_truncada if sinopsis_truncada else ""
        generos = '|'.join(nombres_genre_id) if nombres_genre_id else ""
        paises = "|".join(country_name) if country_name else ""


        


        # Construye el diccionario con los datos relevantes de la película
        datos_pelis = {
                "id": int(formato_json.get('id')),
                "title": title,
                "popularidad": popularidad,
                "votaciones": votaciones,
                "sinopsis": sinopsis,
                "generos":  generos,
                "paises": paises,
                "fecha_emision" : formato_json.get("release_date"),
                "recaudo_usd": recaudo,
                "duracion_min": int(duracion)
            }

        # Devuelve los datos en un diccionario indicando éxito
        return {"ok" : True, "data": datos_pelis}
    except requests.exceptions.Timeout:
        # Maneja error de tiempo de espera
        return {"ok": False, "error": "Tiempo de espera agotado. Intente nuevamente."}
    except requests.exceptions.HTTPError as e:
        # Maneja error HTTP
        return {"ok": False, "error": f"Error en la API: {e}"}
    except requests.exceptions.RequestException:
        # Maneja otros errores de conexión
        return {"ok": False, "error": "No se pudo conectar a la base de datos de películas."}

# Busca películas por nombre y devuelve información de los primeros 5 resultados
def pelis_info_by_name(titulo_peli):
    try:
        # Construye la URL y los parámetros para la búsqueda
        url = my_globals.end_point
        params = {
            "query": titulo_peli,
            "api_key": my_globals.api_key,
            "language" : my_globals.language,
        }

        # Realiza la petición GET con tiempo de espera de 5 segundos
        respuesta = requests.get(url, params=params, timeout=5)
        respuesta.raise_for_status()  # Lanza excepción si el código HTTP es error

        extraer_en_formato_json = respuesta.json()  # Convierte la respuesta a JSON
        lista_pelis = []

        # Obtiene el mapa de géneros (cacheado)
        genre_map_cache =  genre_map()

        # Itera sobre los primeros 5 resultados de la búsqueda
        for datos_peli in extraer_en_formato_json.get('results', [])[:5]:

            # Convierte los IDs de géneros a nombres, usando "Desconocido" si no está en el mapa
            ids = datos_peli.get("genre_ids") or []
            nombres = [genre_map_cache.get(int(gid), f"Desconocido{gid}") for gid in ids]

            # Formatea los géneros como texto separado por '|'
            generos_txt = "|".join(nombres) if nombres else ""

            # Obtiene la sinopsis y la trunca si es muy larga
            sinopsis_original = datos_peli.get('overview', 'Sin sinopsis disponible.')
            sinopsis_truncada = (
                sinopsis_original[:60] + '...' if len(sinopsis_original) > 100 else sinopsis_original
            )

            # Construye el diccionario con los datos relevantes de la película
            datos_pelis = {
                "id": datos_peli['id'],
                "title": datos_peli['title'],
                "popularidad": datos_peli['popularity'],
                "votaciones": datos_peli['vote_average'],
                "sinopsis": sinopsis_truncada,
                "Generos": generos_txt
            }
            lista_pelis.append(datos_pelis)

        # Devuelve solo los 5 primeros resultados en un diccionario indicando éxito
        return {"ok" : True, "data": lista_pelis}

    except requests.exceptions.Timeout:
        # Maneja error de tiempo de espera
        return {"ok": False, "error": "Tiempo de espera agotado. Intente nuevamente."}
    except requests.exceptions.HTTPError as e:
        # Maneja error HTTP
        return {"ok": False, "error": f"Error en la API: {e}"}
    except requests.exceptions.RequestException:
        # Maneja otros errores de conexión
        return {"ok": False, "error": "No se pudo conectar a la base de datos de películas."}
