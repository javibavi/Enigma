from tkinter import *
import os


class Gui:
    
    def __init__(self, geometry: str, bgcolor: str, title: str):
        
        self.window = Tk()
        
        self.window.geometry(geometry)
        
        self.window.config(bg=bgcolor)
        
        self.window.title(title)
        
        self.window.resizable(height=False, width=False)
        
        if os.name == 'nt':
            self.window.iconphoto(True, PhotoImage(file=f'{getcwd()}\\Kirby.png'))
    
    def call(self):
        
        self.window.mainloop();