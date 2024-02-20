class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Agenda:
    def __init__(self):
        self.contactos = []


    def agregar_contacto(self, nombre, telefono):
        contacto = Contacto(nombre, telefono)
        self.contactos.append(contacto)
        print("Contacto agregado con éxito.")
    
    def buscar_contacto(self, buscar):
        resultados = [contacto for contacto in self.contactos if buscar.lower() in contacto.nombre.lower()]
        return resultados
    
    def borrar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                print("Contacto eliminado.")
                return
            else:
                print("Contacto no encontrado.")
    
    def listar_contactos(self):
        if len(self.contactos) != 0:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print("Nombre :" , contacto.nombre, "Numero : " ,contacto.telefono)
        else:
            print("No hay contactos en la agenda.")

agenda = Agenda()

def main():
        while True:
            print("Menú:")
            print("1. Añadir contacto")
            print("2. Buscar contacto")
            print("3. Borrar contacto")
            print("4. Listar contactos")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre = input("Ingrese el nombre del contacto: ")
                telefono = input("Ingrese el número de teléfono: ")
                agenda.agregar_contacto(nombre, telefono)
            elif opcion == '2':
                buscar = input("Ingrese el nombre del contacto a buscar: ")
                resultados = agenda.buscar_contacto(buscar)
                if resultados:
                    print("Resultados de la búsqueda:")
                    for contacto in resultados:
                        print("nombre :", contacto.nombre, "telefono : " ,contacto.telefono)
                else:
                    print("No se encontraron contactos que coincidan con el término de búsqueda.")
            elif opcion == '3':
                nombre = input("Ingrese el nombre del contacto a borrar: ")
                agenda.borrar_contacto(nombre)
            elif opcion == '4':
                agenda.listar_contactos()
            elif opcion == '5':
                print("Saliendo del programa...")
                exit()
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

main()