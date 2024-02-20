class Persona:
    def __init__(self, nom, edad, ced):
        self.nombre = nom
        self.edad = edad
        self.cedula = ced

    def mostrar_datos_persona(self):
        print("Los datos de la persona son: ", self.nombre, self.edad, self.cedula)

    def es_mayor_de_edad(self):
        if(self.edad >= 18):
           return True
        else:
            return False
        
persona = Persona("Abner", 17, 20000000000)
persona.mostrar_datos_persona()
print(persona.es_mayor_de_edad())