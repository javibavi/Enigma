import socket
import pickle 
import os

HOST = "52.14.62.221"
PORT = 5222
username = "anon"

cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

def point_check(max, min):
    while True:
        try: usinp = int(input("$: "))
        except KeyboardInterrupt: quit()
        except: continue
        if min < usinp < max: return usinp

def room_join():
    cls()
    roomjoin_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    roomjoin_socket.connect((HOST, PORT))
    roomjoin_socket.sendall(b'roomrequest')
    open_hosts = pickle.loads(roomjoin_socket.recv(1024))
    
    print('|     room name     |\n')
    for x, roomname in enumerate(open_hosts[1:]):
        print(f'{x+1}) {roomname[2]}')
    print('0 to exit')
    print('____________________')
    print('\nenter room to join -')
    usinp = point_check(len(open_hosts), 1)
    
    if usinp == 0: 
        roomjoin_socket.close()
        main()
    
    else:
        roomjoin_socket.sendall('deleterequest')
        roomjoin_socket.sendall(usinp)
    
def room_gen(): 
    cls()
    print("           _                \n ___ ___  (_)__ ___ _  ___ _\n/ -_) _ \/ / _ `/  ' \/ _ `/\n\__/_//_/_/\_, /_/_/_/\_,_/ \n          /___/             \n\n")
    while True:
        roomname = input("enter room name: ")
        password = input("enter room password: ")  
        if 0 < len(roomname) < 16 and 0 < len(password) < 16:
            host_info = pickle.dumps([roomname, password])
            hostgen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hostgen_socket.connect((HOST, PORT))
            hostgen_socket.sendall(host_info)
            hostgen_socket.close()
            break
        print("room name and password must not be longer than 16 characters")
    print("server configured, type 1 to exit")
    if point_check(2, 0) == 1: main() 
        
def settings():
    cls()
    global username

    print("           _                \n ___ ___  (_)__ ___ _  ___ _\n/ -_) _ \/ / _ `/  ' \/ _ `/\n\__/_//_/_/\_, /_/_/_/\_,_/ \n          /___/             \n\n")
    print(f'1) change username ("{username}")\n2) back')
    usinp = point_check(3, 0)
    if usinp == 1: 
        username = input("enter username: ")
        settings()
    if usinp == 2: main()
    

def main():
    cls()
    
    print("           _                \n ___ ___  (_)__ ___ _  ___ _\n/ -_) _ \/ / _ `/  ' \/ _ `/\n\__/_//_/_/\_, /_/_/_/\_,_/ \n          /___/             \n\n")
    print('1) join a server\n2) create a server\n3) settings\n')
    
    point = point_check(4, 0)

    if point == 1: room_join()
    if point == 2: room_gen()
    if point == 3: settings()
    
if __name__ == "__main__":
    main()
