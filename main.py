from tkinter import *
from os import getcwd
from tkinter import messagebox
import socket
import pickle # used to encode/decode information before it is sent to the server 
from load_server_frames import *
import threading

# Function for the host to submit their info
def host_submit():
    
    # Gets the information from the entries and stores them as a list
    room = config_room_name_entry.get()
    password = config_password_entry.get()
    host_info = pickle.dumps([room, password])
    
    # If the the password/room name is not within 16 characters it throws an error
    if len(room) > 16 or len(password) > 16:
        messagebox.showerror(title="Error", message="Room name and password must not be longer than 16 characters")
    else:
        # send room info to the server
        config_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        config_socket.connect((HOST, PORT))
        config_socket.sendall(host_info)
        config_socket.close()
        
        


# Function for configuring a new server
def config_server():
    
    # Destroy root
    root.destroy()
    
    # Creating window for creating a server
    global config_window
    config_window = Tk()
    config_window.geometry(f'{int(WIDTH/2)}x{int(HEIGHT/2)}')
    config_window.config(bg='#03001C')
    config_window.title("Enigma Server Creation")
    config_window.resizable(width=False, height=False)
    
    # Creating the label for the "title"
    config_label = Label(config_window, text="Enter A Room Name and (Optional) Password", font=FONT,
                         fg=TEXT_FG, bg=TEXT_BG, width = 50)
    config_label.pack()
    
    # Creating a label to have the user enter a room name
    config_room_name_label = Label(config_window, text="Room Name: ",
                                   font=FONT, fg=TEXT_FG, bg=TEXT_BG, 
                                   width=50)
    config_room_name_label.pack()
    
    # Creating the entry box for room name
    global config_room_name_entry
    config_room_name_entry = Entry(config_window, fg=TEXT_FG, bg=TEXT_BG, font=FONT, width=50)
    config_room_name_entry.pack()
    
    # Creating a password label
    config_password_label = Label(config_window, text="Password: ", width=50, bg=TEXT_BG, fg=TEXT_FG, font=FONT)
    config_password_label.pack()
    
    # Creating the entry box for password
    global config_password_entry
    config_password_entry = Entry(config_window, width=50, fg=TEXT_FG, bg=TEXT_BG, font=FONT)
    config_password_entry.pack()
    
    # Creating a submit button
    room_submit_button = Button(config_window, width=50, font=FONT, fg=TEXT_FG, bg=TEXT_BG, text="Submit", command=host_submit,
                                activebackground=TEXT_BG, activeforeground=TEXT_FG)
    room_submit_button.pack()
    
    # Go back to home screen
    back_to_home = Button(config_window, width=50, font=FONT, fg=TEXT_FG, bg=TEXT_BG, 
                          activebackground=TEXT_BG, activeforeground=TEXT_FG, command=main,
                          text="Back to home screen")
    back_to_home.pack()
    
  


# Function for loading the frames with server info that takes two parameters
# starting_index is index the thread will start at
# Column is the column the thread will target
def load_frames(starting_index, column):
    
    # We will use this to access items within our lists
    index = starting_index
    
    # We will use this in case the loop iterates to an index that doesn't exist within our list
    index_exists = True
    
    # Variable for iterating through each row
    row = 0
    
    # While the index is within our list
    while index_exists:
        
            try:
                
                # Create a new serverInfo object using the information from our index and the row and column variables
                server_display = serverInfo(join_window, open_hosts[index], row, column)
                
                # Move the index three steps (There are three threads)
                index +=3
                
                # Move to next row
                row +=1
                
                # Update the screens
                join_window.update_idletasks()
                join_window.update()
                
            # In case of error, end the while loop
            except Exception:
                index_exists = False
            
            
                 
            
    
    
