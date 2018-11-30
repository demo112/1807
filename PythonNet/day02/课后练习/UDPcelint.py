#! /usr/local/bin/python3.7
from socket import *
from sys import argv
addr = argv[1]
port = int(argv[2])
HOST = (addr, port)
sockfd = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Send:")
    if not data:
        break
    sockfd.sendto(data.encode(), HOST)
    data, addr = sockfd.recvfrom(1024)
    print(data.decode())
