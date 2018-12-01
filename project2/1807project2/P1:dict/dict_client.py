#!/usr/bin/python3
# coding=utf-8


"""
    Data:20180928
    name:cooper
    email:huafengodngji@hotmail.com
    model:Pymysql
"""


from socket import *
import sys
import getpass


# 创建网络连接
def main():
    """
        客户端主程序：
        1、解析命令行参数
    :return:
    """
    # 命令行参数 argv[0]代表当前脚本程序路径名
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    s = socket()
    # 查找服务端并链接
    try:
        s.connect((HOST, PORT))
    except Exception as e:
        print(e)
        return
    mule(socket)


def mule(s):
    """
        根据用户输入指令
        调用不同程序
        向服务端发送请求
        处理收到信息输出
        对应do_child()
    """
    while True:
        print("""
        ========welcome=========
        --1.注册
        --2.登陆
        --3.退出
        """)
        try:
            cmd = int(input("输入选项>>"))
        except Exception as e:
            print("命令错误", e)
            continue

        if cmd not in [1, 2, 3]:
            print("请输入正确选项")
            sys.stdin.flush()       # 清除标准输入
            continue
        elif cmd == 1:
            r = do_register(s)
            if r == 0:
            # if name:
                print("注册成功")
                # login(s,name)  #进入二级界面
            elif r == 1:
                print("注册失败：用户存在")
            else:
                print("注册失败")
        elif cmd == 2:
            name = do_login(s)
            if name:
                print("登录成功")
                login(s, name)
            else:
                print("用户名或密码不正确")
        elif cmd == 3:
            s.send(b'E')
            sys.exit("谢谢使用")


def do_register(s):
    while True:
        name = input("User:")
        passwd = getpass.getpass()
        passwd2 = getpass.getpass('Again:')

        if (' ' in name) or (' ' in passwd):
            print("用户名和密码不允许有空格")
            continue
        if passwd != passwd2:
            print("两次密码不一致")
            continue

        msg = 'R {} {}'.format(name, passwd)
        # 发送请求
        s.send(msg.encode())
        # 等待回复
        data = s.recv(128).decode()
        if data == 'OK':
            return 0
        elif data == 'EXISTS':
            return 1
        else:
            return 2


def do_login(s):
    """登陆申请"""
    name = input("User:")
    passwd = getpass.getpass()
    msg = "L {} {}".format(name, passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()

    if data == 'OK':
        return name
    else:
        return


def login(s, name):
    """登陆二级界面"""
    if name:
        print("登陆成功")
    while True:
        print("""
            =========字典========
            --1.查词
            --2.查询历史
            --3.退出
            ====================
            """)
        try:
            cmd = int(input("输入选项>>"))
        except Exception as e:
            print("命令错误", e)
            continue

        if cmd not in [1, 2, 3]:
            print("请输入正确选项")
            sys.stdin.flush()  # 清除标准输入缓冲区
            continue
        elif cmd == 1:
            do_query(s, name)
        elif cmd == 2:
            do_hist(s, name)
        elif cmd == 3:
            return


def do_query(s, name):
    while True:
        word = input('单词:')
        if word == '##':
            break
        msg = "Q {} {}".format(name, word)
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data == "OK":
            data = s.recv(2048).decode()
            print(data)
        else:
            print("没有查询到该单词")


def do_hist(s, name):
    msg = "H {}".format(name)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == "##":
                break
            print(data)
    else:
        print("客户端没有查询到历史记录")
    pass


if __name__ == "__main__":
    main()
