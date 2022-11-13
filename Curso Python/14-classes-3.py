# hERENCIA
class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria#Defaul: public
        self.__precio = precio #Protected con _ , private con doble __

    def mostrar_informacion(self):
        print(f'\r\nNombre: {self.nombre}')
        print(f'Categoria: {self.categoria}')
        print(f'Precio: {self.__precio}')

    #GETTERS Y SETTERS - get = obtiene un valor, set = agrega un valor
    def get_precio(self):
        print(self.__precio)
    
    def set_precio(self, precio):
        self.__precio = precio

#Crea una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 estrellas', 200)

hotel.mostrar_informacion()