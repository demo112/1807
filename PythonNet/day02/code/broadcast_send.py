from socket import *
from time import sleep

dest = ('192.168.1.255', 8888)
# 创建套接字
s = socket(AF_INET, SOCK_DGRAM)

# 设置太接字可以接受广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# 接收
while True:
    try:
        sleep(2)
        s.sendto('可去你的吧'.encode(), dest)
    except (KeyboardInterrupt, SyntaxError):
        raise
    except Exception as e:
        print(e)

s.close()
