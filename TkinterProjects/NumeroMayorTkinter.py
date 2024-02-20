import tkinter as tk

class Application:
    

    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Numero Mayor")
        self.ventana1.geometry("300x300")
        

        self.labelTitulo = tk.Label(self.ventana1, text="***Numero Mayor***")
        self.labelTitulo.place(x = 10, y = 10)
        self.labelTitulo.config(font=("Arial",20))

        self.labelPrimerNumero = tk.Label(self.ventana1, text="Primer numero : ")
        self.labelPrimerNumero.place(x = 8, y = 100)
        self.labelPrimerNumero.config(font=("Arial",10))


        
        self.labelSegundoNumero = tk.Label(self.ventana1, text="Segundo numero : ")
        self.labelSegundoNumero.place(x = 4, y = 120)
        self.labelSegundoNumero.config(font=("Arial",10))


              
        self.labelTercerNumero = tk.Label(self.ventana1, text="tercer numero : ")
        self.labelTercerNumero.place(x = 15, y = 140)
        self.labelTercerNumero.config(font=("Arial",10))


        self.TextBoxPrimerNumero = tk.Entry(self.ventana1, width=10,  )
        self.TextBoxPrimerNumero.place(x = 110, y = 105, height=15)

        self.TextBoxSegundoNumero = tk.Entry(self.ventana1, width=10,)
        self.TextBoxSegundoNumero.place(x = 110, y = 130, height=15)
        
        self.TextBoxTercerNumero = tk.Entry(self.ventana1, width=10,)
        self.TextBoxTercerNumero.place(x = 110, y = 150, height=15)
        
        self.botonevaluar = tk.Button(self.ventana1, text="Calcular", command = self.MayorNumero)
        self.botonevaluar.place(x = 100, y = 180, height=15)


              
        self.labelMayorNumero = tk.Label(self.ventana1, text="Numero Mayor  : ")
        self.labelMayorNumero.place(x =15, y = 200)
        self.labelMayorNumero.config(font=("Arial",10))


        self.EntryMayorNumero = tk.Entry(self.ventana1, width=10,  )
        self.EntryMayorNumero.place(x = 120, y = 210, height=15)



    

        self.ventana1.mainloop()


    def MayorNumero(self):
            numero1 = int(self.TextBoxPrimerNumero.get())
            numero2 = int(self.TextBoxSegundoNumero.get())
            numero3 = int(self.TextBoxTercerNumero.get())
            if numero1 > numero2 and numero1 > numero3:
                self.EntryMayorNumero.insert(0, str(numero1))
            elif numero2 > numero1 and numero2 > numero3:
                self.EntryMayorNumero.insert(0, str(numero2))
            elif numero3 > numero1 and numero3 > numero2:
                self.EntryMayorNumero.insert(0, str(numero3))
            

def main():
    aplication1 = Application()

if __name__ == "__main__":
    main()
    