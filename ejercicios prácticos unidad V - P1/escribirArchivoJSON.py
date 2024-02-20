import json

diccionario = {
    "nombre": "Daniel",
    "apellido": "Farías",
    "edad": 32
}

with open("data.json", "w") as file:
    json.dump(diccionario, file)