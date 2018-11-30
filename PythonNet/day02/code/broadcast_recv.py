from socket import *

# 创建套接字
s = socket(AF_INET, SOCK_DGRAM)

# 设置套接字可以接受广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# 绑定固定端口
s.bind(('0.0.0.0', 8888))

# 接收
while True:
    try:
        msg, addr = s.recvfrom(1024)
        print('从{}获取信息：{}'.format(addr, msg.decode()))
    except (KeyboardInterrupt, SyntaxError):
        raise
    except Exception as e:
        print(e)

s.close()
