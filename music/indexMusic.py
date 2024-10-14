import os
import time
import pygame

# Inicializar pygame y su mezclador
pygame.mixer.init()

# Función para obtener los archivos MP3
def obtener_archivos_mp3(ruta_base):
    archivos_mp3 = {}
    for octava in range(3, 8):  # De C3 a C7 para cubrir más octavas
        nombre_carpeta = f'C{octava}'
        ruta_carpeta = os.path.join(ruta_base, nombre_carpeta)
        if os.path.isdir(ruta_carpeta):
            archivos_mp3[nombre_carpeta] = {}
            notas = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
            for nota in notas:
                nombre_archivo = os.path.join(ruta_carpeta, f'{nota}.mp3')
                if os.path.isfile(nombre_archivo):
                    archivos_mp3[nombre_carpeta][nota] = nombre_archivo
                else:
                    print(f'No se encontró el archivo: {nombre_archivo}')
        else:
            print(f'No se encontró la carpeta: {ruta_carpeta}')
    return archivos_mp3

# Ruta base donde están las carpetas de las notas
ruta_base = 'Piano'
archivos_mp3 = obtener_archivos_mp3(ruta_base)


# Mano izquierda (bajos, acordes en octavas graves)
ritmo_acordes_izquierda = [
    (0.8, ['C', 'D#', 'G'], 'C3'),   # Cm en la octava C3
    (1.0, "Pausa", None),            # Pausa de 1.0 segundos
    (0.8, ['G', 'A#', 'D'], 'C3'),   # Gm en la octava C3
    (1.0, "Pausa", None),            # Pausa de 1.0 segundos
    (0.8, ['F', 'G#', 'C'], 'C3'),   # Fm en la octava C3
    (0.2, ['F', 'G#', 'C'], 'C3'),   # Fm en la octava C3
    (0.8, ['D#', 'G', 'A#'], 'C3'),  # Eb en la octava C3
]

# Mano derecha (melodía, acordes en octavas agudas)
ritmo_acordes_derecha = [
    (0.4, ['C', 'D#', 'G'], 'C5'),   # Cm en la octava C5 (melodía)
    (0.6, ['D#', 'G', 'A#'], 'C5'),  # Eb en la octava C5
    (0.8, ['A#', 'D', 'F'], 'C5'),   # Bb en la octava C5
    (0.4, ['G#', 'C', 'D#'], 'C5'),  # Ab en la octava C5
    (1.0, "Pausa", None),            # Pausa de 1.0 segundos
    (0.8, ['C', 'D#', 'G'], 'C5'),   # Cm en la octava C5 (melodía)
]




# Función para reproducir un acorde o una pausa
def reproducir_acorde(acorde, duracion, octava, canal):
    if acorde == "Pausa":
        time.sleep(duracion)
    else:
        # Crear un objeto Sound de pygame para reproducir el sonido
        notas_a_reproducir = []
        for nota in acorde:
            if nota in archivos_mp3[octava]:
                notas_a_reproducir.append(archivos_mp3[octava][nota])

        if len(notas_a_reproducir) >= 1:
            sonido = pygame.mixer.Sound(notas_a_reproducir[0])
            canal.play(sonido)
            time.sleep(duracion)  # Esperar la duración del acorde o la pausa

# Función para reproducir los acordes de ambas manos simultáneamente
def reproducir_dos_manos(ritmo_izquierda, ritmo_derecha):
    canal_izq = pygame.mixer.Channel(0)  # Canal para la mano izquierda
    canal_der = pygame.mixer.Channel(1)  # Canal para la mano derecha

    for i in range(min(len(ritmo_izquierda), len(ritmo_derecha))):
        duracion_izq, acorde_izq, octava_izq = ritmo_izquierda[i]
        duracion_der, acorde_der, octava_der = ritmo_derecha[i]

        # Reproducir ambos acordes simultáneamente en diferentes canales
        reproducir_acorde(acorde_izq, duracion_izq, octava_izq, canal_izq)
        reproducir_acorde(acorde_der, duracion_der, octava_der, canal_der)

        # Esperar la duración mínima entre las dos manos
        time.sleep(min(duracion_izq, duracion_der))

# Iniciar las dos manos en secuencia
try:
    while True:
        reproducir_dos_manos(ritmo_acordes_izquierda, ritmo_acordes_derecha)

except KeyboardInterrupt:
    print('Reproducción interrumpida por el usuario.')
finally:
    pygame.mixer.quit()  # Cerrar el mezclador de pygame cuando termines
