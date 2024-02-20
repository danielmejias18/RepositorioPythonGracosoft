
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

    def buscar_contacto(self, term):
        resultados = [contacto for contacto in self.contactos if term.lower() in contacto.nombre.lower()]
        return resultados

    def borrar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                print("Contacto eliminado.")
                return
        print("Contacto no encontrado.")

    def listar_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(f"{contacto.nombre}: {contacto.telefono}")
        else:
            print("No hay contactos en la agenda.")

# Crear una instancia de la clase Agenda
agenda = Agenda()

while True:
    print("\nMenú:")
    print("a. Añadir contacto")
    print("b. Buscar contacto")
    print("c. Borrar contacto")
    print("d. Listar contactos")
    print("e. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == 'a':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda.agregar_contacto(nombre, telefono)
    elif opcion == 'b':
        term = input("Ingrese el término de búsqueda: ")
        resultados = agenda.buscar_contacto(term)
        if resultados:
            print("Resultados de la búsqueda:")
            for contacto in resultados:
                print(f"{contacto.nombre}: {contacto.telefono}")
        else:
            print("No se encontraron contactos que coincidan con el término de búsqueda.")
    elif opcion == 'c':
        nombre = input("Ingrese el nombre del contacto a borrar: ")
        agenda.borrar_contacto(nombre)
    elif opcion == 'd':
        agenda.listar_contactos()
    elif opcion == 'e':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")