import os
import time
from pydub import AudioSegment
import simpleaudio as sa

def obtener_archivos_mp3(ruta_base):
    archivos_mp3 = {}
    for octava in range(4, 8):  # De C4 a C7
        nombre_carpeta = f'C{octava}'
        ruta_carpeta = os.path.join(ruta_base, nombre_carpeta)
        if os.path.isdir(ruta_carpeta):
            archivos_mp3[nombre_carpeta] = {}
            # Notas disponibles en cada octava
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

# Acordes de "Just Dance" en formato para piano:
tus_acordes = [
    ['A', 'C', 'E'],   # Am
    ['C', 'E', 'G'],   # C
    ['G', 'B', 'D'],   # G
    ['D', 'F', 'A'],   # Dm
]

# Lista de octavas a reproducir (C4 a C7)
octavas_a_reproducir = ['C4', 'C5', 'C6', 'C7']

# Verificar que hay sonidos disponibles
if not archivos_mp3:
    print('No se encontraron archivos de sonido para las octavas especificadas.')
    exit(1)

# Definir el tempo de la canción (BPM)
bpm = 119  # El BPM de "Just Dance" es aproximadamente 119
duracion_beat = 60 / bpm  # Duración de un beat en segundos

# Reproducción continua en compás con tus acordes siguiendo el ritmo 4/4
try:
    while True:
        for acorde in tus_acordes:
            # Reproducir el acorde en una octava fija o aleatoria
            octava = 'C4'  # Puedes cambiarlo para variar entre octavas

            notas_a_reproducir = []
            for nota in acorde:
                if nota in archivos_mp3[octava]:
                    notas_a_reproducir.append(archivos_mp3[octava][nota])

            if len(notas_a_reproducir) >= 2:  # Asegurarse de tener al menos dos notas
                audio_1 = AudioSegment.from_mp3(notas_a_reproducir[0])
                audio_2 = AudioSegment.from_mp3(notas_a_reproducir[1])

                # Convertir los sonidos a simpleaudio para reproducirlos
                audio_1 = sa.play_buffer(audio_1.raw_data, num_channels=audio_1.channels, bytes_per_sample=audio_1.sample_width, sample_rate=audio_1.frame_rate)
                audio_2 = sa.play_buffer(audio_2.raw_data, num_channels=audio_2.channels, bytes_per_sample=audio_2.sample_width, sample_rate=audio_2.frame_rate)

                print(f'Reproduciendo acorde: {acorde} en la octava {octava}')

                # Esperar la duración de un compás (según el BPM y compás 4/4)
                time.sleep(duracion_beat * 4)  # 4 beats por compás

        # Repetir los acordes sin pausa entre ellos
        print('Progresión completa. Repitiendo...\n')

except KeyboardInterrupt:
    print('Reproducción interrumpida por el usuario.')
