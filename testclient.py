import socket, pickle

HOST = "18.224.63.138"
PORT = 5222

load_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
load_socket.connect((HOST, PORT))
open_hosts = load_socket.recv(1024)
print(open_hosts)
load_socket.close()
