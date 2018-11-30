from socket import *

s = socket()

# 获取套接字地址族类型
print(s.family)

# 获取套接字类型
print(s.type)

# 获取套接字的绑定地址和端口
print(s.getsockname())

# 获取套接字的文件描述符
print(s.fileno())

# 获取客户端链接套接字的对应地址
print(s.getpeername())

# 设置套接字的选项值
print(s.setsockopt(level, option, value))

# 获取套接字的选项值
print(s.getsockopt(level, option))
