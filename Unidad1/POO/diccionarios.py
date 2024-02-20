nombre = input("Ingrese su nombre: ")
edad = (input("Ingrese su edad: "))
direccion = input("Ingrese su direccion: ")
telefono = input("Ingrese su telefono: ")
datos_usuario = {"nombre": nombre , "edad": edad , "direccion": direccion, "telefono": telefono}
print(datos_usuario["nombre"]+ " tiene:" + datos_usuario["edad"] + " años de edad, vive en : "+ datos_usuario["direccion"] + " y su numero de teléfono es: " + datos_usuario["telefono"] )