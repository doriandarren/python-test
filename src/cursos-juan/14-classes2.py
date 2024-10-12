class Restaurant:

    

    def __init__(self, nombre, categoria, precio):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio


    def mostrar_informacion(self):
        print(f'Nombre: {self.__nombre}, Categoría: {self.__categoria}, Precio: {self.__precio}')

    



restaurant = Restaurant('Pizza PHP', 'Comida Italiana', 20)
# print(restaurant)
restaurant.mostrar_informacion()



restaurant2 = Restaurant('Hamburguesas Python', 'Comida casual', 40)
# print(restaurant)
restaurant2.mostrar_informacion()
