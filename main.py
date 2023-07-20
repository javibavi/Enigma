from tkinter import *
from os import getcwd



def create_server():
    pass
def join_server():
    pass

# This function changes our username to whatever is within our username_entry
def set_username():
    global username
    username = username_entry.get()
    
# Creates a separate window for settings
def settings():
    
    # Config settings to make our window more vertical and unresizeable
    settings_window = Toplevel()
    settings_window.title("Enigma Settings")
    settings_window.iconphoto(True, PhotoImage(file=f'{getcwd()}\\Kirby.png'))
    settings_window.geometry(f'{int(WIDTH/5)}x{int(HEIGHT/2)}')
    settings_window.config(bg='#03001C')
    settings_window.resizable(width=False, height=False)
    
    # Label to guide the user to enter a username
    username_label = Label(settings_window, text="Enter a username:  ", font=('Courier', 20), fg=TEXT_FG, bg=TEXT_BG)
    username_label.pack(side=TOP)
    
    # Username entry that allows the user to pick the username
    # By default this is set to "Anonymous"
    global username_entry
    username_entry = Entry(settings_window, font=('Courier', 20), fg=TEXT_FG, bg='#03001C')
    username_entry.pack()
    username_entry.insert(0, username)
    
    # Submit button to submit our username
    # This is binded to the set_username function
    username_submit_button = Button(settings_window, text="Submit your username", font=('Courier', 18), fg=TEXT_FG, bg=TEXT_BG,
                                    command=set_username)
    username_submit_button.pack()
    
    # Sets the focus of our application to settings
    settings_window.grab_set()
    
    
# By default, this is the username
username = "Anonymous"

# Creation of main window
root = Tk()

# Constants used for taking the height of the users screen
HEIGHT = root.winfo_screenheight()
WIDTH = root.winfo_screenwidth()

# Constants for setting the color of the text (FG) and background (BG)
TEXT_FG = '#abdbe3'
TEXT_BG = '#301E67'

# Sets the window to be a quarter of our screen
root.geometry(f'{int(WIDTH/2)}x{int(HEIGHT/2)}')

# Config stuff for background, title, image, etc.
root.title("Enigma")
root.config(bg='#03001C')
root.resizable(width=False, height=False)
root.iconphoto(True, PhotoImage(file=f'{getcwd()}\\Kirby.png'))


# Button for creating a server. Binded to create_server function
create_server_button = Button(root, text="CREATE A SERVER", command=create_server, fg=TEXT_FG, bg=TEXT_BG,
                              font=('Courier', 20), activebackground=TEXT_BG, activeforeground=TEXT_FG)
create_server_button.place(relx=.5, rely=.2, anchor='center')

# Button for joining a server. Binded to join_server function
join_server_button = Button(root, text="JOIN A SERVER", command=join_server, fg=TEXT_FG, bg=TEXT_BG,
                            font=('Courier', 20), activebackground=TEXT_BG, activeforeground=TEXT_FG)
join_server_button.place(relx=.5, rely=.4, anchor='center')

# Button for settings. Binded to settings function
settings_button = Button(root, text="SETTINGS", command=settings, fg=TEXT_FG, bg=TEXT_BG,
                            font=('Courier', 20), activebackground=TEXT_BG, activeforeground=TEXT_FG)
settings_button.place(relx=.5, rely=.6, anchor='center')

# Some gibberish tkinter needs
root.mainloop()