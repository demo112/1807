"""
    http server v2.0
    1.多线程并发
    2。可以请求简单数据
    3。能进行简单请求解析
    4。结构使用类进行封装
"""
from socket import *
from threading import *
import sys
import traceback


# HttpServer类 封装具体的服务器功能
class HttpServer(object):
    def __init__(self, addr, ser_dir):
        self.server_address = addr
        self.static_dir = ser_dir
        self.ip = addr[0]
        self.port = addr[1]
        # 创建套接字
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(self.server_address)

    def handleRequest(self, connfd):
        """客户端请求函数"""
        # 接收客户端请求
        request = connfd.recv(1024)
        # print(request)
        requestHeaders = request.splitlines()
        print(connfd.getpeername(), ":", requestHeaders[0])
        # 获取具体请求内容
        getRequest = str(requestHeaders[0]).split(' ')[1]
        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(connfd, getRequest)
        else:
            self.get_data(connfd, getRequest)
        connfd.close()
    def get_data(self, connfd, getRequest):
        urls = ["/time", "/tedu", "/python"]
        if getRequest in urls:
            responseHeaders = "HTTP/1.1 200 ok\r\n"
            responseHeaders += "\r\n"
            if getRequest == "/time":
                import time
                responseBody = time.ctime()
            elif getRequest == "/tedu":
                responseBody = "大内欢迎你"
            elif getRequest == "/python":
                responseBody = "人生苦短我用python"
        else:
            responseHeaders = "HTTP/1.1 404 not found\r\n"
            responseHeaders += "\r\n"
            responseBody = "=====Sorry Not Found Data======"
        response = responseHeaders + responseBody
        connfd.send(response.encode())

    def get_html(self, connfd, getRequest_html):
        if getRequest_html == "/":
            filename = self.static_dir + "系统模块sys.html"
        else:
            filename = self.static_dir + getRequest_html
        responseHeaders = ''
        responseBody = ''
        try:
            f = open(filename, 'r')
        except IOError:
            responseHeaders = "HTTP/1.1 404 not found\r\n"
            responseHeaders += "\r\n"
            responseBody = "=====Sorry not found======"

        else:
            responseHeaders = "HTTP/1.1 200 ok\r\n"
            responseHeaders += "\r\n"
            responseBody = f.read()
        finally:
            respond = responseHeaders + responseBody
            connfd.send(respond.encode())
            # connfd.close()
            # f.close()

    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port:", self.port)
        while True:
            try:
                connfd, addr = self.sockfd.accept()
            except KeyboardInterrupt:
                sys.exit("服务器进程退出")
            except Exception:
                traceback.print_exc()
                continue
            clientTread = Thread(target=self.handleRequest, args=(connfd, ))
            clientTread.setDaemon(True)
            clientTread.start()


if __name__ == "__main__":
    # 服务器IP
    server_addr = ('0.0.0.0', 9999)
    # 在当前文件夹下创建目录存储静态网页
    static_dir = "./static/"
    # 生成对象
    httpd = HttpServer(server_addr, static_dir)
    # 启动服务器
    httpd.serve_forever()
