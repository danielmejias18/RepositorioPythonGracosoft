

def TablaNumerica():
    num = int(input("Introduce El Numero a Evaluar"))
    nombreArchivo = "tabla-"+str(num)+".txt"
    archivo = open(nombreArchivo, "w")
    if num < 0 or num>10:
        print("Error")
    else: 
        for i in range(1,11):        
            multiplo  = i*num
            escribir = ((str(i) + " x " + str(num) + " = " + str(multiplo) + "\n"))
            archivo.write(escribir)
            print(num, " x ", i ," = ",multiplo)
    archivo.close()
    
        
TablaNumerica()



