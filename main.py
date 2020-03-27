from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Termómetro")
        self.geometry("280x150")
        self.configure(bg = "#DED789")
        
    def start(self):
        self.mainloop()
        

if __name__ == '__main__':
    app = mainApp()
    app.start()