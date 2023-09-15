from tkinter import *
from tkinter import Frame
import tkinter.ttk as ttk



# Class for storing server info and then displaying it in multiple frames
class serverInfo:
    
    
    # Two params, one for what frame to add this frame to and another 
    def __init__(self, master: Frame, info: list, row: int, column: int):
        
        self.frame = Frame(master, bg='#03001C')
        
        self.info = info
        
        # Creating a label with the server name displayed
        self.label = Label(self.frame, text=f'Server Name: {info[2]}', bg='#301E67', fg='#abdbe3', font=('Courier', 20))
        self.label.pack()
        
        # Creating button for joining a server
        self.button = Button(self.frame, bg='green', activebackground='green', foreground='white', activeforeground='white',
                             font=('Courier', 20), text="Join", command=join_server)
        self.button.pack()
        
        self.frame.grid(row=row, column=column)
        
    
# Function for the action of joining a server
def join_server():
    pass
    
        
        
        
if __name__ == "__main__":
    root = Tk()
    root.title("Scrollbar for a Frame of Frames")
    root.geometry("400x300")

    canvas = Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    frame_container = Frame(canvas)
    canvas.create_window((0, 0), window=frame_container, anchor="nw")

    frame_container.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    row = 0

    for i in range(20):
        serverInfo(frame_container, "test", row, 0)
        row+=1
        

    canvas.configure(yscrollcommand=scrollbar.set)

    root.mainloop()
                

                