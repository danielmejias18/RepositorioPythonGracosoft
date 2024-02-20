import json

class Usuario:
    def __init__(self, nom, apell):
        self.nombre = nom
        self.apellido = apell

user = Usuario("Abner", "Saavedra")
print("Objeto python: ", user.__dict__)
json_data = json.dumps(user.__dict__) # Serialización
print("Objeto serializado (formato transportable): ", json_data)
json_data_des = json.loads(json_data) # Deserialización
print("Objeto deserializado (objeto python): ", json_data_des)
#print(Usuario(**json.loads(json_data)))