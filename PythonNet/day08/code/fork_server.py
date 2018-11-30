import os
from socket import *
import sys
import signal


# 创建套接字
HOST = ""       # 不填写自动默认为'0。0。0。0'
PORT = 8888
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(10)

# 客户端链接
print("进程%s等待客户端链接" % os.getpid())
signal.signal(signal.SIGCHLD, signal.SIG_IGN)       # 在父进程中忽略子进程状态改变，子进程退出自动由系统处理


def client_handler(call):
    """客户端处理函数"""
    print("这是一个客户端处理函数")
    print("来自%s的子进程在处理 %s 的请求" % call.getpeername())
    try:
        while True:
            data = call.recv(1024)
            if not data:
                break
            else:
                print(data.decode())
                call.send("收到客户端请求".encode())
    except (KeyboardInterrupt, SystemError):
        sys.exit("子进程退出")
    except Exception as err:
        print("Error", err)
    call.close()
    sys.exit(0)


while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print("Error:", e)
        continue

    # 为客户端创建新的进程，处理请求
    pid = os.fork()

    # 子进程处理
    if pid == 0:
        s.close()
        client_handler(c)
        pass
    else:
        c.close()
        # 父进程或者创建失败，都继续，接收下一个链接
        continue
