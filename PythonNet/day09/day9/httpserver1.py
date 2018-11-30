from socket import * 
from threading import Thread 
import time 

#存放静态页面
STATIC_DIR = "./static"
ADDR = ('0.0.0.0',8000)

#HTTPServer类，封装具体功能
class HTTPServer(object):
    def __init__(self,address):
        #创建套接字
        self.sockfd = socket()
        self.sockfd.setsockopt\
        (SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(address)
        self.sockfd.listen(5)
        #为对象增加属性变量
        self.name = "HTTPServer"
        self.port = address[1]
        self.address = address 

    #启动服务器
    def serve_forever(self):
        print("Listen the port %d"%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            #创建线程处理具体请求
            clientThread = Thread\
            (target = self.handleRequest,args = (connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    def handleRequest(self,connfd):
        #接收客户端请求
        request = connfd.recv(4096)
        #按行切割　字符串
        requestHeadlers = request.splitlines()
        #获取请求行
        print(connfd.getpeername(),":",\
            requestHeadlers[0]) 
        #获取请求内容
        getRequest = str(requestHeadlers[0]).split(' ')[1]

        if getRequest == '/' or getRequest[-5:] == '.html':
            data = self.get_html(getRequest)
        else:
            data = self.get_data(getRequest)

        connfd.send(data.encode())
        connfd.close()

    def get_html(self,page):
        if page == "/":
            filename = STATIC_DIR + "/index.html"
        else:
            filename = STATIC_DIR + page

        try:
            f = open(filename)
        except Exception:
            #没有找到页面
            responseHeadlers = "HTTP/1.1 404 Not Found\r\n"
            responseHeadlers += "Content-Type: text/html\r\n"
            responseHeadlers += '\r\n'
            responseBody = "<h1>Sorry,not found the page</h1>"
        else:
            responseHeadlers = "HTTP/1.1 200  OK\r\n"
            responseHeadlers += "Content-Type: text/html\r\n"
            responseHeadlers += '\r\n'
            responseBody = f.read()
        finally:
            return responseHeadlers + responseBody

    def get_data(self,data):
        responseHeadlers = "HTTP/1.1 200 OK\r\n"
        responseHeadlers += "\r\n"

        if data == "/time":
            responseBody = time.ctime()
        elif data == "/tedu":
            responseBody = "Welcome to tedu"
        else:
            responseBody = "The data not found"
        return responseHeadlers + responseBody


if __name__ == "__main__":
    #生成服务器对象
    httpd = HTTPServer(ADDR)
    #启动服务器
    httpd.serve_forever()