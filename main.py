import socket
import pickle 
import os

HOST = "18.224.63.138"
PORT = 5222
username = "anon"

cls = lambda: os.system('cls')

def point_check(max):
    while True:
        try: usinp = int(input("$: "))
        except KeyboardInterrupt: quit()
        except: continue
        if 0 < usinp < max: return usinp

def room_join():
    cls()
    roomjoin_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    roomjoin_socket.connect((HOST, PORT))
    roomjoin_socket.sendall(b'roomrequest')
    open_hosts = roomjoin_socket.recv(1024)
    
    # print open hosts
        
def room_gen(): # NOT CONFIGURED
    while True:
        roomname = input("enter room name: ")
        password = input("enter room password: ")  
        if len(roomname) < 16 and len(password) < 16:
            host_info = pickle.dumps([roomname, password])
            hostgen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hostgen_socket.connect((HOST, PORT))
            hostgen_socket.sendall(host_info)
            hostgen_socket.close()
            break
        print("room name and password must not be longer than 16 characters")
        
def settings():
    cls()
    global username
    
    print(f'1) change username ("{username}")\n2) back')
    usinp = point_check(3)
    if usinp == 1: 
        username = input("enter username: ")
        settings()
    if usinp == 2: main()
    

def main():
    cls()
    
    print("           _                \n ___ ___  (_)__ ___ _  ___ _\n/ -_) _ \/ / _ `/  ' \/ _ `/\n\__/_//_/_/\_, /_/_/_/\_,_/ \n          /___/             \n\n")
    print('1) join a server\n2) create a server\n3) settings\n')
    
    point = point_check(4)

    if point == 1: room_join()
    if point == 2: room_gen()
    if point == 3: settings()
    
if __name__ == "__main__":
    main()
