"""
contrasenia = "Contraseña"
contraseniaInput = input("Intrduzca la contraseña correcta: ")
while(contrasenia != contraseniaInput):
    contraseniaInput = input("Intrduzca la contraseña correcta: ")
print("Contraseñas iguales:", contrasenia, contraseniaInput)
"""

numero = int(input("Introduzca un número entero: "))
for n in range(1, numero+1):
    print("*"*n)