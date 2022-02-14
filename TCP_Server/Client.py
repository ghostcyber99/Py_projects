#!/user/bin/python3

from email import message
import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname()

port = 444

clientsocket.connect(host, port)

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
 