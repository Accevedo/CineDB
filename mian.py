
from logic.bussiness_context import mostrar_peliculas, elegir_peli, eliminar_pelicula, reemplazar_pelicula_csv
from core.api_handler import pelis_info_by_id


#print(pelis_info_by_id(346698))

while True:
    print(" Elija una de las siguientes opciones ")
    print("1. Mostrar peliculas disponible por titulo")
    print("2. Agregar tu pelicula por ID, seleccione el ID de la pelicula que quiere agregar")
    print("3. Remplaza una pelciula exisitente por otra ")
    print("4. Eliminar pleicula ")
    print("5. Salir del menu")
    
    option = input("Elija una opcion: ")
    
    if option == "1":
        nombre_titulo = input("Elija el titulo que quiere consultar: ").strip()
        list_dict_peliculas = mostrar_peliculas(nombre_titulo)
        list_dict_peliculas
    elif option == "2":
        pelicula_elegida_id = int(input("Seleccione ID de la pelicula que quiere a gregar a su lista: "))
        list_dict_peliculas
        Pelicula_elegida = elegir_peli(pelicula_elegida_id, list_dict_peliculas)
        print(Pelicula_elegida)
    elif option == "3":
        nueva_pelicula = int(input("Coloque el ID del titulo que quiere cambiar: ").strip())
        remplazar = reemplazar_pelicula_csv(nueva_pelicula)
        print(remplazar)
    elif option == "4":
        pileicula_id = int(input("Elija el ID que quiere elimnar").strip())
        pelicula_eliminada = eliminar_pelicula(pileicula_id)
        print(pelicula_eliminada)
    elif option == "5":
        print("Saliendo del menú...")
        break
    else:
        print("Opción inválida. Por favor, elija una opción válida.")