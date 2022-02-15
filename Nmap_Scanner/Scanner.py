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
                3)Comprehensive  """)

print(f"you have selected option: {resp}")
