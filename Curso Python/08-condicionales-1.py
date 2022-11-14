# Revisar si una condicion es mayor a
balance = 500
if balance > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')

# Likes
likes = 200
if likes >= 200:
    print(f'Tienes {likes} likes')
else:
    print('casi llegas a los 200')

#If con texto
lenguaje = 'PHP'
if not lenguaje == 'Python':
    print('Excelente decision')

# Evaluar un Boolean
usuario_autenticado = True
if usuario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')

#Evaluar un elemento de una lista
lenguajes = ['Python','Kotlin','Java','JS','PHP']
if 'PHP' in lenguajes:
    print('PHP si existe')
else:
    print('No esta en la lista')

# IF anidados
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesion')