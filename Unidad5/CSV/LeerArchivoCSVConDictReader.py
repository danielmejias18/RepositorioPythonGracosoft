import csv


row = {"nombre": "manzana", "cajones": 50, "precio":27}

with open("ArchivoCSV.csv", 'w', newline="") as file:
    fieldnames = ["nombre", "cajones", "precio"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    csv_writer.writerow(row)
        