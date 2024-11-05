import random

lista_musica = {}

#1. 
def cargar_lista(nombre_archivo):
    with open(nombre_archivo, "r") as fichero:
        for linea in fichero:
            cancion, artista = linea.strip().split(" - ")
            lista_musica[cancion] = artista
    return lista_musica

# 2.
def agregar_cancion(lista, cancion, artista):
    lista[cancion] = artista
    return lista

# 3.
def eliminar_cancion(lista, cancion):
    if cancion in lista:
        del lista[cancion]
        print(f"Canción '{cancion}' eliminada con éxito")
    else:
        print(f"La canción '{cancion}' no se encuentra en la lista.")
    return lista

# 4.
def contar_canciones(lista):
    return len(lista)

# 5.
def buscar_por_artista(lista, artista):
    canciones_artista = []
    if artista in lista.values():
        for cancion, art in lista.items():
            if art == artista:
                canciones_artista.append(cancion)
        return canciones_artista

# 6.
def ordenar_alfabeticamente(lista):
    return sorted(lista.items())

# 7.
def crear_lista_aleatoria(lista, n):
    return random.sample(list(lista.items()), n)

# 8.
def guardar_lista(lista, nombre_archivo):
    with open(nombre_archivo, "w") as fichero:
        for cancion, artista in lista.items():
            fichero.write(f"{cancion} - {artista}\n")
    print(f"Lista guardada en {nombre_archivo}")



# 1. Cargar lista:
lista_musica = cargar_lista("playlist.txt")

cancion = input("Introduce un nombre de canción: ")
artista = input("Introduce el nombre de un artista: ")
lista_musica = agregar_cancion(lista_musica, cancion, artista)

# 3. Eliminar canción
cancion_eliminar = input("Introduce un nombre de canción para eliminarla: ")
lista_musica = eliminar_cancion(lista_musica, cancion_eliminar)

# 4. Contar Canciones
numero_canciones = contar_canciones(lista_musica)
print(f"Hay {numero_canciones} canciones en la lista.")

# 5. Buscar por artista
artista_buscar = input("Introduce el nombre del artista a buscar: ")
canciones_artista = buscar_por_artista(lista_musica, artista_buscar)
print(f"Canciones de {artista_buscar}: {canciones_artista}")

# 6. Ordenar por orden alfabético
lista_ordenada = ordenar_alfabeticamente(lista_musica)
print("Lista ordenada:", lista_ordenada)

# 7. Crear lista aleatoria
num_canciones_aleatorias = int(input("Número de canciones para la lista aleatoria: "))
lista_aleatoria = crear_lista_aleatoria(lista_musica, num_canciones_aleatorias)
print("Lista aleatoria de reproducción:", lista_aleatoria)

# 8. Guardar lista
guardar_lista(lista_musica, "nueva_playlist.txt")
