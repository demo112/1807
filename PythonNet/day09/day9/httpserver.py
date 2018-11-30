from socket import * 

#httpserver基本功能
#接收http请求，查看，返回一个页面
def handleClient(connfd):
    request = connfd.recv(4096)
    print("***************")
    print(request)
    print("***************")

    f = open('index.html','r')
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html\r\n"
    response += "\r\n"
    response += f.read() 
    connfd.send(response.encode())


sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8000))
sockfd.listen(5)
while True:
    print("Listen the port 8000...")
    connfd,addr = sockfd.accept()
    handleClient(connfd)
    connfd.close()