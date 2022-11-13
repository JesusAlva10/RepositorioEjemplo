lenguajes = ['Python','Kotlin','Java','JS']
print(lenguajes)

print(lenguajes[0])

# Ordenar los elementos
lenguajes.sort()
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

# Modificando valores de un arreglo
lenguajes[2] = 'PHP'
print(lenguajes)

# Agregando elementos
lenguajes.append('Ruby')
print(lenguajes)

# Eliminando elementos
del lenguajes[1]
print(lenguajes)

# Eliminar de un arreglo
lenguajes.pop()# Elimina el ultimo elemento
print(lenguajes)

# Eliminar con pop una posicion en especifico
lenguajes.pop(0)# Elimina el ultimo elemento
print(lenguajes)

# Eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)

