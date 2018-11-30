from socket import *
sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.bind(('127.0.0.1', 7777))
sockfd.listen(5)
while True:
    print("开始新的循环收发")
    connfd, addr = sockfd.accept()
    while True:
        data_recv = connfd.recv(1024).decode()
        # if data_recv == "##" or '':
        if not data_recv:
            print("客户端退出")
            break
        print(data_recv)
        data_send = data_recv
        n = connfd.send(data_send.encode())
        print("发送了回执%s字节" % n)
    connfd.close()
sockfd.close()
