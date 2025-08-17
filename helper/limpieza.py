from core import api_handler
import math

def limpiar_formatear_datos_numericos(datos):
    
    
    if datos in (None, "", "N/A"):
        return math.nan
    else:
        try:
            return float(str(datos).replace(",", "").replace("$", ""))
        except ValueError:
            return math.nan