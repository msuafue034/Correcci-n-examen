import random

# 1. Cargar lista:
def cargar_lista(nombre_archivo):
    lista_musica = {}
    with open(nombre_archivo, "r") as fichero:  # Con 'with open' no hace falta cerrarlo
        for linea in fichero:
            cancion, artista = linea.strip().split(" - ")
            print(f"Canción: {cancion} - Artista: {artista}")
            lista_musica[cancion] = artista
    return lista_musica

# 2 Añadir canción:
def agregar_cancion(lista, cancion, artista):
    if cancion in lista:
        print("La canción ya está introducida en la lista.")
    else:
        lista[cancion] = artista
        print(f"La canción '{cancion}' de {artista} se ha añadido.")
    return lista

# 3 Eliminar canción:
def eliminar_cancion(lista, cancion):
    if cancion in lista:
        del lista[cancion]
        print(f"La canción '{cancion}' se ha eliminado correctamente.")
    else:
        print(f"La canción '{cancion}' no se encuentra en la lista.")

# 4 Contar Canciones:
def contar_canciones(lista):
    return len(lista)    

# 5. Buscar por artista:
def buscar_por_artista(lista, artista):
    canciones_artista = []
    for cancion in lista:
        if lista[cancion] == artista:
            canciones_artista.append(cancion)
    return canciones_artista

# 6. Ordenar por orden alfabético:
def ordenar_alfabeticamente(lista):
    return sorted(lista)

# 7. Crear lista aleatoria:
def crear_lista_aleatoria(lista, n):
    return random.sample(list(lista.items()), n)

# 8. Guardar lista:
def guardar_lista(lista, nombre_archivo):
    with open(nombre_archivo, "w") as fichero:
        for cancion, artista in lista.items():
            fichero.write(f"{cancion} - {artista}\n")
    print(f"Lista guardada en {nombre_archivo}")


################ LLAMADAS A LAS FUNCIONES ################

# 1. Cargar lista:
nombre_archivo = "playlist.txt"
lista_canciones = cargar_lista(nombre_archivo)
print("\nLista cargada:", lista_canciones)

# 2. Añadir canción:
cancion_nueva = input("Introduce el nombre de la canción a añadir: ")
artista_nuevo = input("Introduce el nombre del artista: ")
lista_canciones = agregar_cancion(lista_canciones, cancion_nueva, artista_nuevo)

# 3. Eliminar canción:
cancion_eliminar = input("Introduce el nombre de la canción para eliminarla: ")
eliminar_cancion(lista_canciones, cancion_eliminar)

# 4. Contar canciones:
print("Número de canciones en la lista:", contar_canciones(lista_canciones))

# 5. Buscar por artista:
artista_buscar = input("Introduce el nombre del artista para buscar sus canciones: ")
canciones_artista = buscar_por_artista(lista_canciones, artista_buscar)
print(f"Canciones de {artista_buscar}:", canciones_artista)

# 6. Ordenar por orden alfabético:
lista_ordenada = ordenar_alfabeticamente(lista_canciones)
print("Lista ordenada alfabéticamente:", lista_ordenada)

# 7. Crear lista aleatoria:
num_canciones = int(input("Número de canciones para la lista aleatoria: "))
lista_aleatoria = crear_lista_aleatoria(lista_canciones, num_canciones)
print("Lista aleatoria de reproducción:", lista_aleatoria)

# 8. Guardar lista:
guardar_lista(lista_canciones, nombre_archivo)
