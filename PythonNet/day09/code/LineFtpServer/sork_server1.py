from socketserver import *


# 创建服务器类
# class Server(ThreadingUDPServer):等效
class Server(ThreadingMixIn, UDPServer):
        pass


class Handler(DatagramRequestHandler):
    def handle(self):
        # self.request = accept 返回的套接字

        while True:
            data = self.rfile.readline()
            data.self.request[1].recvfrom(1024)
            print(self.client_address)
            if not data:
                break
            print(data)
            self.wfile.write(b"Receive")



if __name__ == "__main__":
    server_addr = ('0.0.0.0', 6666)
    # 创建服务器对象
    server = Server(server_addr, Handler)   # 当服务求接到来自与server_addr的请求，调用Handler处理
    server.serve_forever()
