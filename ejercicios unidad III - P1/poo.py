class Persona:
  def __init__(self, nom, apell):
     self.nombre = nom
     self.apellido = apell

  def mostrar(self):
    print("Nombre ", self.nombre)

class Alumno(Persona): 
  def __init__(self, nom, apellido, nota1, nota2, nota3):
    super().__init__(nom, apellido)
    self.nota1 = nota1
    self.nota2 = nota2
    self.nota3 = nota3

  def nota_final(self):
    return (self.nota1 + self.nota2 + self.nota3) / 3
  
  def mostrar_nota_final(self):
    print(self.nombre+ " " + self.apellido + " su nota final es: ", self.nota_final())

def main():
  alumno1 = Alumno("Abner", "Saavedra", 18, 19, 20)
  alumno2 = Alumno("Pepito", "Pérez", 17, 16, 20)

  alumno1.mostrar_nota_final()
  alumno2.mostrar_nota_final()

if __name__ == "__main__":
  main()