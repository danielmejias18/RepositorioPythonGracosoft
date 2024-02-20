class Pantalon:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

class Tienda:
    def __init__(self):
        self.ventas = []

    def agregar_venta(self, codigo, tipo_pantalon, cantidad):
        self.ventas.append((codigo, tipo_pantalon, cantidad))

    def imprimir_detalles_venta(self):
        for venta in self.ventas:
            codigo, tipo_pantalon, cantidad = venta
            precio = self.obtener_precio_por_tipo(tipo_pantalon)
            total_precio = precio * cantidad
            print(f"Venta - Código: {codigo}, Tipo de Pantalón: {tipo_pantalon}, Cantidad: {cantidad}, Precio Total: {total_precio}")

    def obtener_total_ventas(self):
        return len(self.ventas)

    def obtener_cantidad_vendida_por_tipo(self):
        cantidad_por_tipo = {'A': 0, 'B': 0, 'C': 0}
        for venta in self.ventas:
            tipo_pantalon = venta[1]
            cantidad = venta[2]
            cantidad_por_tipo[tipo_pantalon] += cantidad
        return cantidad_por_tipo

    def obtener_tipo_mas_vendido(self):
        cantidad_por_tipo = self.obtener_cantidad_vendida_por_tipo()
        tipo_mas_vendido = max(cantidad_por_tipo, key=cantidad_por_tipo.get)
        return tipo_mas_vendido

    def obtener_monto_total_vendido(self):
        monto_total = 0
        for venta in self.ventas:
            tipo_pantalon = venta[1]
            cantidad = venta[2]
            precio = self.obtener_precio_por_tipo(tipo_pantalon)
            monto_total += precio * cantidad
        return monto_total

    def obtener_precio_por_tipo(self, tipo_pantalon):
        precios = {'A': 30, 'B': 20, 'C': 10}
        return precios[tipo_pantalon]

# Crear una instancia de la clase Tienda
tienda = Tienda()

# Solicitar datos de venta al usuario
while True:
    codigo = input("Ingrese el código de la venta (o 'q' para salir): ")
    if codigo.lower() == 'q':
        break
    tipo_pantalon = input("Ingrese el tipo de pantalón (A, B o C): ")
    cantidad = int(input("Ingrese la cantidad vendida: "))
    tienda.agregar_venta(codigo, tipo_pantalon, cantidad)

# Imprimir detalles de las ventas
tienda.imprimir_detalles_venta()
print("Número total de ventas:", tienda.obtener_total_ventas())
print("Cantidad vendida por tipo de pantalón:", tienda.obtener_cantidad_vendida_por_tipo())
print("Tipo de pantalón más vendido:", tienda.obtener_tipo_mas_vendido())
print("Monto total vendido: $", tienda.obtener_monto_total_vendido())