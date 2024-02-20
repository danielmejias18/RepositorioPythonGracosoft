notas = []

for n in range (1, 6):
    nota = float(input("Introduzca una nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
mayornota = max(notas)
menornota = min(notas)
print("La media es : ", media)
print("Menornota : ", menornota)
print("Mayornota : ", mayornota)



