from tkinter import *
from tkinter import Frame

# Class for storing server info and then displaying it in multiple frames
class serverInfo:
    
    
    # Two params, one for what frame to add this frame to and another 
    def __init__(self, master, info, row, column):
        
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
    tk = Tk()

    frame = Frame(tk)
    frame.pack()

    scrollbar = Scrollbar(frame, orient='vertical')
    scrollbar.grid(row=0, column=3)




    server = serverInfo(frame, ['hot dogs', 'fake ip', 'servername'], 0, 0)



    server1 = serverInfo(frame, ['hot dogs', 'fake ip', 'servername'], 0, 1)
    server2 = serverInfo(frame, ['hot dogs', 'fake ip', 'servername'], 0, 2)
    server3 = serverInfo(frame, ['hot dogs', 'fake ip', 'servername'], 1, 0)
    server4 = serverInfo(frame, ['hot dogs', 'fake ip', 'servername'], 1, 1)
    server5 = serverInfo(frame, ['hot dogs', 'fake ip', 'servername'], 1, 2)
    server6 = serverInfo(frame, ['hot dogs', 'fake ip', 'servername'], 2, 0)
    server7 = serverInfo(frame, ['hot dogs', 'fake ip', 'servername'], 2, 1)


    tk.mainloop()
            

            