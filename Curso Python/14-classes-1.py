class Restaurant:
    #self
    def agregar_restaurant(self, nombre):
        self.nombre = nombre
        print('Agregando')

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

#instanciar clase
restaurant = Restaurant()
restaurant.agregar_restaurant('Pizzeria')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hamburguesas')
restaurant2.mostrar_informacion()

#Mostrar la informacion
print(f'Nombre restaurant: {restaurant.nombre}')
print(f'Nombre restaurant: {restaurant2.nombre}')

