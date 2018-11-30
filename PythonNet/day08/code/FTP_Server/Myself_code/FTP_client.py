import sys
from socket import *



# 基本文件操作功能
class FtpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"L")      # 发送请求
#         等待回复
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print("文件列表接收完毕\n")
        else:
            print("失败原因", data)

    def do_get(self, filename):
        self.sockfd.send(("G " + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            fd = open(filename, "wb")
            while True:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    break
                fd.write(data)
            fd.close()
            print("%s 下载完毕\n" % filename)
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b"Q")


# 网络链接
def main():
    if len(sys.argv) < 3:
        print("your argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    sockfd = socket()

    # 尝试链接
    # noinspection PyBroadException
    try:
        sockfd.connect(ADDR)
    except:
        print("链接失败")
        return

    # 生成类的对象
    ftp = FtpClient(sockfd)
    while True:
        print("===================命令选项===================")
        print("++++++++++++++++++++list+++++++++++++++++++++")
        print("++++++++++++++++++get file+++++++++++++++++++")
        print("++++++++++++++++++put file+++++++++++++++++++")
        print("++++++++++++++++++++quit+++++++++++++++++++++")
        print("===================命令选项===================")

        cmd = input("请输入命令")

        if cmd.strip() == "list":
            ftp.do_list()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd.strip() == 'quit':
            ftp.do_quit()
            sockfd.close()
            sys.exit("谢谢使用")
        else:
            print('请输入正确命令')
            continue


if __name__ == "__main__":
    main()
