cadena = input("Ingrese una cadena: ")

diccionario = {}

for n in range(0, len(cadena)):
    aparicion = 0
    valor = cadena[n]
    for m in range(0, len(cadena)):
        if(valor == cadena[m]):
            aparicion = aparicion + 1
        diccionario[valor] = aparicion

print(diccionario)