import re

# Nombre del archivo de texto que contiene los acordes y la letra
file_name = 'song.txt'

try:
    # Abrir el archivo en modo de lectura ('r')
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        chords = []
        lyrics = []
        all_acordes = []

        for line in lines:
            # Verificar si la línea contiene acordes usando una expresión regular
            pattern = re.findall(r'\b[A-G][#b]?(m|7|maj7|sus2|sus4|aug|dim)?\b', line)
            
            if pattern:
                # Almacenar los acordes y su posición en la línea (index)
                line_info = []
                chord_positions = [(match.start(), match.group()) for match in re.finditer(r'\b[A-G][#b]?(m|7|maj7|sus2|sus4|aug|dim)?\b', line)]
                
                for position, chord in chord_positions:
                    line_info.append((position, chord))
                chords.append(line_info)
                
                # También almacenar la línea con letra y acordes
                lyrics.append(line.strip())
            else:
                # Si no hay acordes, solo es letra
                lyrics.append(line.strip())
        
        # Calcular la posición máxima de los acordes
        max_chord = 0
        for chord_line in chords:
            for position, _ in chord_line:
                if position > max_chord:
                    max_chord = position

        # Imprimir los resultados y calcular los tiempos
        print("Calculated chord times:")
        for chord_line in chords:
            current_time = 0.0
            previous_position = 0
            
            for position, chord in chord_line:
                # Calcular la diferencia en espacios desde la última posición
                space_count = position - previous_position
                # Calcular el tiempo adicional basado en los espacios (0.1 por espacio)
                time_increment = space_count * 0.1
                current_time += time_increment
                # Redondear el tiempo a una cifra decimal
                current_time = round(current_time, 1)
                # Imprimir el acorde con su tiempo calculado, agregando la coma al final
                print(f"({current_time}, [(['{chord}'], 'C4')]),")
                # Actualizar la posición anterior para el siguiente cálculo
                previous_position = position

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. Make sure the file name and path are correct.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
