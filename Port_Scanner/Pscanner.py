#!/usr/bin/python3

import socket

target = input("please enter the target IP: ")
port = input(int("please enter the target port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

def portScanner(port):
    if s.connect_ex((target, port)): #error handling
          print("the port is closed")
    else:
        print("the port is open")


portScanner(port)

