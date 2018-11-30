from socket import *

s = socket()

s.bind(('127.0.0.1', 8888))
s.listen(6)

c, addr = s.accept()
print("您已成功链接：", addr)
f = open('recv.jpg', 'wb')
while True:
    data = c.recv(4096)
    if not data:
        break
    f.write(data)
f.close()
c.close()
s.close()
