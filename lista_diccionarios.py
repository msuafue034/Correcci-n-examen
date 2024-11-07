# Repetir el enunciado del examen pero con las cancioner organizadas en lista de diccionarios.
    #* Try-except
    #* Comprobar el nº de valores ficheros (comprobar si tiene tres elementos por diccionario)
    #* Crear función buscar_cancion
    #* Crear en un fichero con formato JSON

import json

# Cargar lista:
def cargar_lista(nombre_archivo):
    lista_musica = []
    try:
        with open(nombre_archivo, "r") as fichero:
            for linea in fichero:
                elementos = linea.strip().split(" - ")
                if len(elementos) == 3:
                    cancion, artista, genero = elementos
                    print(f"Cancion: {cancion} - Artista: {artista} - Genero: {genero}")
                    diccionario = {
                        "nombre": cancion,
                        "artista": artista,
                        "genero": genero,
                    }
                    lista_musica.append(diccionario)
        return lista_musica
    except FileNotFoundError:
        print("No se ha podido encontrar el fichero. Inténtelo de nuevo")
        return[]

# Añadir canción:
def añadir_cancion(lista, cancion_nueva, artista_nuevo, genero_nuevo):
    
    indice = buscar_cancion(lista, cancion_nueva)
    
    if indice >= 0:
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
    indice = buscar_cancion(lista, nombre_cancion)
    
    if indice < 0:
        print(f"La canción {nombre_cancion} no se encuentra en la lista.")
    else:
        del lista[indice]
        print(f"La canción {nombre_cancion} se ha eliminado con éxito.")

# Guardar lista:
def guardar_lista(lista, nombre_archivo):
    with open(nombre_archivo, "w") as fichero:
        for cancion in lista:
            fichero.write(f"{cancion['nombre']} - {cancion['artista']} - {cancion['genero']}\n")
    print(f"Lista guardada en {nombre_archivo}")
    
# Guardar lista en JSON:
def guardar_json(lista, archivo_json):
    try:
        with open(archivo_json, "w") as fichero:
            lista = json.dump(lista, fichero, indent=4, ensure_ascii=False) #Indent para formato, ensure_ascii para que guarde elementos especiales como tildes
            return lista
            # Se pueden cambiar estas dos últimas líneas por [return json.load(fichero)]
            print(f"Lista guardada correctamente en formato JSON \n- Ubicación: {archivo_json}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no ha podido encontrarse")
        return []
    

# Buscar canción:
def buscar_cancion(lista, nombre_cancion):
    for i, cancion in enumerate(lista):
        if cancion["nombre"] == nombre_cancion:
            return i
    return -1
    #Se devuelve -1 o cualquier número menor a 0 --> Si no tiene índice (>=0) no existe 



###################### LLAMADAS A LAS FUNCIONES ######################

# 1. Cargar lista:
nombre_archivo = "biblioteca.txt"
lista_canciones = cargar_lista(nombre_archivo)
print("Lista cargada: ", lista_canciones)

# 2. Añadir canción:
cancion_nueva = input("Introduce el nombre de la canción a añadir: ")
artista_nuevo = input("Introduce el nombre del artista: ")
genero_nuevo = input("Introduce el género de la canción: ")
lista_canciones = añadir_cancion(lista_canciones, cancion_nueva, artista_nuevo, genero_nuevo)
print("Lista actualizada: ", lista_canciones)

# 3. Eliminar canción:
cancion_eliminar = input("Introduce el nombre de la canción para eliminarla: ")
eliminar_cancion(lista_canciones, cancion_eliminar)

# 4. Guardar lista:
guardar_lista(lista_canciones, nombre_archivo)

# Guardar la lista en JSON
archivo_json = "biblioteca.json"
guardar_json(lista_canciones, archivo_json)
