class Restaurant:

    def agregar_restaurant(self, nombre):
        self.nombre = nombre


    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')



restaurant = Restaurant()
# print(restaurant)
restaurant.agregar_restaurant('Pizza PHP')
restaurant.mostrar_informacion()


restaurant2 = Restaurant()
# print(restaurant)
restaurant2.agregar_restaurant('Hamburguesas Python')
restaurant2.mostrar_informacion()