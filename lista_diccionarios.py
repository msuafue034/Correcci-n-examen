# Repetir el enunciado del examen 

# 1. Cargar lista:
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

# 2 Añadir canción:
def añadir_cancion(lista_canciones, cancion_nueva, artista_nuevo, genero_nuevo):
    encontrada == True
    
    #Buscar
    
    if encontrada == True:
        print(f"La canción {cancion_nueva} ya está añadida a la lista de canciones")
    else:
        diccionario = {
            "nombre":cancion_nueva,
            "artista":artista_nuevo,
            "genero":genero_nuevo,
        }
        lista_canciones.append(diccionario)
        print(f"La canción {cancion_nueva} se ha añadido con éxito.")
    return lista_canciones
    

# 3 Eliminar canción:


# 4 Contar Canciones:
 

# 5. Buscar por artista:


# 6. Ordenar por orden alfabético:


# 7. Crear lista aleatoria:


# 8. Guardar lista:



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


# 4. Contar canciones:


# 5. Buscar por artista:


# 6. Ordenar por orden alfabético:


# 7. Crear lista aleatoria:


# 8. Guardar lista:

