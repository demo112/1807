from socket import *
sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.bind(('127.0.0.1', 7777))
sockfd.listen(5)
print("Waiting...")
connfd, addr = sockfd.accept()
while True:
    data = connfd.recv(1024).decode()
    print(data)
    if data == "##":
        break
    data = "收到信息"
    n = connfd.send(data.encode())
    print("发送了%s字节" % n)
connfd.close()
sockfd.close()