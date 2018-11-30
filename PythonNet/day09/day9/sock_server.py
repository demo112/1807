#多进程　tcp　server
from socketserver import * 

#创建server类
# class Server(ForkingMixIn,TCPServer):
# class Server(ForkingTCPServer):
#     pass 

#多线程tcp并发
class Server(ThreadingTCPServer):
    pass


#具体的请求处理类
class Handler(StreamRequestHandler):
    def handle(self):
        # self.request ==> accept返回的套接字
        print("Connect from",\
            self.request.getpeername())
        while True:
            data = self.request.recv(1024).decode()
            if not data:
                break
            print(data)
            self.request.send(b'Receive')

#创建ｓｅｒｖｅｒ对象
server = Server(("0.0.0.0",8888),Handler)

#启动服务器
server.serve_forever()
