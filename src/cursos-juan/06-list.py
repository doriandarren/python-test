lenguajes = ["Python", "Kotlin", "Java", "Javascript"]

#
print(lenguajes[0])

# Ordenar lengaujes
lenguajes.sort()
print(lenguajes) 

#Accder a un elemento
aprendiendo = f'Estoy aprendiento {lenguajes[3]}'
print(aprendiendo)


#Modificar
lenguajes[2] = 'PHP'
print(lenguajes)


# Agregar
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar
del lenguajes[1]
print(lenguajes)

lenguajes.pop()
print(lenguajes)


lenguajes.pop(0)
print(lenguajes)


lenguajes.remove('PHP')
print(lenguajes)
