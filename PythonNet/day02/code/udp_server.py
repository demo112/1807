from socket import *

# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('0.0.0.0', 8888)
sockfd.bind(server_addr)

# 消息的收发
while True:
    print("Waiting for your input......")
    data, addr = sockfd.recvfrom(1024)
    print('从%s收到消息%s' % (addr, data.decode()))
    sockfd.sendto('收到你的消息'.encode(), addr)

# noinspection PyUnreachableCode
sockfd.close()
