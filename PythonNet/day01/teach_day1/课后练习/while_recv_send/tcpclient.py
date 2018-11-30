from socket import *
sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.connect(('127.0.0.1', 7777))
while True:
    data = input("发送内容").encode()
    if  not data:
        break
    sockfd.send(data)
    data = sockfd.recv(1024)
    print("收到了%s" % data.decode())
sockfd.close()
