def app():
    #crear archivo
    archivo = open('archivo.txt', 'w') # permiso escritura

    for i in range(0, 20):
        archivo.write('Esta es una linea' + str(i) + "\r\n")

    archivo.close()



app()