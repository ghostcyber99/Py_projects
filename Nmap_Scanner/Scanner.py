#!/usr/bin/python3

import nmap 

scanner = nmap.PortScanner()

print ('Welcome, this is a simple nmap automation tool')
print('<---------------------------------------------------------------------->')

ip_addr = input("please enter the IP, you want to scan: ")
print(f"scanning {ip_addr}")
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive  \n """)

print(f"you have selected option: {resp}")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v sS')
    print(scanner.scaninfo())
    print(("Ip Status: ", scanner[ip_addr].state)) #display the state of the ip 
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys()) #display all the open ports 
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v sU')
    print(scanner.scaninfo())
    print(("Ip Status: ", scanner[ip_addr].state)) #display the state of the ip 
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys()) #display all the open ports 
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print(("Ip Status: ", scanner[ip_addr].state)) #display the state of the ip 
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys()) #display all the open ports 
elif resp >= '4':
    print("please enter a valid option")



     


     


