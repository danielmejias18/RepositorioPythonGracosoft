
asignaturas = [["matematicas", 0], ["fisica", 0], ["quimica",0], ["historia",0]]



for n in range (0, len(asignaturas)): 

    nota = float(input("Introduce la nota de "+ asignaturas[n][0]+ ": "))
    if nota > 10:
        asignaturas[n] [0,1].remove()
    else:
       asignaturas[n][1]= nota
print("Las asignaturas que debes repetir son:, ", [asignaturas])