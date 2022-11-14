# Creando un diccionario simple
cancion = {
    'artista' : 'Metalica',
    'cancion' : 'Enter Sandman',
    'lanzamiento' : 1992,
    'likes' : 3000
}
#Acceder a los elementis del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

# Mezclar con un string
artista = cancion['artista']
print(f'Estoy escuchando {artista}')

# Agregar  un nuevo valor
cancion['playlist'] = 'Heavy metal'
print(cancion)

# Reemplazar valor existente
cancion['cancion'] = 'seek & destroy'
print(cancion)

# Eliminar un valor
del cancion['lanzamiento']
print(cancion)