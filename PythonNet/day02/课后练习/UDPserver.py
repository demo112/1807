#! /usr/local/bin/python3.7
from socket import *
sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(('127.0.0.1', 8888))
while True:
    data, addr = sockfd.recvfrom(1024)
    print("receive from %s:%s" % (addr, data.decode()))
    data = "RECEIVED %s" % data.decode()
    sockfd.sendto(data.encode(), addr)
