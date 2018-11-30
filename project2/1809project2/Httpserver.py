"""多线程Httpserver服务器"""
import re
import sys
import time
from settings import *
from socket import *
from threading import Thread


# WebFrame通信函数
def connect_frame(METHOD, PATH_INFO):
    s = socket()
    try:
        s.connect(frame_address)
    except:
        print("Connect err")
        return
    s.send(METHOD.encode())
    time.sleep(0.1)
    s.send(PATH_INFO.encode())
    response = s.recv(4096).decode()
    if not response:
        s.close()
        return "404"
    else:
        s.close()
        return response



# 封装Httpserver类
class Httpserver(object):

    def __init__(self, address):
        self.address = address
        self.create_socket()     # 创建套接字
        self.bind(address)       # 绑定

    def create_socket(self):
        """创建套接字"""
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self, address):
        """绑定"""
        self.ip = address[0]
        self.port = address[1]
        self.sockfd.bind(address)
        pass

    def server_forever(self):
        """监听，启动服务器"""
        self.sockfd.listen(10)
        print("Sever start on:", self.port)
        # 循环接收
        while True:
            connfd, addr = self.sockfd.accept()
            print("Connect from:", addr)
            # 创建处理请求的线程
            handle_client = Thread(target=self.handle,
                                   args=(connfd,))
            # 设置守护线程
            handle_client.setDaemon(True)
            # 启动线程
            handle_client.start()

    def handle(self, connfd):
        request = connfd.recv(4096)
        if not request:
            connfd.close()
            return

        # 将请求行按照换行符进行拆分
        request_lines = request.splitlines()
        # 获取请求行
        request_line = request_lines[0].decode()
        print(request_line)

        # 判断请求行的合法性
        pattern = r'(?P<METHOD>[A-Z]+)\s+(?P<PATH_INFO>/\s*)'
        try:
            env = re.match(pattern, request_line).groupdict()
            print(env)
        except:
            response = "http/1.1 500 server error\r\n"
            response += "\r\n"
            response += "Server error"
            connfd.send(response.encode())
            connfd.close()
            return

        # 正常数据处理
        content = connect_frame(**env)      # 调用另外的服务
        if content == '404':
            header = "HTTP/1.1 404 NOT FOUND\r\n"
            header += "\r\n"
            body = "Sorry not Found"
            response = header + body
        else:
            header = "HTTP/1.1 200 OK\r\n"
            header += "\r\n"
            response = header + content
        connfd.send(response.encode())
        connfd.close()

if __name__ == "__main__":
    httpserver = Httpserver(ADDR)
    httpserver.server_forever()