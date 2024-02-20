lista_de_notas = []
suma = 0.0
promedio = 0.0
mayorNota = -1
menorNota = 21

for n in range(1, 6):
    lista_de_notas.append(int(input("Ingrese la nota: ")))

for n in range(1, 6):
    suma = suma + lista_de_notas[n-1]
    promedio = suma / len(lista_de_notas)
    if (lista_de_notas[n-1] > mayorNota):
        mayorNota= lista_de_notas[n-1]
    if (menorNota > lista_de_notas[n-1]):
        menorNota= lista_de_notas[n-1]
    print(lista_de_notas[n-1])
print(lista_de_notas[n-1], "Nota promedio: ", promedio, "Mayor nota: ", mayorNota, "Menor nota: ", menorNota)

def promedioDeNotas(lista_de_notas):
 for n in range(1, 6):
  suma = suma + lista_de_notas[n-1]
 promedio = suma / len(lista_de_notas)
 return promedio

def mayorNota(lista_de_notas):
 for n in range(1, 6):
  if (lista_de_notas[n-1]  > mayorNota):
   mayorNota= lista_de_notas[n-1]
   return mayorNota
 
def menorNota(lista_de_notas):
  for n in range(1, 6):
   if (lista_de_notas[n-1] < menorNota):
    menorNota= lista_de_notas[n-1]
    return menorNota
   