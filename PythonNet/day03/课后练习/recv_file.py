import time
from socket import socket

def link_in(ADDR):
    s = socket()
    s.bind((ADDR[0], ADDR[1]))
    s.listen(5)
    return s


def recv_file(sockfd):
    c, addr = sockfd.accept()
    f = open('recv.jpg', 'wb')
    while True:
        data = c.recv(1024)
        if data == b'##':
            break
        f.write(data)
    close(f, c, sockfd)


def close(file, connfd, sockfd):
    file.close()
    connfd.close()
    sockfd.close()


def get_addr(HOST='127.0.0.1', PORT=8888):
    ADDR = (HOST, PORT)

    return ADDR

def main():
    addr = get_addr()
    sockfd = link_in(addr)
    recv_file(sockfd)


if __name__ == "__main__":
    main()
