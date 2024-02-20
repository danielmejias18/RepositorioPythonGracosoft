pasajeros = []

def agregar_pasajeros():
    resp = int(input("¿Desea agregar nuevos pasajeros? (1) Si o (2) No: "))
    while resp != 2:  
        nombre = input("Ingrese el nombre del pasajero: ")
        cedula = input("Ingrese el número de cédula: ")
        ciudad_destino = input("Ingrese la ciudad de destino: ")
        pais_destino = input("Ingrese el país de destino: ")
        tupla_pasajeros = (nombre, cedula, ciudad_destino, pais_destino)
        pasajeros.append(tupla_pasajeros)
        resp = int(input("¿Desea agregar nuevos pasajeros? (1) Si o (2) No: "))
    print(pasajeros)                               

def buscar_cedula_ciudad(lista):
    for n in range(0, len(lista)):
        ced = input("Ingrese la cédula del pasajero a buscar: ")
        if lista[n][1] == ced:
            print(lista[n][2])

def ciudad_cant_pasajeros(lista):
    cantpasajeros = 0
    ciud = input("Ingrese la ciudad a buscar: ")
    for n in range(0, len(lista)):
        if lista[n][2] == ciud:
            cantpasajeros = cantpasajeros + 1
    print(cantpasajeros)

def buscar_cedula_pais(lista):
    for n in range(0, len(lista)):
        ced = input("Ingrese la cédula del pasajero a buscar: ") 
        if lista[n][1] == ced:
            print(lista[n][3])

def pais_cant_pasajeros(lista):
    cantpasajeros = 0
    pais = input("Ingrese el país a buscar: ")
    for n in range(0, len(lista)):
        if lista[n][3] == pais:
            cantpasajeros = cantpasajeros + 1
    print(cantpasajeros)

def contarPasajeros(lista):
    listaContadores = []
    contPasajeros = 0
    for n in range(0, len(lista)):
        pais = lista[n][3]
        for m in range(0, len(lista)):  
            if pais == lista[m][3]:
                contPasajeros = contPasajeros + 1
        paisContPasajeros = [pais, contPasajeros]
        listaContadores.append(paisContPasajeros)
        contPasajeros = 0
    return listaContadores

def definir_menor(lista):
    menor = lista[0]
    for n in range(0, len(lista)):
        valorLista = lista[n]
        if valorLista[1] <= menor[1]:
            menor = lista[n]
    return menor

def definir_mayor(lista):
    mayor = lista[0]
    for n in range(0, len(lista)):
        if lista[n][1] >= mayor[1]:
            mayor = lista[n]
    return mayor

def menu_principal():
    listaContadores = contarPasajeros(pasajeros)
    resp = input("1- Continuar o 2- Salir: ")
    while resp != "2":
        print("1. Agregar pasajeros a la lista de viajeros")
        print("2. Dado la cédula de un pasajero, ver a qué ciudad viaja.")
        print("3. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad")
        print("4. Dado la cédula de un pasajero, ver a qué país viaja")
        print("5. Dado un país, mostrar la cantidad de pasajeros que viajan a ese país")
        print("6. El país con la menor cantidad de pasajeros")
        print("7. El país con la mayor cantidad de pasajeros")
        resp2 = input("Seleccione una opción: ")
        if resp2 == "1":
            agregar_pasajeros()
        elif resp2 == "2":
            buscar_cedula_ciudad(pasajeros)
        elif resp2 == "3":
            ciudad_cant_pasajeros(pasajeros)
        elif resp2 == "4":
            buscar_cedula_pais(pasajeros)
        elif resp2 == "5":
            pais_cant_pasajeros(pasajeros)
        elif resp2 == "6":
            print(definir_menor(listaContadores))
        elif resp2 == "7":
            print(definir_mayor(listaContadores))
        resp = input("1- Continuar o 2- Salir: ")

def main():
    menu_principal()

if __name__ == "__main__":
    main()