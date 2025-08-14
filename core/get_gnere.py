import requests
from config import my_globals
import json

def genre_map() -> dict[int, str]:
    # If the genre map is already cached and is a non-empty dict, return it
    if isinstance(my_globals.my_genre_map, dict) and my_globals.my_genre_map:
        return my_globals.my_genre_map
    
    try:
        # Define the API endpoint and parameters
        url = "https://api.themoviedb.org/3/genre/movie/list"
        params  = {
            "api_key" : my_globals.api_key,
            "Language" : my_globals.language
        }
        # Make a GET request to the API
        respuesta = requests.get(url, params=params, timeout=5)
        respuesta.raise_for_status()  # Raise an exception for HTTP errors
        data = respuesta.json()  # Parse the JSON response
        # Build a dictionary mapping genre IDs to genre names
        genre_map = {int(genre["id"]): genre['name'] for genre in data.get("genres", [])}
        print(genre_map)
        # Cache the genre map in my_globals
        my_globals.my_genre_map = genre_map
        return genre_map
    except requests.exceptions.RequestException:
        # On request error, return the cached genre map or an empty dict
        return my_globals.my_genre_map or {}

        # print(json.dumps(formato_jason, indent=4))  # Example for pretty-printing JSON