class Alumno :
    def __init__(self,  cedula, asistencia, nota):
        self.cedula = cedula
        self.asistencia = asistencia
        self.nota = nota

class Parcial :
    def __init__(self, totalAlumnos, totalAusentes, totalNotas):
        self.totalAlumnos = totalAlumnos
        self.totalAusentes = totalAusentes
        self.totalNotas = totalNotas
    def calcular_porcentaje_alumnos_ausentes(self):
    
        porcAusentes = 0.0
       
          
        else: 
            contTotal+=1
            contTotal = contTotal+contAusentes
            porcAusentes = (contAusentes/contTotal) * 100
            return porcAusentes
        

    def calcular_nota_parcial(self, nota):
        sumanotas = 0
        sumanotas =  sumanotas + nota 

alumnos = [] 
resp = input("Ingrese datos alumno :  SI: 1, NO: 2 ")
while (resp!= "2"):
    cedula = input("Ingrese cedula del alumno : ")
    asistencia = input("Ingrese asistencia del alumno : ")
    nota = input("Ingrese nota del alumno : ")
    alumno = Alumno(cedula, asistencia, nota)
    alumnos.append(alumno)
    resp = int(input("Ingrese datos del alumno :SI")) 

print("porcentaje de almunos ausentes : ", alumnos[0].calcular_porcentaje)