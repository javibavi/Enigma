from tkinter import *
import os

# Simple template for creating gui
class Gui:
    
    # Uses geometry, background color, and title as the initial parameters
    def __init__(self, geometry: str, bgcolor: str, title: str):
        
        self.window = Tk()
        
        self.window.geometry(geometry)
        
        self.window.config(bg=bgcolor)
        
        self.window.title(title)
        
        self.window.resizable(height=False, width=False)
        
        # For windows
        if os.name == 'nt':
            self.window.iconphoto(True, PhotoImage(file=f'{os.getcwd()}\\Kirby.png'))
    
    def call(self) -> None:
        
        self.window.mainloop()