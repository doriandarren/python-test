import os
import pygame
import random
import time

def obtener_archivos_mp3(ruta_base):
    archivos_mp3 = {}
    for nota in range(4, 8):  # De C4 a C7
        nombre_carpeta = f'C{nota}'
        ruta_carpeta = os.path.join(ruta_base, nombre_carpeta)
        if os.path.isdir(ruta_carpeta):
            archivos_mp3[nombre_carpeta] = []
            for i in range(1, 8):  # De Cx-1.mp3 a Cx-7.mp3
                nombre_archivo = f'{nombre_carpeta}-{i}.mp3'
                ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
                if os.path.isfile(ruta_archivo):
                    archivos_mp3[nombre_carpeta].append(ruta_archivo)
                else:
                    print(f'No se encontró el archivo: {ruta_archivo}')
        else:
            print(f'No se encontró la carpeta: {ruta_carpeta}')
    return archivos_mp3

# Inicializar pygame
pygame.init()
pygame.mixer.init()

# Ruta base donde están las carpetas de las notas
ruta_base = 'Piano'  # Asegúrate de que esta ruta es correcta

# Obtener los archivos MP3
archivos_mp3 = obtener_archivos_mp3(ruta_base)

# Lista de notas a reproducir
notas_a_reproducir = ['C4', 'C5', 'C6', 'C7']

# Crear una lista de todos los archivos de las notas
lista_sonidos = []
for nota in notas_a_reproducir:
    archivos_nota = archivos_mp3.get(nota, [])
    if archivos_nota:
        lista_sonidos.extend(archivos_nota)
    else:
        print(f'No se encontraron archivos para la nota {nota}')

# Verificar que hay sonidos disponibles
if not lista_sonidos:
    print('No se encontraron archivos de sonido para las notas especificadas.')
    pygame.quit()
    exit(1)

# Definir parámetros del compás
beats_por_compas = 4  # Número de beats por compás

# Definir la secuencia de la escala (subir y luego bajar)
escala_duracion = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4]

# Inicializar el índice de la escala
indice_escala = 0
ascendente = True  # Para controlar la dirección de la escala

# Reproducción continua en compás
try:
    ultimo_sonido = None
    while True:
        for beat in range(beats_por_compas):
            # Seleccionar un sonido aleatorio que no sea el mismo que el último reproducido
            sonido_actual = random.choice(lista_sonidos)
            while sonido_actual == ultimo_sonido and len(lista_sonidos) > 1:
                sonido_actual = random.choice(lista_sonidos)
            ultimo_sonido = sonido_actual

            try:
                # Cargar y reproducir el archivo MP3
                sonido = pygame.mixer.Sound(sonido_actual)
                sonido.play()
                print(f'Compás {beat+1}/{beats_por_compas} - Reproduciendo: {sonido_actual}')
                
                # Asignar la duración del beat según la escala
                duracion_beat = escala_duracion[indice_escala]

                # Esperar a que termine de reproducir el sonido o hasta el siguiente beat
                tiempo_de_reproduccion = duracion_beat * 1000  # Convertir a milisegundos
                pygame.time.delay(int(tiempo_de_reproduccion))
                
                # Actualizar el índice de la escala (subir y luego bajar)
                if ascendente:
                    indice_escala += 1
                    if indice_escala == len(escala_duracion) - 1:  # Si llegamos al final de la subida
                        ascendente = False
                else:
                    indice_escala -= 1
                    if indice_escala == 0:  # Si llegamos al final de la bajada
                        ascendente = True

            except pygame.error as e:
                print(f'Error al reproducir {sonido_actual}: {e}')

        print('Compás completo. Iniciando nuevo compás...\n')
        # Pausa opcional entre compases
        time.sleep(1)  # Pausar por 1 segundo entre compases

except KeyboardInterrupt:
    print('Reproducción interrumpida por el usuario.')
finally:
    pygame.quit()
