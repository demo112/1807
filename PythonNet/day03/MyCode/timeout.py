from socket import *
from time import sleep, ctime


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 将监听套接字设置为超时时间

s.settimeout(5)
while True:
    print("Waiting for connect.....")
    try:
        c, addr = s.accept()
    except timeout:
        sleep(1)
        print(ctime())
        continue
    else:
        print("connect from", addr)
        while True:
            data = c.recv(1024).decode()
            c.setblocking(False)
            if not data:
                break
            print(data)
            s.send(ctime.encode())
        c.close()
s.close()


