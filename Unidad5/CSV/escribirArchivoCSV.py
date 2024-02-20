import csv

row = ["Daniel ", "Mejias", 17]

#Abre el archivo en modo de escritura

with open("ArchivoCSV.csv", "w") as file:

    #Crea un objeto csv
    csv_writer = csv.writer(file)

    #Escribe en el archivo
    csv_writer.writerow(row)