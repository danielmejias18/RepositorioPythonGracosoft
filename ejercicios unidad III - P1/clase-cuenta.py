class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar_datos_cuenta(self):
        print("Los datos de la cuenta son: ", self.titular, self.cantidad)

    def ingresar_cantidad(self, cant):
        if(cant > 0):
            self.cantidad = self.cantidad + cant
    
    def retirar_cantidad(self, cant):
        if(cant <= self.cantidad):
            self.cantidad = self.cantidad - cant

cuenta = Cuenta("Abner Saavedra", 1000)
cuenta.mostrar_datos_cuenta()
cantidadEgreso = float(input("Ingrese cantidad debito: "))
cuenta.retirar_cantidad(cantidadEgreso)
cuenta.mostrar_datos_cuenta()
cantidadIngreso = float(input("Ingrese cantidad abono: "))
cuenta.ingresar_cantidad(cantidadIngreso)
cuenta.mostrar_datos_cuenta()