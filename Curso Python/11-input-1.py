nombre = input('Cual es tu nombre: \r\n')
print(f'Hola {nombre}')

#Datos que seran numeros
edad = input('Cual es tu edad: \r\n')
#Convertir edad (String) a int
edad = int(edad)
if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aun no puedes votar')

#Mezclarlo con operadores
numero = input('Agrega un numero y te dire si es par o non:  \r\n')
numero = int(numero)
if numero % 2 == 0:# operador modulo %
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')
