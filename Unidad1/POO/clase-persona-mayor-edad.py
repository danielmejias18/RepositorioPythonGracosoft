class persona:
    def __init__(self, nom, edad, ced):
        self.nombre = nom
        self.edad = edad
        self.cedula = ced
    def mostrar(self):
        print("los datos de la persona son " + self.nombre + " " , self.edad , " " , self.cedula)
    
    def esmayoredad(self):
        if (self.edad >= 18):
            return "Es mayor de edad"
        else:
            return "No es mayor de edad"
persona = persona("Juan", 17, 2000000)
persona.mostrar()
print(persona.esmayoredad())
