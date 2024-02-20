nombre = input("Ingrese nombre: ")
edad = input("Ingrese edad: ")
direccion = input("Ingrese dirección: ")
telefono = input("Ingrese telefono: ")

datos_usuario = { "nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono }

print(datos_usuario["nombre"] + " tiene " + datos_usuario["edad"] + " años de edad, vive en " + datos_usuario["direccion"] + " y su telefono es "+ datos_usuario["telefono"])