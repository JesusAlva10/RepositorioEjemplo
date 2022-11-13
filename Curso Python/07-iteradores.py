lenguajes = ['Python','Kotlin','Java','JS','PHP','Rugby','GO']

print(lenguajes)

# Iteradores
for lenguaje in lenguajes:
    print(f'Estoy aprendiendo {lenguaje}')
# Este print indentado esta dentro del for por la indentacion
    print('Texto dentro')
# Este print no indentado esta fuera del for por la indentacion
print('Texto fuera')

# For que escriba numeros
for numero in range(0, 10):
    print(numero)

# For con intervalo
for numero in range(0, 10, 3):
    print(numero)

