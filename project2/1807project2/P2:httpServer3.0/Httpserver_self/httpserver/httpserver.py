#coding=uf-8
"""
    name:cooper
    E-mail:huafengdongji@hotmial.com
    Time:20180929

"""
import sys      # 进程间通信
import re       # 正则表达式，匹配请求方法和内容
import time
from socket import *        # 套接字
from threading import Thread    # 多线程并发
from .setting import *


class HTTPServer(object):

    def __init__(self, addr=('0.0.0.0', 80)):
        """
            绑定套接字，链接地址
        """
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.addr = addr

    def bind(self, addr):
        """
            分散创建方法降低函数内聚性
        :param addr:
        :return:
        """
        self.ip = addr[0]
        self.port = addr[1]
        self.sockfd.bind(addr)

    def server_forever(self):
        """启动HttpServer服务"""
        self.sockfd.listen(3)
        print("Listen to the port:", self.port)
        # 阻塞监听端口
        while True:
            try:
                connfd, addr = self.sockfd.accept()
            except Exception as e:
                print('客户端强制退出', e)
                continue
            # 开启子线程
            handle_client = Thread(target=self.handle_request, args=(connfd,))
            # 设置守护程序，父进程退出，子进程也退出，为下面创建子进程时关闭主进程作准备
            handle_client.daemon(True)
            handle_client.start()


    def handle_request(self, connfd):
        request = connfd.recv(4096)
        request_lines = request.splitlines()
        # 获取请求行
        request_line = request_lines[0].decode()
        # 使用正则表达式提取出请求方法和请求内容
        pattern = r"(?P<METHOD>[A-Z]+)\s+(?P<PATH>/\s*)"
        try:
            env = re.match(pattern, request_line).groupdict()
        except:
            respoonse_handlers = 'HTTP/1.1 500 ServerError\r\n'

            # 看到视频的62分



if __name__ == "__main__":
    # 如果在init中没有从setting导入ADDR则需要在此处导入
    httpd = HTTPServer()
    httpd.server_forever()
