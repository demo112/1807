from socket import *


# 确保两端使用同一个套接字文件
sock_file = './sock_file'

# 创建本地套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)

# 链接另一端
sockfd.connect(sock_file)

# 消息收发
while True:
    msg = input("请输入")
    if msg:
        sockfd.send(msg.encode())
        print(sockfd.recv(1024).decode())
    else:
        break
# noinspection PyUnreachableCode
sockfd.close()
