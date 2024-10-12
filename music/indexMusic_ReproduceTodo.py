import os
import random
from pydub import AudioSegment
import simpleaudio as sa

def obtener_archivos_mp3(ruta_base):
    archivos_mp3 = {}
    for octava in range(1, 8):  # De C1 a C7
        nombre_carpeta = f'C{octava}'
        ruta_carpeta = os.path.join(ruta_base, nombre_carpeta)
        if os.path.isdir(ruta_carpeta):
            archivos_mp3[nombre_carpeta] = {
                'notas': []
            }
            # Agregar todas las notas (blancas y negras) de la octava
            notas = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
            for nota in notas:
                nombre_archivo = os.path.join(ruta_carpeta, f'{nota}.mp3')
                if os.path.isfile(nombre_archivo):
                    archivos_mp3[nombre_carpeta]['notas'].append(nombre_archivo)
                else:
                    print(f'No se encontró el archivo: {nombre_archivo}')
        else:
            print(f'No se encontró la carpeta: {ruta_carpeta}')
    return archivos_mp3

# Ruta base donde están las carpetas de las octavas
ruta_base = 'Piano'  # Carpeta principal

# Obtener los archivos MP3
archivos_mp3 = obtener_archivos_mp3(ruta_base)

# Lista de octavas a reproducir (C1 a C7)
octavas_a_reproducir = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']

# Verificar que hay sonidos disponibles
if not archivos_mp3:
    print('No se encontraron archivos de sonido para las octavas especificadas.')
    exit(1)

# Reproducción de una octava simulando un teclado de piano
try:
    while True:
        for octava in octavas_a_reproducir:
            if octava in archivos_mp3:
                # Seleccionar una nota aleatoria de la octava
                if archivos_mp3[octava]['notas']:
                    nota = random.choice(archivos_mp3[octava]['notas'])
                    audio = AudioSegment.from_mp3(nota)
                    sa.play_buffer(audio.raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)
                    print(f'Reproduciendo nota: {nota}')
except KeyboardInterrupt:
    print('Reproducción interrumpida por el usuario.')
