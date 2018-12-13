from socket import *


# 创建套接字
def hanlder_client(connfd):
    request = connfd.recv(4096)
    print(request)
    # b'GET / HTTP/1.1' \
    # b'Host: 127.0.0.1:8888' \
    # b'Connection: keep-alive' \
    # b'Upgrade-Insecure-Requests: 1' \
    # b'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36' \
    # b'DNT: 1' \
    # b'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' \
    # b'Accept-Encoding: gzip, deflate, br' \
    # b'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8'
    request_line = request.splitlines()
    request_data = request_line[0]
    print(request_data)     # 此处需要解析请求

    # 解析后返回请求内容
    try:
        f = open('index.html', 'r')
        print("opened")
        data = f.read()
        response = b'HTTP/1.1 200 ok\r\n' + \
                   b'\r\n' + \
                   data.encode()
        connfd.send(response)
    except:
        request = b'HTTP/1.1 404 not found\r\n' + \
                  b'\r\n' + \
                  b'NOT Find page'
        connfd.send(request)
def main(ADDR):
    # 主程序
    # 套接字创建到绑定
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(6)
    print("Ready for accept from:", ADDR)

    # 接收并处理请求
    while True:
        connfd, address = sockfd.accept()
        hanlder_client(connfd)
        connfd.close()


if __name__ == "__main__":
    addr = ('127.0.0.1', 8000)
    main(addr)
