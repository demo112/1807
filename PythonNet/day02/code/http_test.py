from socket import *


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('192.168.31.234', 5555))
s.listen(5)
while True:
    c, addr = s.accept()
    print('Connect from', addr)
    data = c.recv(4096)
    print("*******************")
    print(data.decode())
    print("*******************")
    data = '''HTTP/1.1 200 OK
    Content-Encoding: gzip
    Content-type: text/html
    
    <h1>Welcome to Cooper</h1>
    <p>这是一个测试</p>
    '''
    c.send(data.encode())
    c.close()
s.close()
