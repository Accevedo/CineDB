#from logic.bussiness_context import mostrar_peliculas, elegir_peli, eliminar_pelicula, reemplazar_pelicula_csv
from core.analisis import cargar_datos,top5_movies,count_by_genre,count_by_country,promedio_votaciones_por_genero,duracion_promedio, recaudado_por_titulo, Cantidad_total_de_películas_guardadas, promedio_votaciones_por_pais,count_by_genre_runtime
from auditoria.logs_auditoria import generar_batch_id, procesar_detalle_pelicula, crear_lista_logs


#print(generar_batch_id())
#print(procesar_detalle_pelicula("Maria"))
#crear_lista_logs({"Pruba": 2})
#cargar_datos()
#top5_movies()
#count_by_genre()
#count_by_country()
#promedio_votaciones_por_genero()
#duracion_promedio()
#recaudado_por_titulo()
#Cantidad_total_de_películas_guardadas()
promedio_votaciones_por_pais()
#count_by_genre_runtime()