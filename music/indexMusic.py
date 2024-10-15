import os
import time
import threading
from pydub import AudioSegment
import simpleaudio as sa

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

# Mano izquierda (bajos)
ritmo_acordes_izquierda = [
    (0.4, ['C', 'E', 'G'], 'C4'),   # C mayor en la octava C2
    (0.4, ['G', 'A#', 'D'], 'C4'),  # G menor en la octava C2
    (0.4, ['F', 'A', 'C'], 'C4'),   # F mayor en la octava C2
    (0.4, ['A', 'C', 'E'], 'C4'),   # A menor en la octava C2
]

# Mano derecha (melodía)
ritmo_acordes_derecha = [
    (0.4, ['C', 'E', 'G'], 'C6'),   # C mayor en la octava C4
    (0.4, ['G', 'A#', 'D'], 'C6'),  # G menor en la octava C4
    (0.4, ['F', 'A', 'C'], 'C5'),   # F mayor en la octava C4
    (0.4, ['A', 'C', 'E'], 'C6'),   # A menor en la octava C4
]

# Función para reproducir un acorde o una pausa usando pydub y simpleaudio
def reproducir_acorde(acorde, duracion, octava, mano):
    if acorde == "Pausa":
        print(f'{mano} - Pausa de {duracion} segundos')
        time.sleep(duracion)
    else:
        # Verificar si la octava está presente en el diccionario
        if octava not in archivos_wav:
            print(f"Error: La octava '{octava}' no se encuentra en el diccionario archivos_wav. Mano: {mano}")
            return  # Salimos de la función si la octava no existe

        # Reproducir cada nota del acorde en paralelo
        sonidos = []
        print(f'{mano} - Reproduciendo acorde: {acorde} en la octava {octava}')
        for nota in acorde:
            if nota in archivos_wav[octava]:
                # Cargar el archivo WAV
                audio = AudioSegment.from_wav(archivos_wav[octava][nota])
                sonido = sa.play_buffer(audio.raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)
                sonidos.append(sonido)

        # Esperar por la duración especificada, pero dejar que el sonido se siga reproduciendo
        time.sleep(duracion)

# Función para reproducir los acordes de ambas manos simultáneamente
def reproducir_dos_manos(ritmo_izquierda, ritmo_derecha):
    for i in range(min(len(ritmo_izquierda), len(ritmo_derecha))):
        duracion_izq, acorde_izq, octava_izq = ritmo_izquierda[i]
        duracion_der, acorde_der, octava_der = ritmo_derecha[i]

        # Reproducir ambos acordes simultáneamente usando hilos
        hilo_izq = threading.Thread(target=reproducir_acorde, args=(acorde_izq, duracion_izq, octava_izq, "Mano Izquierda"))
        hilo_der = threading.Thread(target=reproducir_acorde, args=(acorde_der, duracion_der, octava_der, "Mano Derecha"))
        
        # Iniciar ambos hilos
        hilo_izq.start()
        hilo_der.start()
        
        # Esperar a que ambos hilos terminen
        hilo_izq.join()
        hilo_der.join()

        # No hacer sleep demasiado tiempo; esto es solo para avanzar al siguiente acorde
        time.sleep(0.05)  # Duración mínima entre acordes, ajustable

# Iniciar las dos manos en paralelo
try:
    while True:
        reproducir_dos_manos(ritmo_acordes_izquierda, ritmo_acordes_derecha)

except KeyboardInterrupt:
    print('Reproducción interrumpida por el usuario.')
