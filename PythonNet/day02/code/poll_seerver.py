from socket import *
from select import *

# 注册IO事件
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建Poll对象
p = poll()

# 创建关注IO的地图
fdmap = {s.fileno(): s}

# 注册关注deIO
p.register(s, POLLIN | POLLERR)

while True:
    # 进行IO监控
    events = p.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('Connect from', addr)
            p.register(c.POLLIN | POLLHUP)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                # 客户端推出，从关注事件移除
                p.inregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
        else:
            # noinspection PyUnboundLocalVariable
            print(data.decode())
            fdmap[fd].send(b'Receive')
