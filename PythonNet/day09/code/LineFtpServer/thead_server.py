from socket import *
import os
import sys
from threading import *
import traceback


"""基于threading的多线程并发"""


# 创建套接字
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)


def handler(connfd):
    print("connfd from:", connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b"Receive request")
    connfd.close()
    sys.exit(0)
    pass


# 等待客户端请求
while True:
    # noinspection PyBroadException
    try:
        connfd, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception:
        traceback.print_exc()
        continue

    t = Thread(target=handler, args=(connfd,))
    # 守护进程，主线程结束后分支进程自动结束
    t.setDaemon(True)
    t.start()
