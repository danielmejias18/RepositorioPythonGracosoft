def contar_caracteres(cadena):
    contador = {}
    for caracter in cadena:
        if caracter in contador:
            contador[caracter] += 1
        else:
            contador[caracter] = 1
    return contador

cadena = input("Ingresa la cadena a analizar: ")
contador = contar_caracteres(cadena)
print(contador)

    



