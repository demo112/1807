from socket import * 


def clo():
    # 关闭套接字
    connfd.close()
    sockfd.close()


# 创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
# 绑定地址
sockfd.bind(('127.0.0.1', 8888))
# 设置监听
sockfd.listen(5)        # 第二次握手
# 等待客户端连接
while True:
    print("Waiting for connect...")
    connfd, addr = sockfd.accept()
    print("Connect from", addr)
    while True:
        # 消息收发
        data = connfd.recv(1024)
        if data == b'##':
            break
        elif data == b'break':
            break
            # connfd, addr = sockfd.accept()
        print("Receive:", data.decode())
        n = connfd.send(b"Receive your message")
        print("send %d bytes" % n)
    if data == b'break':
        clo()
        break
