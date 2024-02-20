def ingresar_asignaturas():
    
  
    asignaturas = []
    
    print("Introduce las asignaturas del curso (escribe 'fin' para terminar):")
    while True:
        asignatura = input("Asignatura: ")
        if asignatura.lower() == 'fin':
            break
        asignaturas.append(asignatura)
    return asignaturas

def preguntar_notas(asignaturas):
  
    asignaturas_pendientes = []
    for asignatura in asignaturas:
        nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
        if nota < 10.0: 
            asignaturas_pendientes.append(asignatura)
    return asignaturas_pendientes

def mostrar_asignaturas_pendientes(asignaturas_pendientes):
    
    if asignaturas_pendientes:
        print("Tienes que repetir las siguientes asignaturas:")
        for asignatura in asignaturas_pendientes:
            print(asignatura)
    else:
        print("¡Felicidades! Has aprobado todas las asignaturas.")

def main():
    asignaturas = ingresar_asignaturas()
    asignaturas_pendientes = preguntar_notas(asignaturas)
    mostrar_asignaturas_pendientes(asignaturas_pendientes)

main()