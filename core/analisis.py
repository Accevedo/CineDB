from config import my_globals
import pandas as pd

# TODO: Implementar validación por campo con columnas tipo 'valido_para_analisis' en todas las funciones


# Limpieza y análisis de datos, esto lo hacemos para asegurar que los datos estén limpios y tipados 
def cargar_datos():
    # Lee el archivo CSV y convierte la columna 'fecha_emision' a tipo datetime
    df_peliculas = pd.read_csv(my_globals.file, parse_dates=['fecha_emision'])
    # print(df_peliculas.info())  # Información del DataFrame (comentado)
    return df_peliculas.set_index(['id'])  # Establece 'id' como índice y retorna el DataFrame

def top5_movies():
    # Obtiene los datos limpios
    df = cargar_datos()
    # Convierte la columna 'popularidad' a tipo numérico, valores no convertibles serán NaN
    df['popularidad'] = pd.to_numeric(df['popularidad'], errors='coerce')
    # Selecciona las 5 películas con mayor popularidad
    top5 = df.nlargest(5, 'popularidad')[['title', 'fecha_emision', 'popularidad']]
    print(top5)  # Muestra el resultado
    return top5  # Retorna el DataFrame con el top 5

def count_by_genre():
    df = cargar_datos()
    df['generos'] = df['generos'].str.split('|')
    df_expandido = df.explode('generos')

    conteo_por_titulo = (
        df_expandido
        .groupby('generos')['title']
        .count()
        .sort_values(ascending=False)
        .reset_index()
    )

    conteo_por_titulo.columns = ['generos', 'cantidad']

    print(conteo_por_titulo)  # Para depurar
    return conteo_por_titulo


def promedio_votaciones_por_pais():
    # Obtiene los datos limpios
    df = cargar_datos()
    # Separa los géneros en listas usando el separador '|'
    df['paises'] = df['paises'].str.split('|')
    # Expande el DataFrame para que cada género tenga su propia fila
    df_expandido = df.explode('paises')
    # Calcula el promedio de votaciones por género
    promedio_por_pais =(
        df_expandido
        .groupby('paises')['votaciones']
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    promedio_por_pais.columns = ['paises', 'promedio_votaciones']
   
    df_pais_por_titulo = df_expandido.groupby('paises')['title'].apply(lambda x: ", ".join(x.head(3))).reset_index()

    print(df_pais_por_titulo)

    promedio_por_pais = promedio_por_pais.merge(df_pais_por_titulo, on="paises", how="left")

    promedio_por_pais = promedio_por_pais.rename(columns={"title": "peliculas_destacadas"})

    #print(promedio_por_pais)  # Muestra el promedio por género
    #print(promedio_por_pais)
    return promedio_por_pais  # Retorna el promedio por género

def count_by_genre_runtime():
    # Obtiene los datos limpios
    df = cargar_datos()
    df ['generos'] = df['generos'].str.split('|')
    df_explode = df.explode('generos')
    timpo_por_genero = df_explode.groupby('generos')['duracion_min'].mean().sort_values(ascending=False)
    print(timpo_por_genero)

def count_by_country():
    # Obtiene los datos limpios
    df = cargar_datos()
    # Separa los países en listas usando el separador '|'
    df['paises'] = df['paises'].str.split('|')
    # Expande el DataFrame para que cada país tenga su propia fila
    df_expandido = df.explode('paises')
    # Cuenta cuántas películas hay por cada país
    conteo_por_paises = df_expandido.groupby('paises')['title'].count().sort_values(ascending=False)
    print(conteo_por_paises)  # Muestra el conteo por país
    return conteo_por_paises  # Retorna el conteo por país

def promedio_votaciones_por_genero():
    # Obtiene los datos limpios
    df = cargar_datos()
    # Separa los géneros en listas usando el separador '|'
    df['generos'] = df['generos'].str.split('|')
    # Expande el DataFrame para que cada género tenga su propia fila
    df_expandido = df.explode('generos')
    # Calcula el promedio de votaciones por género
    promedio_por_genero = df_expandido.groupby('generos')['votaciones'].mean().sort_values(ascending=False)
    print(promedio_por_genero)  # Muestra el promedio por género
    return promedio_por_genero  # Retorna el promedio por género



def duracion_promedio():
    df = cargar_datos()
    updated_df = df[df['duracion_min'] > 0]
    print(updated_df['duracion_min'].mean())
    return updated_df['duracion_min'].mean()


def recaudado_por_titulo():
    df = cargar_datos()
    df_filtrado = df[df['recaudo_usd'] > 0]
    top5 = df.nlargest(5, 'recaudo_usd')[['title', 'recaudo_usd']]
    
    print(top5)
    return df_filtrado


def Cantidad_total_de_películas_guardadas():
    df = cargar_datos()
    #print(df['title'])
    return df.loc[:, ['title', 'sinopsis', 'generos', 'duracion_min']]
    # tottal = df['total_peliculas'] = df['title'].count()
    # resultado = pd.DataFrame({
    #     "Total_peliculas": [tottal]
    # })

    # print(resultado)
    # return f"{df} Cantidad de peliculas guardadas {resultado['Total_peliculas']}"
