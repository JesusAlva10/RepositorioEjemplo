class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria#Defaul: public
        self.precio = precio #Protected con _

    def mostrar_informacion(self):
        print(f'\r\nNombre: {self.nombre}')
        print(f'Categoria: {self.categoria}')
        print(f'Precio: {self.precio}')

    #GETTERS Y SETTERS - get = obtiene un valor, set = agrega un valor
    def get_precio(self):
        print(self.precio)
    
    def set_precio(self, precio):
        self.precio = precio

#Crea una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca
    # Reescribir un metodo (debe llamarse igual)
    def mostrar_informacion(self):
        print(f'\r\nNombre: {self.nombre}')
        print(f'Categoria: {self.categoria}')
        print(f'Precio: {self.precio}')
        print(f'Alberca: {self.alberca}')


    #Agregar un metodo que solo exista en hotel
    def get_alberca(self):
        return self.alberca

hotel = Hotel('Hotel POO', '5 estrellas', 200, 'si')

hotel.mostrar_informacion()