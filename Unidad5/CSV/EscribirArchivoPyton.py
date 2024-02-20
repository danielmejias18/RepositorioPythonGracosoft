#Abrimos el archivo de texto plano en modo escritura (w)

archivo = open("archivo.txt", "w")


#Escribimos una linea en el archivo

#archivo.write("Hola mundooooo\n")

archivo.writelines(["linea 1\n", "linea 2\n", "linea 3\n", "linea 4\n", "linea 5\n"])


#Cerramos el archivo
archivo.close()