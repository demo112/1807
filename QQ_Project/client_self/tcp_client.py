from socket import *


def tcp_client():
    """
    可以实现随时进出服务端，
    进入退出都有服务端提示，
    能循环发送消息
    """
    # 创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 发起连接
    sockfd.connect(('127.0.0.1', 9999))
    while True:
        name = input("请输入您的姓名")
        if not name:
            continue
        else:
            sockfd.sendall(name.encode())
            data = sockfd.recv(1024)
            print(data.decode())
            break

    while True:
        # 消息收发
        print('c等待输入')
        msg = input("Msg>>")
        if msg:
            sockfd.sendall(msg.encode())
            data = sockfd.recv(1024)
            print(data.decode())
        else:
            print('kong')
            break
    print("您已推出")
    sockfd.close()


if __name__ == "__main__":
    tcp_client()
