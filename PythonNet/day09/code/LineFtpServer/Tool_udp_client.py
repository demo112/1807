# !
from socket import *
import sys

if len(sys.argv) < 3:
    print('''
            argv is error!
            run as 
            python3 udp_client.py 127.0.0.1 8888
            ''')
    raise NameError

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)

# print(sys.argv)
# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 消息的收发
while True:
    data = input("请输入要发送的内容")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    data, addr = sockfd.recvfrom(1024000)
    print('从%s收到消息%s' % (addr, data.decode()))

sockfd.close()
