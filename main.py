from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    entrada = None
    tipoUnidad = None
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Termómetro")
        self.geometry("280x150")
        self.configure(bg = "#DED789")
        
        self.temperatura = StringVar(value="") # VV de control
        self.tipoUnidad = StringVar(value= "C")
        
        self.createLayout()
        
    def createLayout():
        self.entrada = ttk.Entry(self, variable=self.temperatura)
        
    def start(self):
        self.mainloop()
        

if __name__ == '__main__':
    app = mainApp()
    app.start()