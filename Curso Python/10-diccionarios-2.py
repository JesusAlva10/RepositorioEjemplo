jugador = {}
print(jugador)

jugador['nombre'] = 'Jesus'
jugador['puntaje'] = 0
print(jugador)

# Incremetar el puntaje
jugador['puntaje'] = 100
print(jugador)

# Incremetar el puntaje
jugador['puntaje'] = 200
print(jugador)

# Acceder a un valor
print(jugador.get('consola', 'No existe ese valor'))

# Iterar en el diccionaro
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#Eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']
print(jugador)


