class cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar_datos_cuenta(self):
        print("los datos de la cuenta son " + self.titular + " ", self.cantidad)
    def ingresarCantidad(self, cant):
        cant = float(input("Ingrese la cantidad a ingresar: "))
        self.cantidad =self.cantidad+ cant
    def retirarCantidad(self, cant):
        cant= float(input("Ingrese la cantidad a retirar: "))
        self.cantidad = self.cantidad-cant

def main():
    dinero = 1000
    cuenta1 = cuenta("Juan", dinero)
    cuenta1.mostrar_datos_cuenta()
    cuenta1.ingresarCantidad(cuenta1.cantidad)
    cuenta1.mostrar_datos_cuenta()
    cuenta1.retirarCantidad(cuenta1.cantidad)
    cuenta1.mostrar_datos_cuenta()

main()
