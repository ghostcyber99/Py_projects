#!/user/bin/bash/python3 

from email import message 
import socket

#serversocket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname() 
port = 444

#binding to the object created 
serversocket.bind(host, port)

#listener for client
serversocket.listen(3)

while True:
    #starting the connection 
    clientsocket, address = serversocket.accept()

    print("connection established with" % str(address))

    message = "hello thank you for connecting" + "\r\n"
    clientsocket.send(message.encode("ascii"))  


    clientsocket.close 
 