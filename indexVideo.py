import os
from moviepy.video.io.VideoFileClip import VideoFileClip

# Configuración
video_path = '1997_eljuego.mp4'  # Ruta del video original
output_folder = 'segmentos'  # Carpeta donde guardar los segmentos

# Asegúrate de que la carpeta de salida existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Leer el archivo de video
video = VideoFileClip(video_path)

# Duración total del video en segundos
duracion_total = video.duration

# Duración de cada segmento (3 minutos = 180 segundos)
duracion_segmento = 180
n_segmento = 1

# Cortar el video en segmentos
for inicio in range(0, int(duracion_total), duracion_segmento):
    final = min(inicio + duracion_segmento, duracion_total)
    clip = video.subclip(inicio, final)
    
    # Guardar cada segmento en la carpeta de salida
    output_path = os.path.join(output_folder, f'segmento_{n_segmento}.mp4')
    clip.write_videofile(output_path, codec='libx264')
    
    print(f'Segmento {n_segmento} guardado como {output_path}')
    n_segmento += 1

# Cerrar el video original para liberar recursos
video.close()

print("Video dividido en segmentos exitosamente.")



