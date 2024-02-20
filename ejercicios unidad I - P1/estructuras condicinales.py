#Condicional simple

#edad = int(input("¿Cuántos años tienes? "))

#if edad>=18:
 #print("Eres mayor de edad")

 #Condicinal multiple

nombre1 = input("Ingrese nombre persona 1: ")
nombre2 = input("Ingrese nombre persona 2: ")
 
if (nombre1[0].upper == nombre2[0].upper) or (nombre1[len(nombre1)-1].upper == nombre2[len(nombre2)-1].upper):
 print("Coincidencia")
else:
 print("No hay coincidencia")