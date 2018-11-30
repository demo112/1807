from socket import *


# 创建套接字
prepare = socket(AF_INET, SOCK_STREAM)
# 绑定服务端地址
prepare.bind(('0.0.0.0', 8888))
# 设置监听套接字
prepare.listen(5)
# 等待客户端链接
print('Waiting for input...')
user_input, add = prepare.accept()
# 消息收发
# 设置传入字符的长度
data = user_input.recv(2048)         # 此处输出位字节串
# 转换为字符串
print(data.decode(), add)

# 返回客户端信息
n = user_input.send(b'Already get your message')
# 关闭套接字
prepare.close()
user_input.close()
