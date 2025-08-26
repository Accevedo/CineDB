import streamlit as st 
from PIL import Image
from logic import bussiness_context
import pandas as pd
from core import analisis
from config import my_globals
import plotly.express as px



# Configuración inicial de la página
st.set_page_config(page_title="CineDex", layout="wide")

# Mostrar logo + título alineados a la izquierda
col_logo, col_title = st.columns([1, 8])  # Logo más pequeño, título más ancho

with col_logo:
    st.image("data/logo.png", width=500)

with col_title:
    st.markdown(
        """
        <h1 style='text-align: center; padding-top: 10px; margin-bottom: 0px;'>
            <span style='color:#ffffff;'>Cine</span><span style='color:#ffcc00;'>Dex</span>
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Sidebar de navegación
st.sidebar.title("📂 Menú principal")
opcion = st.sidebar.radio(
    "Selecciona una opción:",
    [
        "📊 Análisis",
        "📽️ Mis Peliculas",
        "🔍 Consultar película",
        "➕ Agregar película",
        "✏️ Remplazar y Eliminar",
        "🗑️ Eliminar película"
    ]
)


# Vista principal según lo que el usuario elija
if opcion ==  "📽️ Mis Peliculas":
    st.subheader( "📽️ Mis Peliculas")
    #Mi codigo
    peliculas_guardadas = analisis.Cantidad_total_de_películas_guardadas()
    st.dataframe(peliculas_guardadas)

elif opcion == "📊 Análisis":
    st.subheader("📊 Análisis de las películas")

    # Fila 1
    fila1_col1, fila1_col2 = st.columns(2)
    fila2_col1, fila2_col2 = st.columns(2)

    with fila1_col1:
        st.markdown("### 🌟 Top 5 películas más populares")
        top5_df = analisis.top5_movies()
        if not top5_df.empty:
            fig_top5 = px.bar(
                top5_df,
                x="popularidad",
                y="title",
                orientation='h',
                color="popularidad",
                color_continuous_scale="sunset",
                labels={"title": "Película", "popularidad": "Popularidad"},
                height=350
            )
            fig_top5.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_top5, use_container_width=True)
        else:
            st.info("No hay datos para el Top 5.")

    with fila1_col2:
        st.markdown("### 🌟 🎭 Cantidad de películas por género")
        count_genre = analisis.count_by_genre()
        if not count_genre.empty:
            fig_genre = px.bar(
                count_genre,
                x="generos",
                y="cantidad",
                orientation="v",
                color="generos",
                color_continuous_scale="sunset",
                labels={"generos": "Género", "cantidad": "Cantidad de películas"},
                height=350
            )
            st.plotly_chart(fig_genre, use_container_width=True)
        else:
            st.info("No hay datos por género.")

    with fila2_col1:
        
        st.markdown("### 🌍⭐ Votaciones promedio por país")
        votaciones_pais = analisis.promedio_votaciones_por_pais()

        if not votaciones_pais.empty:
            fig_pais = px.choropleth(
            votaciones_pais,
            locations="paises",  # ← esta columna debe tener nombres como "United States"
            locationmode="country names",  # ← esto le dice a Plotly que no estás usando códigos ISO
            color="promedio_votaciones",
            hover_name="paises",
            hover_data=["promedio_votaciones", "peliculas_destacadas"],
            color_continuous_scale="Viridis",
            range_color=(
                votaciones_pais["promedio_votaciones"].min(),
                votaciones_pais["promedio_votaciones"].max()
            ),
            labels={"promedio_votaciones": "Prom. de votación"},
            height=350
            )

            #fig_pais.update_geos(projection_type="natural earth")
            #st.plotly_chart(fig_pais, use_container_width=True)
            fig_pais.update_geos(
            showcoastlines=True,
            coastlinecolor="white",          # ← bordes blancos
            showframe=False,
            showland=True,
            landcolor="rgb(40,40,40)",       # ← color del mapa base (oscuro)
            bgcolor="rgba(0,0,0,0)",         # ← fondo del canvas transparente
            projection_type="natural earth"
            )

            fig_pais.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",   # fondo de la hoja
            plot_bgcolor="rgba(0,0,0,0)"     # fondo del gráfico
            )

            st.plotly_chart(fig_pais, use_container_width=True)


            
        else:
            st.info("No hay datos para mostrar en el mapa.")
     
    with fila2_col2:
        
        st.markdown("### 🎬💲 Recuado por titulo")
        recaudo = analisis.recaudado_por_titulo()

        if not votaciones_pais.empty:
            fig_recaudado = px.bar(
            recaudo,
            x='title',
            y='recaudo_usd',
            orientation='v',
            color='title',
            color_continuous_scale='sunset',
            labels={"title": "peliculas", "cantidad_recudada": "recaudo_usd"},
            
            )

            st.plotly_chart(fig_recaudado, use_container_width=True)
         
        else:
            st.info("No hay datos para mostrar en el mapa.")

    





        
elif opcion == "🔍 Consultar película":
    st.subheader("🔍 Consultar película por título")
    # Aquí pondremos un input de texto + llamada a tu función
    titulo = st.text_input("Escribe el título de la película")

    if st.button("Buscar"):
        if titulo.strip() == "" or not isinstance(titulo, str) :
            st.warning("Por favor, escribe un titulo valido")
        else:
            resultado = bussiness_context.mostrar_peliculas(titulo)
        
        if resultado:
            st.success(f" Titulo consultado: {titulo}")
            st.dataframe(resultado)

elif opcion == "➕ Agregar película":
    st.subheader("➕ Agregar película por ID")
    # Aquí pondremos un input de ID + botón para guardar
    pelicula_id = st.text_input("Escribe el ID de la pelicula que quiera agrgar")


    if st.button("Agregar"):
        try:
            pelicula_id =int(pelicula_id)
            df = pd.read_csv(my_globals.file)

            if pelicula_id in df['id'].values:
                st.warning("Esta pelicula ya la tenemos")
            else:
                pelicula_elegida = bussiness_context.elegir_peli(pelicula_id)
                df = pd.DataFrame([pelicula_elegida]).set_index('id')
                st.dataframe(df)
                st.success(F"Guardado correctamente")
        
        except ValueError:
            st.error("Error confirme si el ID colocado es valido o Exisite")




elif opcion == "✏️ Remplazar y Eliminar":
    st.subheader("✏️ Remplazar y Eliminar por ID")
    
    col1, col2 = st.columns(2)

    with col1:
        old_id = st.text_input("🎬 ID actual (a reemplazar)", key="old_id")
    
    with col2:
        new_id = st.text_input("🆕 Nuevo ID (para reemplazar)", key="new_id")


    if st.button("remplazar"):
        try:
            old_id = int(old_id)
            new_id = int(new_id)

           
            mensaje = bussiness_context.reemplazar_pelicula_csv(old_id, new_id)

            df = pd.read_csv(my_globals.file)

            st.success(mensaje)
            
            df_remplazado = df[df["id"] == new_id]

            st.dataframe(df_remplazado)

            
            
        except ValueError:
            st.warning("Verifique que el ID sea un numero entero valido")
            

elif opcion == "🗑️ Eliminar película":
    st.subheader("🗑️ Eliminar película por ID")
    # Input de ID + botón para eliminar
    pelicula_id = st.text_input("Escribe el ID de la pelicula que quiere borrar ")
    if st.button("Eliminar"):
        try:
            pelicula_id = int(pelicula_id)
            pelicula_eliminada = bussiness_context.eliminar_pelicula(pelicula_id)
            st.success(f"Pelicula Eliminada: {pelicula_id}")
            st.dataframe(pelicula_eliminada)
        
        except Exception as e:
            st.error("El ID no es valido")





#print("Streamlit:", streamlit.__version__)
#print("Pillow:", PIL.__version__)