import json

diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "pais": "Colombia"
}

with open("data.json", "w") as file :    
    json.dump(diccionario, file)
    
