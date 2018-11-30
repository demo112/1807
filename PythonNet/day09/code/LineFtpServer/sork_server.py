from socketserver import *


# 创建服务器类
# class Server(ForkingTCPServer):等效
class Server(ForkingMixIn, TCPServer):
        pass


class Handler(StreamRequestHandler):
    def handle(self):
        # self.request = accept 返回的套接字
        print("Connect from:", self.request.getpeername())
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            else:
                print(data.decode())
                self.request.send(b"Receive")
        pass


if __name__ == "__main__":
    server_addr = ('0.0.0.0', 6666)
    # 创建服务器对象
    server = Server(server_addr, Handler)   # 当服务求接到来自与server_addr的请求，调用Handler处理
    server.serve_forever()
