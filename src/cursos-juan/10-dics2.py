
jugador = {}
print(jugador)


jugador['nombre'] = 'Pepe'
jugador['puntaje'] = 0
print(jugador)


jugador['puntaje'] = 100
print(jugador)


#Acceder
print(jugador.get('consola', 'No existe ese valor'))


#Iterar
for llave, valor in jugador.items():
    print(valor)

#eliminar y puntaje

del jugador['nombre']
del jugador['puntaje']
print(jugador)
