import os
import random
import time
from pydub import AudioSegment
import simpleaudio as sa

def obtener_archivos_mp3(ruta_base):
    archivos_mp3 = {}
    for octava in range(4, 8):  # De C4 a C7 (puedes cambiarlo a C1 a C7 si es necesario)
        nombre_carpeta = f'C{octava}'
        ruta_carpeta = os.path.join(ruta_base, nombre_carpeta)
        if os.path.isdir(ruta_carpeta):
            archivos_mp3[nombre_carpeta] = {}
            # Agregar todas las notas (blancas y negras) de la octava
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
ruta_base = 'Piano'  # Carpeta principal donde están las octavas

# Obtener los archivos MP3
archivos_mp3 = obtener_archivos_mp3(ruta_base)

# Combinaciones de notas agradables (acordes mayores y menores)
combinaciones_agradables = [
    ['C', 'E', 'G'],  # C mayor
    ['A', 'C', 'E'],  # A menor
    ['G', 'B', 'D'],  # G mayor
    ['D', 'F', 'A'],  # D menor
    ['E', 'G#', 'B'],  # E mayor
    ['F', 'A', 'C'],  # F mayor
    ['C', 'E', 'G', 'Bb'],  # C7 (séptima)
]

# Lista de octavas a reproducir
octavas_a_reproducir = ['C4', 'C5', 'C6', 'C7']

# Verificar que hay sonidos disponibles
if not archivos_mp3:
    print('No se encontraron archivos de sonido para las octavas especificadas.')
    exit(1)

# Definir parámetros del compás
beats_por_compas = 4  # Número de beats por compás

# Definir la secuencia de la escala (subir y luego bajar)
escala_duracion = [0.1, 0.2, 0.3, 0.4, 0.5, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4]

# Inicializar el índice de la escala
indice_escala = 0
ascendente = True  # Para controlar la dirección de la escala

# Reproducción continua en compás con acordes agradables
try:
    while True:
        for beat in range(beats_por_compas):
            # Seleccionar una combinación agradable de notas (acorde)
            combinacion = random.choice(combinaciones_agradables)

            # Reproducir la combinación en una octava aleatoria
            octava = random.choice(octavas_a_reproducir)

            notas_a_reproducir = []
            for nota in combinacion:
                if nota in archivos_mp3[octava]:
                    notas_a_reproducir.append(archivos_mp3[octava][nota])

            if len(notas_a_reproducir) >= 2:  # Asegurarse de tener al menos dos notas
                audio_1 = AudioSegment.from_mp3(notas_a_reproducir[0])
                audio_2 = AudioSegment.from_mp3(notas_a_reproducir[1])

                # Convertir los sonidos a simpleaudio para reproducirlos
                audio_1 = sa.play_buffer(audio_1.raw_data, num_channels=audio_1.channels, bytes_per_sample=audio_1.sample_width, sample_rate=audio_1.frame_rate)
                audio_2 = sa.play_buffer(audio_2.raw_data, num_channels=audio_2.channels, bytes_per_sample=audio_2.sample_width, sample_rate=audio_2.frame_rate)

                print(f'Compás {beat+1}/{beats_por_compas} - Reproduciendo: {combinacion} en la octava {octava}')

                # Asignar la duración del beat según la escala
                duracion_beat = escala_duracion[indice_escala]

                # Esperar la duración del beat
                time.sleep(duracion_beat)

            # Actualizar el índice de la escala (subir y luego bajar)
            if ascendente:
                indice_escala += 1
                if indice_escala == len(escala_duracion) - 1:  # Si llegamos al final de la subida
                    ascendente = False
            else:
                indice_escala -= 1
                if indice_escala == 0:  # Si llegamos al final de la bajada
                    ascendente = True

        print('Compás completo. Iniciando nuevo compás...\n')
        # Pausa opcional entre compases
        time.sleep(1)  # Pausar por 1 segundo entre compases

except KeyboardInterrupt:
    print('Reproducción interrumpida por el usuario.')
