#!/usr/bin/python3
# coding=utf-8


"""
    Data:20180928
    name:cooper
    email:huafengodngji@hotmail.com
    model:Pymysql
"""


import os
import time
import signal
import pymysql
import sys
from socket import *


# 定义需要的全局变量
DICT_TEXT = './P1:dict.txt'
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)


# 主程序控制
def main():
    """
        数据库主程序：
        1、创建数据库TCP连接
        2、忽略子进程信号，避免僵尸进程
        3、等待接收客户端链接
        4、解析链接请求，创建子进程处理请求
    """
    # 创建数据库连接
    db = pymysql.connect(
        'localhost', 'root', '', 'P1:dict')

    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   # 防止套接字占用端口

    try:
        s.bind(ADDR)
    except OSError:
        s.close()
        e = "%s 端口已占用,请重启原服务器" % (PORT,)
        sys.exit(e)

    s.listen(5)
    print("服务器已启动")

    # 忽略子进程信号，用于避免🧟‍♀僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        try:
            c, addr = s.accept()
            """accept() -> (socket object, address info)
            Wait for an incoming connection.  Return a new socket
            representing the connection, and the address of the client.
            For IP sockets, the address info is a pair (hostaddr, port).
            """
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 创建子进程
        pid = os.fork()
        if pid == 0:
            print("服务器创建子进程：准备处理请求")
            s.close()
            do_child(c, db)
        else:
            c.close()
            continue


def do_child(c, db):
    """
        循环接收客户端请求
        对应mule()
    """
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), ":", data)
        if (not data) or (data[0] == "E"):
            c.close()
            sys.exit(0)
        elif data[0] == "R":
            do_register(c, db, data)
        elif data[0] == "L":
            do_login(c, db, data)
        elif data[0] == "Q":
            do_query(c, db, data)
        elif data[0] == "H":
            do_hist(c, db, data)


def do_login(c, db, data):
    print("登陆操作")
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user where name='%s' and passwd='%s'" % (name, passwd)
    cursor.execute(sql)
    r = cursor.fetchone()

    if r is None:
        c.send(b'FAll')
    else:
        print("%s登陆成功" % name)
        c.send(b"OK")


# noinspection PyBroadException
def do_register(c, db, data):
    print("注册操作")
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user where name='%s'" % name
    cursor.execute(sql)
    r = cursor.fetchone()

    if r is not None:
        c.send(b'EXISTS')
        print("用户已存在")
        return

    # 用户不存在插入用户
    sql = "insert into user (name, passwd) values('%s', '%s')" % (name, passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        db.rollback()
        c.send(b'FALL')
    else:
        print("%s注册成功" % name)


# noinspection PyBroadException
def do_query(c, db, data):
    print("查询操作")
    l = data.split(' ')
    name = l[1]
    word = l[2]
    cursor = db.cursor()
    print('打开数据库')

    # noinspection PyBroadException
    def insert_history():
        tm = time.ctime()
        sql = "insert into hist (name, word, time) values('%s', '%s', '%s')" % (name, word, tm)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    # 文本查询
    try:
        print('翻开字典，开始查词')
        f = open(DICT_TEXT)
    except:
        c.send(b'FALL')
        return

    for line in f:
        tmp = line.split(' ')[0]    # 以空格分割行
        if tmp > word:
            c.send(b"Server FALL")
            f.close()
            return
        elif tmp == word:
            c.send(b'OK')
            time.sleep(0.1)
            c.send(line.encode())
            f.close()
            insert_history()
            return
    c.send(b"Server FALL")
    f.close()


def do_hist(c, db, data):
    print("历史记录")
    l = data.split(' ')
    name = l[1]
    cursor = db.cursor()
    sql = "select * from hist where name='%s' limit(10)" % name
    cursor.execute(sql)
    r = cursor.fetchall()
    if not r:
        c.send(b'FALL')
        return
    else:
        c.send(b"OK")

    for i in r:
        time.sleep(0.1)
        msg = "%s %s %s" % (i[1], i[2], i[3])
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b'##')


if __name__ == '__main__':
    main()
