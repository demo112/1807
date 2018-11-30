from socket import * 
import sys 

HOST = sys.argv[1]
PORT = int(sys.argv[2])
#要访问的服务端地址
ADDR = (HOST,PORT)

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input("消息:")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr = sockfd.recvfrom(1024)
    print("从服务端接收：",data.decode())
sockfd.close()