from socket import * 
import os,sys 
from threading import * 

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

#客户端处理函数
def handler(connfd):
    print("Connect from",connfd.getpeername())
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        connfd.send(b'Receive your msg')
    connfd.close()

s = socket()
s.bind(ADDR)
s.listen(5)

while True:
    try:
        connfd,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue 

    t = Thread(target=handler,args= (connfd,))
    t.setDaemon(True)
    t.start()

