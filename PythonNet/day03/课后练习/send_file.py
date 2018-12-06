import time
from socket import socket

def get_addr(HOST='127.0.0.1', PORT=8888):
    ADDR = (HOST, PORT)
    return ADDR


def link_in():
    s = socket()
    addr = get_addr()
    s.connect(addr)
    return s


def close(file, sockfd):
    file.close()
    sockfd.close()
    print('发送结束')

def send_file():
    sockfd = link_in()
    f = open('send.jpg', 'rb')
    while True:
        data = f.read(1024)
        if not data:
            time.sleep(0.1)
            sockfd.send(b'##')
            break
        else:
            sockfd.send(data)
    close(f, sockfd)

def main():
    send_file()


if __name__ == "__main__":
    main()
