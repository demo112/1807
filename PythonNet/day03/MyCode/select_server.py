from select import select
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 9999))
s.listen(3)

rlist = [s]
wlist = []
xlist = []
# 提交我们关注的IO等待IO发生
rs, ws, xs = select(rlist, wlist, xlist)
print('有IO事件发生')
c, addr = rs[0].accept()
print('connect from:', addr)
