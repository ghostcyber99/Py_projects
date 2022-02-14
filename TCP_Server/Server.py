#!/user/bin/bash/python3 

from email import message
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444

#binding to the object created 
serversocket.bind(host, port)

#listener for client
serversocket.listen()

while True:
    clientsocket, address = serversocket.accept()

    print("connection established with" % str(address))

    message = "hello thank you for connecting" + "\r\n"

    clientsocket.close
