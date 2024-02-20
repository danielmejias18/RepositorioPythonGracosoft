class Agenda:
    
    def __init__(self):
         self.contactos =[]

    def agregar_contacto(self):
        print("Agregar contacto" )
        nom = input("Ingrese nombre del contacto: ")
        telf = input("Ingrese telefono del contacto: ")
        email = input("Ingrese email del contacto: ")
        self.contactos.append({"nombre":nom, "telefono":telf, "email":email})
    
    def listar_contacto(self):
        print("Listar contacto" )
        if len(self.contactos) == 0:
            print("No hay contactos agregados")
        else:
            for n in range(0, len(self.contactos)):
                print(self.contactos[n]["nombre"])
           
    
    def buscar_contacto(self):
        print("Buscar contacto" )
        nombre = input("Ingrese nombre del contacto a buscar: ")
        for n in range(0, len(self.contactos)):
            if self.contactos[n]["nombre"] == nombre:
                print("Datos del contacto :")
                print("nombre: "+ self.contactos[n]["nombre"])
                print("telefono: "+ str(self.contactos[n]["telefono"]))
                print("email: "+ self.contactos[n]["email"])
                return n

            
    
    def editar_contacto(self):
        print("Para editar")
        n = self.buscar_contacto()
        print("Selecciona lo que deseas editar:")
        print("1. Nombre")
        print("2. Telefono")
        print("3. Email")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
        while opcion != 4:
            if opcion == 1:
                nombre = input("Ingrese nuevo nombre: ")
                self.contactos[n]["nombre"] = nombre
            elif opcion == 2:
                telefono = input("Ingrese nuevo telefono: ")
                self.contactos[n]["telefono"] = telefono
            elif opcion == 3:
                email = input("Ingrese nuevo email: ")
                self.contactos[n]["email"] = email
           
            print("Selecciona lo que deseas editar:")
            print("1. Nombre")
            print("2. Telefono")
            print("3. Email")
            print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
        
                
            
    
def main():
    print("1. Anadir contacto")
    print("2. Listar contacto")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Salir")
    agenda = Agenda()

    opcion = int(input("seleccione una opcion: "))


    while opcion!= 5:
        if opcion == 1:
            agenda.agregar_contacto()
        elif opcion == 2:
            agenda.listar_contacto()
        elif opcion == 3:
            agenda.buscar_contacto()
        elif opcion == 4:
            agenda.editar_contacto()
        opcion = int(input("seleccione una opcion: "))

main()