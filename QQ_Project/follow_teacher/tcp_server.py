#!/usr/local/bin/python3.7
# coding=utf-8
"""
    文档说明

    name:cooper
    email:huafengdongji@hotmail.com
    data: 2018/09/11
    class: AID1807
    introduce:
        Chatroom server
    env: python3.7
"""
import os
import sys
from socket import *
name_dir = {}


def do_login(s, user, name, addr):
    """登陆判断"""
    if (name in user) or name == '管理员':
        s.sendto('给用户名已存在'.encode(), addr)
        return
    s.sendto('OK'.encode(), addr)
    # 通知其他人
    msg = '欢迎%s加入' % name
    for i in user:
        s.sendto(msg.encode(), user[i])
        user[name] = addr
    return name_dir


def do_chat(s, user, name, text):
    msg = '%s 说： %s' % (name, text)
    for i in user:
        if i != name:
            s.send(msg.encode(), user[i])

# 退出聊天室
def do_quit(s, user, name):
    msg = name + "退出了聊天室"
    for i in user:
        if i == name:
            s.sendto('EXIT')
        else:
            s.sento(msg.encode(), user[i])
    # 从字典中删除用户
    del user[name]

def do_child(s, addr):
    """管理员喊话"""
    while True:
        msg = input('管理员消息')
        msg = 'C 管理员 ' + msg
        s.sendto(msg.encode(), addr)


def do_parent(s):
    """接收客户端请求"""
    user = {}
    while True:
        msg, addr = s.recvfrom(1024)
        msglist = msg.decode().split(' ')
        # 区分请求类型
        if msglist[0] == 'L':
            do_login(s, user, msglist[1], addr)
        elif msglist[0] == 'C':
            do_chat(s, user, msglist[1], ' '.join(msglist[2:]))
        elif msglist[0] == 'Q':
            do_quit(s, user, msglist[1])

    # print('this is do parent')
    # pass


# 创建网络，创建进程，调用功能函数
def main():
    # sever address
    ADDR = ('0.0.0.0', 8888)
    # 创建数据报套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    # 创建一个新的进程，处理管理员喊话功能
    pid = os.fork()
    if pid < 0:
        sys.exit('创建进程失败')
    elif pid == 0:
        do_child(s, ADDR)
    else:
        do_parent(s)



if __name__ == "__main__":
    main()
