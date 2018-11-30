""""ftp文件服务器"""
import os
import signal
import time
import sys
from socket import *

# 文件库路径
FILE_PATH = "/Users/ftpfile/"
HOST = "0.0.0.0"
PORT = 9999
ADDR = (HOST, PORT)


# 将文件服务器写在类中
class FtpServer(object):
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        """读取文件名列表
            过滤掉隐藏文件和文件夹（目录）"""
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b"OK")
            # 等待是为避免b"OK"与文件内容混淆
            time.sleep(0.1)
        # 创建空白字符串
        files = ''
        print(file_list)
        for file in file_list:
            # 筛除开头为"."的隐藏文件和判断不为为普通文件的文件夹等
            if file[0] != '.' and \
                    os.path.isfile(FILE_PATH + file):
                files += file + '#'
        self.connfd.sendall(files.encode())

    def do_get(self, filename):
        # noinspection PyBroadException
        try:
            fd = open(FILE_PATH + filename, "rb")
        except Exception as e:
            print("读取出错：", e)
            self.connfd.send('文件不存在'.encode())
            return
        self.connfd.send(b"OK")
        time.sleep(1)
        # 发送文件
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)
        print("文件发送完毕")


# 创建套接字，接收客户端链接，创建新的进程
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print("listen to port 8888")

    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常:", e)
            continue
        print("客户端登录:", addr)
        # 创建多线程
        pid = os.fork()
        if pid == 0:
            sockfd.close()
            # 判断客户端请求
            ftp = FtpServer(connfd)
            while True:
                data = connfd.recv(1024).decode()
                if not data or data[0] == 'Q':
                    connfd.close()
                    sys.exit("客户端已退出")
                elif data[0] == "L":
                    ftp.do_list()
                elif data[0] == "G":
                    filename = data.split(' ')[-1]
                    ftp.do_get(filename)

        else:
            connfd.close()
            continue


if __name__ == "__main__":
    main()
