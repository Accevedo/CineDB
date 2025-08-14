import requests
from config import my_globals
import json


def get_query_country() -> dict[str, str]:

    if isinstance(my_globals.my_country_map, dict) and my_globals.my_country_map:
        return my_globals.my_country_map
    
    try:
        url =  f"https://api.themoviedb.org/3/configuration/countries?api_key={my_globals.api_key}"
        respuesta  = requests.get(url, timeout=5)
        respuesta.raise_for_status()
        data  = respuesta.json()
        movie_country = {coun["iso_3166_1"] : coun['english_name'] for coun in data}
        #print(movie_country)
        my_globals.my_country_map = movie_country
        return my_globals.my_country_map
        
        #print(json.dumps(data, indent=4))
    except requests.exceptions.RequestException:
        return my_globals.my_country_map or {}
    
    


