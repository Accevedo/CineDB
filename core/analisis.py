from config import my_globals
import pandas as pd



#Limpieza y analisis de datos, esto lo hacemos para asegurar que los datos esten limpios y tipados 
def cargar_datos():
# Lee el archivo CSV y convierte la columna 'fecha' a tipo datetime
    df_peliculas = pd.read_csv(my_globals.file, parse_dates=['fecha_de_emision'])
    print(df_peliculas)
    print(df_peliculas.shape)
    print(df_peliculas.dtypes)