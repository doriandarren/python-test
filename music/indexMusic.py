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

# Array que contiene el ritmo con pausas y acordes
ritmo_acordes = [
    (0.1, ['A', 'C', 'E']),   # 0.1 segundos - Am
    (0.2, "Pausa"),           # 0.2 segundos de pausa
    (0.3, ['C', 'E', 'G']),   # 0.3 segundos - C
    (0.3, "Pausa"),           # 0.3 segundos de pausa
    (1, ['G', 'B', 'D']),     # 1 segundo - G
    (0.9, "Pausa"),           # 0.9 segundos de pausa
    (0.4, ['D', 'F', 'A'])    # 0.4 segundos - Dm
]

# ritmo_acordes = [
#     (0.7, ['D', 'F', 'A']),   # 0.7 segundos - Dm
#     (0.9, ['A', 'C', 'E']),   # 0.9 segundos - Am
#     (0.8, ['E', 'G#', 'B']),  # 0.8 segundos - E
#     (0.6, ['F', 'A', 'C']),   # 0.6 segundos - F
#     (0.5, ['C', 'E', 'G'])    # 0.5 segundos - C
# ]



# Lista de octavas a reproducir (C4 a C7)
octavas_a_reproducir = ['C4', 'C5', 'C6', 'C7']

# Verificar que hay sonidos disponibles
if not archivos_mp3:
    print('No se encontraron archivos de sonido para las octavas especificadas.')
    exit(1)

# Función para reproducir los acordes durante el tiempo especificado
def reproducir_acorde(acorde, duracion):
    if acorde == "Pausa":
        # Si es una pausa, solo esperamos el tiempo de la pausa
        print(f'Pausa de {duracion} segundos')
        time.sleep(duracion)
    else:
        # Elegir una octava aleatoria
        octava = 'C4'  # Puedes cambiarlo a cualquier octava

        notas_a_reproducir = []
        for nota in acorde:
            if nota in archivos_mp3[octava]:
                notas_a_reproducir.append(archivos_mp3[octava][nota])

        if len(notas_a_reproducir) >= 1:  # Asegurarse de que hay notas para reproducir
            audio = AudioSegment.from_mp3(notas_a_reproducir[0])

            # Convertir los sonidos a simpleaudio para reproducirlos
            audio = sa.play_buffer(audio.raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)

            print(f'Reproduciendo acorde: {acorde} durante {duracion} segundos en la octava {octava}')

            # Esperar la duración especificada para este acorde
            time.sleep(duracion)

# Reproducción continua según el array de ritmo y acordes
try:
    while True:
        for duracion, acorde in ritmo_acordes:
            reproducir_acorde(acorde, duracion)
        print('Progresión completa. Repitiendo...\n')

except KeyboardInterrupt:
    print('Reproducción interrumpida por el usuario.')
