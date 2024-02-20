triple = """Primera línea 
esto se verá en la otra línea
            """
#print(triple)

cadena = "Python "+"es "+"el "+"mejor "+"lenguaje"

cadena = "Python "*10

#print(cadena)

# Operador de interpolación

name = "Abner"
age = 32

#saludo = "Hola mi nombre es %s y tengo %s años de edad." % (name, age)

# Operador str.format

saludo = "Hola mi nombre es {} y tengo {} años de edad.".format(name, age)


# Operador f-strings

saludo = f"Hola mi nombre es {name} y tengo {age} años de edad."

print(saludo)