def load_server():
    
    # Destroy root
    root.destroy()
    
    # Creating blank window to display all of the servers
    global join_window
    join_window = Tk()
    join_window.geometry(f'{int(WIDTH/2)}x{int(HEIGHT/2)}')
    join_window.config(bg='#03001C')
    join_window.title("Enigma Server List")
    join_window.resizable(width=False, height=False)
    
    
    
    # Gather all available servers
    load_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    load_socket.connect((HOST, PORT))
    load_socket.sendall(b'roomrequest')
    
    # Store open servers within a list 
    global open_hosts
    open_hosts = load_socket.recv(1024)
    print(pickle.loads(open_hosts))
    open_hosts = pickle.loads(open_hosts)
    
    
    
    # Threads that target our function 
    # They have to be daemon threads, otherwise the program will break
    column_zero_thread = threading.Thread(target=load_frames, args=(1, 0), daemon=True)
    column_one_thread = threading.Thread(target=load_frames, args=(2, 1), daemon=True)
    column_two_thread = threading.Thread(target=load_frames, args=(3, 2), daemon=True)
    
    
    # Starting the threads
    column_zero_thread.start()
    column_one_thread.start()
    column_two_thread.start()
    
    
    
    # Mainloop because without this it breaks
    join_window.mainloop()
    
    

# This function changes our username to whatever is within our username_entry
def set_username():
    
    if len(username_entry.get()) < 16:
        global username
        username = username_entry.get()
    else:
        messagebox.showerror(title="Error", message="The username entered was not within 16 characters")
    
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
    username_label = Label(settings_window, text="Enter a username:  ", font=FONT, fg=TEXT_FG, bg=TEXT_BG)
    username_label.pack(side=TOP)
    
    # Username entry that allows the user to pick the username
    # By default this is set to "Anonymous"
    global username_entry
    username_entry = Entry(settings_window, font=FONT, fg=TEXT_FG, bg='#03001C')
    username_entry.pack()
    username_entry.insert(0, username)
    
    # Submit button to submit our username
    # This is binded to the set_username function
    username_submit_button = Button(settings_window, text="Submit your username", font=('Courier', 18), fg=TEXT_FG, bg=TEXT_BG,
                                    command=set_username, activebackground=TEXT_BG, activeforeground=TEXT_FG)
    username_submit_button.pack()
    
    # Sets the focus of our application to settings
    settings_window.grab_set()
    


def main():
    
    # Try to destroy the other screen if we decide to go back to home screen
    try:
        config_window.destroy()
    except Exception:
        pass
    
    

    # Creation of main window
    global root
    root = Tk()

    # Constants used for taking the height of the users screen
    global HEIGHT
    global WIDTH
    HEIGHT = root.winfo_screenheight()
    WIDTH = root.winfo_screenwidth()

    

    # Sets the window to be a quarter of our screen
    root.geometry(f'{int(WIDTH/2)}x{int(HEIGHT/2)}')

    # Config stuff for background, title, image, etc.
    root.title("Enigma")
    root.config(bg='#03001C')
    root.resizable(width=False, height=False)
    root.iconphoto(True, PhotoImage(file=f'{getcwd()}\\Kirby.png'))


    # Button for creating a server. Binded to create_server function
    create_server_button = Button(root, text="CREATE A SERVER", command=config_server, fg=TEXT_FG, bg=TEXT_BG,
                                font=FONT, activebackground=TEXT_BG, activeforeground=TEXT_FG)
    create_server_button.place(relx=.5, rely=.2, anchor='center')

    # Button for joining a server. Binded to load_server function
    load_server_button = Button(root, text="JOIN A SERVER", command=load_server, fg=TEXT_FG, bg=TEXT_BG,
                                font=FONT, activebackground=TEXT_BG, activeforeground=TEXT_FG)
    load_server_button.place(relx=.5, rely=.4, anchor='center')

    # Button for settings. Binded to settings function
    settings_button = Button(root, text="SETTINGS", command=settings, fg=TEXT_FG, bg=TEXT_BG,
                                font=FONT, activebackground=TEXT_BG, activeforeground=TEXT_FG)
    settings_button.place(relx=.5, rely=.6, anchor='center')

    # Some gibberish tkinter needs
    root.mainloop()
    
if __name__ == "__main__":
    
    # By default, this is the username
    global username
    username = "Anonymous"
    
    # Constants of the server address and port
    global HOST
    global PORT
    HOST = "18.224.63.138"
    PORT = 5222
    
    # Constants for setting the color of the text (FG) and background (BG) and font
    global TEXT_BG
    global TEXT_FG
    global FONT
    TEXT_FG = '#abdbe3'
    TEXT_BG = '#301E67'
    FONT = ('Courier', 20)
    
    main()