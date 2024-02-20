class Persona:
    def __init__(self, nom, apell):
        self.nombre = nom
        self.apellido = apell
    
    def mostrar(self):
        print("Nombre: ", self.nombre)

class Alumno(Persona):
    def __init__(self,nom, apell, nota1, nota2, nota3):
        super().__init__(nom, apell)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def notafinal(self):
        notafinal = (self.nota1 + self.nota2 + self.nota3)/3
        return notafinal
    def mostrar_notafinal(self):
        print("Notafinal: ", self.notafinal)


def main():
    alumno1 = Alumno( "Juan", "Perez", 8, 9, 5)
    alumno2 = Alumno("Pedro", "Perez", 7, 8, 5 )
    print("la nota final del alumno" , alumno1.nombre, " es :" , alumno1.notafinal())
    print(alumno2.notafinal())

main()