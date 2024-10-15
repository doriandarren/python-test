import os
import time
import pygame

# Inicializar pygame y su mezclador
pygame.mixer.init()

# Función para obtener los archivos MP3
def obtener_archivos_mp3(ruta_base):
    archivos_mp3 = {}
    for octava in range(1, 8):  # De C1 a C7 para cubrir más octavas
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
    (0.9, ['C', 'E', 'G'], 'C4'),   # C mayor en la octava C2
    (1.2, ['G', 'B', 'D'], 'C4'),  # G menor en la octava C2
    (0.9, ['F', 'A', 'C'], 'C4'),   # F mayor en la octava C2
    (1.2, ['A', 'C', 'E'], 'C4'),   # A menor en la octava C2
]

# Mano derecha (melodía, acordes en octavas agudas)
ritmo_acordes_derecha = [
    (0.9, ['C', 'E', 'G'], 'C5'),   # C mayor en la octava C4
    (1.2, ['G', 'B', 'D'], 'C6'),  # G menor en la octava C4
    (0.9, ['F', 'A', 'C'], 'C5'),   # F mayor en la octava C4
    (1.2, ['A', 'C', 'E'], 'C6'),   # A menor en la octava C4
]



# Función para reproducir un acorde o una pausa con depuración
def reproducir_acorde(acorde, duracion, octava, canal, mano):
    if acorde == "Pausa":
        print(f'{mano} - Pausa de {duracion} segundos')
        time.sleep(duracion)
    else:
        if octava not in archivos_mp3:
            print(f"Error: La octava {octava} no se encuentra en el diccionario archivos_mp3.")
            return  # Salimos de la función si la octava no existe

        notas_a_reproducir = []
        for nota in acorde:
            if nota in archivos_mp3[octava]:
                notas_a_reproducir.append(archivos_mp3[octava][nota])
            else:
                print(f"Error: La nota {nota} no se encuentra en la octava {octava}.")

        if len(notas_a_reproducir) >= 1:
            print(f'{mano} - Reproduciendo acorde: {acorde} en la octava {octava}')
            sonido = pygame.mixer.Sound(notas_a_reproducir[0])
            canal.play(sonido)
            time.sleep(duracion)



# Función para reproducir los acordes de ambas manos simultáneamente
def reproducir_dos_manos(ritmo_izquierda, ritmo_derecha):
    canal_izq = pygame.mixer.Channel(0)  # Canal para la mano izquierda
    canal_der = pygame.mixer.Channel(1)  # Canal para la mano derecha

    for i in range(min(len(ritmo_izquierda), len(ritmo_derecha))):
        duracion_izq, acorde_izq, octava_izq = ritmo_izquierda[i]
        duracion_der, acorde_der, octava_der = ritmo_derecha[i]

        # Reproducir ambos acordes simultáneamente en diferentes canales
        reproducir_acorde(acorde_izq, duracion_izq, octava_izq, canal_izq, "Mano Izquierda")
        reproducir_acorde(acorde_der, duracion_der, octava_der, canal_der, "Mano Derecha")

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
