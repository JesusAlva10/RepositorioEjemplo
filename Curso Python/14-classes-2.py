class Restaurant:
    #constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f'\r\nNombre: {self.nombre}')
        print(f'Categoria: {self.categoria}')
        print(f'Precio: {self.precio}')

#El constructor se ejecuta automaticamente al generar una instancia

restaurant = Restaurant('Pizzeria', 'Comida', 50)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburguesas', 'Comida', 20)
restaurant2.mostrar_informacion()
