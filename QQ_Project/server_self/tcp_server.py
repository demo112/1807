from socket import *


def tcp_server():
    """可以循环接收客户端申请，"""
    # 创建套接字
    sockfd = socket(AF_INET, SOCK_STREAM)
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 绑定地址
    sockfd.bind(('127.0.0.1', 9999))

    # 设置监听
    sockfd.listen(5)

    # name_addr = {}
    print("聊天室已开启")
    while True:
        # 等待客户端连接
        connfd, addr = sockfd.accept()
        name = connfd.recv(1024)
        connfd.send("您已加入聊天室".encode())
        print("%s已加入" % name.decode())
        while True:
            # 消息收发
            print('s等待接收')
            data = connfd.recv(1024)
            # print(data, data.decode())
            if data:
                print("Receive:", data.decode())
                connfd.send("已收到".encode())
            else:
                print(("%s已退出聊天室" % name.decode()))
                connfd.close()
                break

    # noinspection PyUnreachableCode
    sockfd.close()


if __name__ == "__main__":
    tcp_server()
