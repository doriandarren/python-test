import os
import time
from pydub import AudioSegment
import simpleaudio as sa
from time import time as cronometro  # Usamos 'cronometro' para medir el tiempo

# Función para obtener los archivos WAV
def obtener_archivos_wav(ruta_base):
    archivos_wav = {}
    for octava in range(1, 8):  # De C1 a C7 para cubrir más octavas
        nombre_carpeta = f'C{octava}'
        ruta_carpeta = os.path.join(ruta_base, nombre_carpeta)
        if os.path.isdir(ruta_carpeta):
            archivos_wav[nombre_carpeta] = {}
            notas = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
            for nota in notas:
                nombre_archivo = os.path.join(ruta_carpeta, f'{nota}.wav')
                if os.path.isfile(nombre_archivo):
                    archivos_wav[nombre_carpeta][nota] = nombre_archivo
                else:
                    print(f'No se encontró el archivo: {nombre_archivo}')
        else:
            print(f'No se encontró la carpeta: {ruta_carpeta}')
    return archivos_wav

# Ruta base donde están las carpetas de las notas WAV
ruta_base_wav = 'Piano'  # Asegúrate de que esta es la ruta correcta
archivos_wav = obtener_archivos_wav(ruta_base_wav)

# Definir el array de ritmo de acordes, cada entrada puede tener múltiples acordes
ritmo_acordes = [
    (0.0, [(['Dm'], 'C4')]),
    (0.3, [(['F'], 'C4')]),
    (1.4, [(['Am'], 'C4')]),
    (0.9, [(['G'], 'C4')]),
    (2.4, [(['Dm'], 'C4')]),
    (0.0, [(['F'], 'C4')]),
    (1.7, [(['Am'], 'C4')]),
    (2.2, [(['G'], 'C4')]),
    (0.0, [(['Dm'], 'C4')]),
    (1.0, [(['F'], 'C4')]),
    (1.3, [(['Am'], 'C4')]),
    (2.4, [(['G'], 'C4')]),
    (0.4, [(['Dm'], 'C4')]),
    (1.7, [(['F'], 'C4')]),
    (2.8, [(['Am'], 'C4')]),
    (4.0, [(['G'], 'C4')]),
    (1.6, [(['Dm'], 'C4')]),
    (2.2, [(['F'], 'C4')]),
    (0.0, [(['C'], 'C4')]),
    (3.0, [(['Dm'], 'C4')]),
    (0.0, [(['F'], 'C4')]),
    (1.0, [(['Am'], 'C4')]),
    (4.0, [(['Dm'], 'C4')]),
    (4.7, [(['F'], 'C4')]),
    (1.3, [(['Am'], 'C4')]),
    (2.4, [(['G'], 'C4')]),
    (4.1, [(['Dm'], 'C4')]),
    (0.3, [(['F'], 'C4')]),
    (1.4, [(['Am'], 'C4')]),
    (2.1, [(['G'], 'C4')]),
    (1.6, [(['Dm'], 'C4')]),
    (2.2, [(['F'], 'C4')]),
    (0.0, [(['C'], 'C4')]),
    (3.0, [(['Dm'], 'C4')]),
    (0.0, [(['F'], 'C4')]),
    (1.0, [(['Am'], 'C4')]),
    (4.0, [(['Dm'], 'C4')]),
    (4.7, [(['F'], 'C4')]),
    (1.3, [(['Am'], 'C4')]),
    (2.4, [(['G'], 'C4')]),
    (4.1, [(['Dm'], 'C4')]),
    (0.3, [(['F'], 'C4')]),
    (1.4, [(['Am'], 'C4')]),
    (2.2, [(['G'], 'C4')]),
    (0.0, [(['G'], 'C4')]),
    (1.7, [(['F'], 'C4')]),
    (0.6, [(['G'], 'C4')]),
    (0.0, [(['C'], 'C4')]),
    (0.0, [(['F'], 'C4')]),
    (1.7, [(['C'], 'C4')]),
    (0.4, [(['Dm'], 'C4')]),
    (1.3, [(['F'], 'C4')]),
    (0.9, [(['Am'], 'C4')]),
    (1.9, [(['G'], 'C4')]),
    (0.5, [(['Dm'], 'C4')]),
    (2.6, [(['F'], 'C4')]),
    (0.3, [(['Am'], 'C4')]),
    (1.3, [(['G'], 'C4')]),
    (1.3, [(['Dm'], 'C4')]),
    (0.0, [(['C'], 'C4')]),
    (0.6, [(['Dm'], 'C4')]),
    (1.3, [(['Em'], 'C4')]),
    (3.3, [(['F'], 'C4')]),
    (0.0, [(['Am'], 'C4')]),
    (0.5, [(['Dm'], 'C4')]),
    (2.0, [(['F'], 'C4')]),
    (3.8, [(['Am'], 'C4')]),
    (0.9, [(['G'], 'C4')]),
    (0.0, [(['Dm'], 'C4')]),
    (1.7, [(['F'], 'C4')]),
    (0.3, [(['Am'], 'C4')]),
    (2.7, [(['Em'], 'C4')]),
    (1.6, [(['Dm'], 'C4')]),
    (2.2, [(['F'], 'C4')]),
    (0.0, [(['C'], 'C4')]),
    (3.0, [(['Dm'], 'C4')]),
    (0.0, [(['F'], 'C4')]),
    (1.0, [(['Am'], 'C4')]),
    (4.0, [(['Dm'], 'C4')]),
    (4.7, [(['F'], 'C4')]),
    (1.3, [(['Am'], 'C4')]),
    (2.4, [(['G'], 'C4')]),
    (4.1, [(['Dm'], 'C4')]),
    (0.3, [(['F'], 'C4')]),
    (1.4, [(['Am'], 'C4')]),
    (2.1, [(['G'], 'C4')]),
    (1.6, [(['Dm'], 'C4')]),
    (2.2, [(['F'], 'C4')]),
    (0.0, [(['C'], 'C4')]),
    (3.0, [(['Dm'], 'C4')]),
    (0.0, [(['F'], 'C4')]),
    (1.0, [(['Am'], 'C4')]),
    (4.0, [(['Dm'], 'C4')]),
    (4.7, [(['F'], 'C4')]),
    (1.3, [(['Am'], 'C4')]),
    (2.4, [(['G'], 'C4')]),
    (4.1, [(['Dm'], 'C4')]),
    (0.3, [(['F'], 'C4')]),
    (1.4, [(['Am'], 'C4')]),
    (2.2, [(['G'], 'C4')]),
    (1.1, [(['Dm'], 'C4')]),
    (3.9, [(['F'], 'C4')]),
    (1.1, [(['Am'], 'C4')]),
    (4.2, [(['G'], 'C4')]),
    (0.7, [(['Dm'], 'C4')]),
    (3.5, [(['F'], 'C4')]),
    (2.5, [(['Am'], 'C4')]),
    (4.6, [(['G'], 'C4')]),
    (0.8, [(['Dm'], 'C4')]),
    (1.7, [(['F'], 'C4')]),
    (0.0, [(['Am'], 'C4')]),
    (1.2, [(['G'], 'C4')]),
    (0.0, [(['Dm'], 'C4')]),
    (2.1, [(['F'], 'C4')]),
    (0.0, [(['Am'], 'C4')]),
    (1.5, [(['G'], 'C4')]),
    (0.7, [(['G'], 'C4')]),
    (0.0, [(['F'], 'C4')]),
    (0.7, [(['Am'], 'C4')]),
    (0.2, [(['G'], 'C4')]),
    (0.2, [(['Dm'], 'C4')]),
    (0.0, [(['F'], 'C4')]),
    (1.1, [(['Am'], 'C4')]),
    (0.2, [(['G'], 'C4')]),
    (0.0, [(['F'], 'C4')]),
    (1.5, [(['C'], 'C4')]),
]

