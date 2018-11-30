from select import select
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# f = open('receive.txt', 'wb')
rlist = [s]
wlist = []
xlist = [s]
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print('connect from:', addr)
            rlist.append(c)         # 持续关注该链接
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                f.write(data.encode())
                print(data)
                # 将客户端套接字放入wlist列表
                wlist.append(r)
    for w in ws:
        w.send(b'receive your message')
        wlist.remove(w)
    for x in xs:
        if x is s:
            s.close()
