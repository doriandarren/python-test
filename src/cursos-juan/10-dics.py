#Diccionario simple

cancion = {
    'artista' : 'Metalica',
    'cancion' : 'Enter Dandman',
    'lanzamiento': 1992,
    'likes' : 3000
}

print(cancion['artista'])
print(cancion['lanzamiento'])


artista = cancion['artista']
print(f'Estoy escuchando {artista}')


cancion['playlist'] = 'Heavy metal'
print(cancion)

