from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    __temperaturaAnt = ""
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Termómetro")
        self.geometry("160x150")
        self.configure(bg = "#ECECEC")
        self.resizable(0,0) #Esto no deja redimensionar la ventana
        
        self.temperatura = StringVar(value="") # VV de control
        self.temperatura.trace("w", self.validateTemperature) #"trace, w" cada vez que escribimos o borramos en el recuadro llama a la funcion validateTemperature
        self.tipoUnidad = StringVar(value= "C")
        
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        
        self.lblUnidad = ttk.Label(self, text="Grados:").place(x=10, y=45)
        self.unidadF = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F").place(x=20, y=70)
        self.unidadC = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C").place(x=20, y=95)
        
    def start(self):
        self.mainloop()
        
    def validateTemperature(self, *args): #*args: espera una tupla o lista sin numero fijo de vv
        nuevoValor = self.temperatura.get()
        print("nuevoValor: ", nuevoValor)
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor
        except:
            self.temperatura.set(self.__temperaturaAnt)
            print("Valor anterior: ", self.__temperaturaAnt)
if __name__ == '__main__':
    app = mainApp()
    app.start()