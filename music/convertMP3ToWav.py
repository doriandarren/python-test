import os
from pydub import AudioSegment

# Ruta base donde están las carpetas de los archivos MP3
ruta_base_mp3 = 'Piano'

# Ruta base para la nueva carpeta con archivos WAV
ruta_base_wav = 'PianoWav'

# Crear la carpeta base para los archivos WAV si no existe
if not os.path.exists(ruta_base_wav):
    os.makedirs(ruta_base_wav)

# Recorrer las octavas de C1 a C7
for octava in range(1, 8):
    nombre_carpeta = f'C{octava}'
    ruta_carpeta_mp3 = os.path.join(ruta_base_mp3, nombre_carpeta)
    ruta_carpeta_wav = os.path.join(ruta_base_wav, nombre_carpeta)

    # Imprimir las rutas para depuración
    print(f'Buscando en: {ruta_carpeta_mp3}')
    
    # Crear la carpeta para la octava en la carpeta WAV
    if not os.path.exists(ruta_carpeta_wav):
        os.makedirs(ruta_carpeta_wav)

    # Notas disponibles en cada octava
    notas = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    # Convertir cada archivo MP3 a WAV
    for nota in notas:
        archivo_mp3 = os.path.join(ruta_carpeta_mp3, f'{nota}.mp3')
        archivo_wav = os.path.join(ruta_carpeta_wav, f'{nota}.wav')

        if os.path.exists(archivo_mp3):
            # Cargar el archivo MP3 y convertirlo a WAV
            sonido = AudioSegment.from_mp3(archivo_mp3)
            sonido.export(archivo_wav, format='wav')
            print(f'Convertido: {archivo_mp3} a {archivo_wav}')
        else:
            print(f'Archivo MP3 no encontrado: {archivo_mp3}')
