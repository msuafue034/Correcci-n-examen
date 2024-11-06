# Repetir el enunciado del examen pero con las cancioner organizadas en lista de diccionarios.
    # T-except
    # Comprobar el nº de valores ficheros (comprobar si tiene tres elementos por diccionario)
    # Crear función buscar_cancion
    # Crear en un fichero con formato JSON

# Cargar lista:
def cargar_lista(nombre_archivo):
    lista_musica = []
    with open (nombre_archivo, "r") as fichero:
        for linea in fichero:
            cancion, artista, genero = linea.strip().split(" - ")
            print(f"Cancion: {cancion} - Artista: {artista} - Genero: {genero}")
            diccionario = {
                "nombre":cancion,
                "artista":artista,
                "genero":genero,
            }
            lista_musica.append(diccionario)
    return lista_musica

# Añadir canción:
def añadir_cancion(lista, cancion_nueva, artista_nuevo, genero_nuevo):
    
    encontrada = buscar_cancion(lista, cancion_nueva)
    
    if encontrada == True:
        print(f"La canción {cancion_nueva} ya está añadida a la lista de canciones")
    else:
        diccionario = {
            "nombre":cancion_nueva,
            "artista":artista_nuevo,
            "genero":genero_nuevo,
        }
        lista.append(diccionario)
        print(f"La canción {cancion_nueva} se ha añadido con éxito.")
    return lista
    
# Eliminar canción:
def eliminar_cancion(lista, nombre_cancion):
    encontrada = buscar_cancion(lista, nombre_cancion)
    
    if encontrada == False:
        print(f"La canción {nombre_cancion} no se encuentra en la lista.")
    else:
        if cancion["nombre"] == nombre_cancion:
            lista.remove(cancion)
        print(f"La canción {nombre_cancion} se ha eliimnado con éxito.")
        
# Guardar lista:


# Buscar canción:
def buscar_cancion(lista, nombre_cancion):
    for cancion in lista:
        if cancion["nombre"] == nombre_cancion:
            return True
    return False

    



################ LLAMADAS A LAS FUNCIONES ################

# 1. Cargar lista:
nombre_archivo = "biblioteca.txt"
lista_canciones = cargar_lista(nombre_archivo)
print("\nLista cargada: ", lista_canciones)

# 2. Añadir canción:
cancion_nueva = input("Introduce el nombre de la canción a añadir: ")
artista_nuevo = input("Introduce el nombre del artista: ")
genero_nuevo = input("Introduce el género de la canción: ")
lista_canciones = añadir_cancion(lista_canciones, cancion_nueva, artista_nuevo, genero_nuevo)
print("\nLista actualizada: ", lista_canciones)

# 3. Eliminar canción:



# 8. Guardar lista:

