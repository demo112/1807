import re
import sys
import time
from settings import *
from socket import *
from threading import Thread

STATIC_DIR = "./static"

# webframe服务器类
class WebFrame(object):
    def __init__(self, frame_address):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(frame_address)

    # 启动服务器
    def start(self):
        self.sockfd.listen(10)
        print("框架服务器启动")
        while True:
            connfd, addr = self.sockfd.accept()
            method = connfd.recv(4096).decode()
            path_info = connfd.recv(4096).decode()
            self.handle(connfd, method, path_info)

    # 处理请求
    def handle(self, connfd, method, path_info):
        if method == "POST":
            pass
        elif method == 'GET':
            if path_info == '/':
                response = self.get_html("/index.html")
            else:
                response = self.get_html(path_info)
            connfd.send(response.encode())
            connfd.close()

    def get_html(self, path_info):
        full_path = STATIC_DIR + path_info
        try:
            fd = open(full_path)
        except:
            response = '404'
            print("Open file err")
        else:
            response = fd.read()
            fd.close()
        return response

if __name__ == "__main__":
    webfarme = WebFrame(frame_address)
    webfarme.start()