from tkinter import *


class Gui:
    
    def __init__(self, geometry: str, bgcolor: str, title: str, icon: PhotoImage):
        
        self.window = Tk()
        
        self.window.geometry(geometry)
        
        self.window.config(bg=bgcolor)
        
        self.window.title(title)
        
        self.window.iconphoto(True, icon)
    
    def call(self):
        
        self.window.mainloop();