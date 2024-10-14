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

# Array que contiene el ritmo con notas y octavas específicas
ritmo_acordes = [
    (0.1, ['A', 'C', 'E'], 'C4'),   # Am en la octava C4
    (0.2, "Pausa", None),           # Pausa de 0.2 segundos
    (0.3, ['C', 'E', 'G'], 'C5'),   # C en la octava C5
    (0.3, "Pausa", None),           # Pausa de 0.3 segundos
    (1, ['G', 'B', 'D'], 'C6'),     # G en la octava C6
    (0.9, "Pausa", None),           # Pausa de 0.9 segundos
    (0.4, ['D', 'F', 'A'], 'C4')    # Dm en la octava C4
]

# Verificar que hay sonidos disponibles
if not archivos_mp3:
    print('No se encontraron archivos de sonido para las octavas especificadas.')
    exit(1)

# Función para reproducir los acordes durante el tiempo especificado
def reproducir_acorde(acorde, duracion, octava):
    if acorde == "Pausa":
        # Si es una pausa, solo esperamos el tiempo de la pausa
        print(f'Pausa de {duracion} segundos')
        time.sleep(duracion)
    else:
        # Usamos la octava que viene en el array
        if octava is None:
            octava = 'C4'  # Valor por defecto si no se especifica octava

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
        for duracion, acorde, octava in ritmo_acordes:
            reproducir_acorde(acorde, duracion, octava)
        print('Progresión completa. Repitiendo...\n')

except KeyboardInterrupt:
    print('Reproducción interrumpida por el usuario.')
