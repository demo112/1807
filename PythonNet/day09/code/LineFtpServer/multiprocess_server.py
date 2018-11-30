from socket import *
import os
import sys
from multiprocessing import *
import traceback
import signal


"""基于multiprocessing的多线程并发"""


# 创建套接字
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)


def handler():
    print("connfd from:", connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b"Receive request")
    connfd.close()
    pass


# 让系统自动处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
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

    p = Process(target=handler)     # 进程此处可以不尽兴传参，因为创建子进程将会创建一的独立的空间

    # 守护进程，主线程结束后分支进程自动结束
    p.daemon = True
    p.start()
