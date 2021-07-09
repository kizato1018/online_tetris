import socket
import time

HOST = '127.0.0.1'
PORT = 7414

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    msg = "server send : %s " % data.decode()
    print(msg)
    s.send(str.encode(msg))