# Función para reproducir un conjunto de acordes (múltiples acordes) usando pydub y simpleaudio
def reproducir_acordes_conjuntos(acordes, inicio):
    # Cronometrar y mostrar el tiempo actual de reproducción
    tiempo_actual = cronometro() - inicio
    print(f'Tiempo: {tiempo_actual:.2f}s - Reproduciendo {len(acordes)} acorde(s)')

    sonidos = []
    # Reproducir todos los acordes simultáneamente
    for acorde, octava in acordes:
        print(f'Acorde: {acorde} en la octava {octava}')
        for nota in acorde:
            if nota in archivos_wav[octava]:
                # Cargar el archivo WAV
                audio = AudioSegment.from_wav(archivos_wav[octava][nota])
                sonido = sa.play_buffer(audio.raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)
                sonidos.append(sonido)

# Función para manejar la línea de tiempo que siempre se ejecute
def linea_de_tiempo(ritmo_acordes):
    inicio = cronometro()  # Iniciar el cronómetro
    while True:  # Bucle infinito
        for duracion, acordes in ritmo_acordes:
            reproducir_acordes_conjuntos(acordes, inicio)
            time.sleep(duracion)  # Esperar el tiempo indicado antes de reproducir el siguiente conjunto de acordes

# Iniciar la línea de tiempo
try:
    linea_de_tiempo(ritmo_acordes)

except KeyboardInterrupt:
    print('Reproducción interrumpida por el usuario.')
