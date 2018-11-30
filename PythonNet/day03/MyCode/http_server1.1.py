from socket import *


def handleClient(connfd):
    request = connfd.recv(4096)
    request_lines = request.splitlines()
    for line in request_lines:
        print(line.decode())
    try:
        f = open("index.html", 'r')
    except IOError:
        response = "HTTP/1.1 404 not found\r\n"
        response += "\r\n"
        response += "=====Sorry not found======"
    else:
        response = "HTTP/1.1 200 ok\r\n"
        response += "\r\n"
        response += f.read()
    finally:
        connfd.send(response.encode())
        f.close()
    return

# 创建套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('127.0.0.1', 8888))
    sockfd.listen(6)
    print("listen to the port 8888")
    while True:
        connfd, addr = sockfd.accept()
        # 处理请求
        handleClient(connfd)
        connfd.close()

if __name__ == '__main__':
    main()