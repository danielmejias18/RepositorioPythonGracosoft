import csv
filename = "camion.csv"
def diccionariodatos(filename):
    
        file  = open(filename, 'r')
        reader = csv.DictReader(file)
        return reader


def creacionariodatos(diccionario):
    with open("CreacionCsv", 'w', newline="")  as file:
        fieldname = ["nombre", "cajones"]
        writer = csv.DictWriter(file, fieldnames=fieldname)
        writer.writeheader()
        for row in diccionario:
            linea = {'nombre': row['nombre'], 'cajones': row['cajones']}
            writer.writerow(linea)

dic = diccionariodatos("camion.csv")
creacionariodatos(dic) 