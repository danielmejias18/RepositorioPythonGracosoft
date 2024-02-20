#PASO 1: Abrir el archivo en modo lectura

archivo = open("archivo.txt", "r")

#PASO 2: Obtener o leer el contenido del archivo

for linea in archivo:
    print(linea)


#PASO 3: Cerrar el archivo
    
archivo.close()