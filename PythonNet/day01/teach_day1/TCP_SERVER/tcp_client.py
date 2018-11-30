from socket import * 


# 创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
# 发起链接    第一次握手
server_addr = ('127.0.0.1', 8888)
sockfd.connect(server_addr)     # 第一次握手
while True:
    data = input('请输入')
    sockfd.send(data.encode())      # 第三次握手
    if data == '##' or data == 'break':
        break
    data = sockfd.recv(1024)
    print('接收到', data.decode())

# 关闭套接字
sockfd.close()
