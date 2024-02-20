import json 

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
user = Usuario("Daniel","Mejias")
print(user.__dict__)
###############################################################################
json_data = json.dumps(user.__dict__) #Serializar              
print(json_data)
###############################################################################
json_data_des = json.loads(json_data) #Deserial
print(json_data_des)
###############################################################################
print(Usuario(**json.loads(json_data)))

