# ----------------------------------------------------
# 函数装饰器
# ---------------------------------------------------
# def mydeco(fn):
#     def fx():
#         print("fx被调用")
#     return fx
#
# @mydeco
# def myfun():
#     print("myfun被调用")
# #在mufun被调用以后，在下边加上了一个
# #myfun = mydeco(mufun)
#
# myfun()
# myfun()
# myfun()


# exmple
# ===================================
# 小李写的装饰器--权限验证
# # ===================================
# def privileged_check(fn):
#     def fx(name, x):
#         print('正在验证权限')
#         if True:
#             fn(name, x)
#         else:
#             print('验证权限失败')
#     return fx
#
#
#
# # ===================================
# # 小李写的装饰器--发送短信
# # ===================================
# def message_send(fn):
#     def fy(n, money):
#         fn(n, money)
#         print("正在发送短信给", n, '......')
#     return fy
# # ===================================
# # 老魏写的
# # ===================================
# @message_send
# @privileged_check
# def savemoney(name, x):
#     print(name, '存钱', x, '元')
# # 实质是
# # savemoney = privileged_check(savemoney)   fx
# # savemoney = message_send(savemoney)       fy
# @privileged_check
# def withdraw(name, x):
#     print(name, '取钱', x, '元')
# # ===================================
# # 小张写的
# # ===================================
# savemoney('小王', 200)
# savemoney('小赵', 400)
# withdraw('小李', 500)
# # ===================================









# ----------------------------------------------------
# 面试题
# ---------------------------------------------------
# L = [1, 2, 3]
# def f(n=0, lst=[]):
#     lst.append(n)
#     print(lst)
#
# f(4, L)
# f(5, L)
# f(100)
# f(200)

# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [100]
# [100, 200]













# ----------------------------------------------------
# import.py
# ---------------------------------------------------
# import math, sys, time, os             #导入数学模块
# print(dir(math))
# print(math.factorial(5))            #阶乘
#
#
# print(math.cos(0))
# print(math.pi)
# print(time.actime)



# 练习:
#   Mysql_order 输入一个圆的半径，打印出这个圆的面积
#   2. 输入一个圆的面积，打印出这个圆的半径

# import math
# def sq(r):
#     sq = math.pi * r ** 2
#     return sq
# def r(sq):
#     r = math.sqrt(sq / math.pi)
#     return r
# print(sq(10))
# print(r(314))

# from math import pi as pi
# from math import sqrt as sqrt
# def sq(r):
#     sq = pi * r ** 2
#     return sq
# def r(sq):
#     r = sqrt(sq / pi)
#     return r
# print(sq(10))
# print(r(314))
# ----------------------------------------------------

# ---------------------------------------------------
# # 写一个程序，输入你的出生日期，
# #     1) 算出你已经出生多少天?
# #     2) 算出你出生的那天是星期几?
# from time import *
# year = int(input("请输入年份："))
# mouth = int(input("请输入月份："))
# day = int(input("请输入日期："))
# hour = int(input("请输入小时：") or '0')
# T = (year, mouth, day, hour, 15, 0, 0, 0, 0)
# def days(T):
#     s = time() - mktime(T)
#     d = localtime(mktime(T))
#     d = d[6] + 1
#     ds = s / 60 / 60 // 24
#     return d, ds
# s = days(T)
#
# print('那天是周', s[0], '过了', s[1], '天')













# ----------------------------------------------------
# 课后练习
# ---------------------------------------------------
# from math import *
# def s(n):
#     s = 1 / factorial(n)
#     return s
# def main(n):
#     S = 1
#     for m in range(1, n):
#         S += s(m)
#     return S
# print(main(10000000))


#
# 2. 写一个程序，以电子时钟格式:
#     HH:MM:SS格式显示时间
#     要求每隔一秒变化一次
#
from time import localtime
from time import sleep
from time import time
from time import time
from time import mktime
from time import asctime
# def show_time():
#     s = int(time())
#     # S = s % 60
#     # M = s // 60 % 60
#     # H = s // 3600 % 24 + 8
# # WAY2
#     s = int(time())
#     Local = localtime(s)
#     H = Local[3]
#     M = Local[4]
#     S = Local[5]
#     # print(Local)
#     return H, M, S
# # print(show_time())
# def watch():
#     while True:
#         L = show_time()
#         H = L[0]
#         M = L[1]
#         S = L[2]
#         # n = input('%s : %s : %s' % (H, M, S))
#         # n = '%02s : %02s : %02s' % (H, M, S)
#         # n = '%02d : %02d : %02d' % L[0:3]
#         # print(n)
#         print('%02d : %02d : %02d' % L[0:3])  #为什么这样不可以
#         sleep(1)
# watch()

#     设置一个闹钟，启动时设定时间，到时间后打印一句时间到
# def bettwen():
#     h = int(input('请输入时'))
#     m = int(input('请输入分'))
#     s = int(input('请输入秒'))
#     now = localtime(time())
#     # print(now)
#     set = mktime((now[0], now[1], now[2], h, m, s, 0, 0, 0))
#     # print(set)
#     b = set - time()
#     return b
# # print(bettwen())
# def clock():
#     sleep(bettwen())
#     print('时间到了')

# clock()

# way2
# from time import *
# def alarm(h, m):
#     while True:
#         t = localtime(time())
#         # print(t)
#         print('%02d : %02d : %02d' % t[3:6], end='\r')
#         sleep(1)
#         # if h == t[3] and m == t[4]:
#         if (h, m) == t[3:5]:
#             print('\n时间到')
#             break
#
# h = int(input('请输入时'))
# m = int(input('请输入分'))
# alarm(h, m)



# ----------------------------------------------------

# ---------------------------------------------------
l = [1, 2, 3]


def f(n=0, lst=[]):
    lst.append(n)
    print(lst)


f(4, l)  # [1, 2, 3, 4]
f(5, l)  # [1, 2, 3, 4, 5]
f(100)   # [100]
f(200)  # [100, 200] 打印结果是什么,为什么?

print(__doc__)










# ----------------------------------------------------

# ---------------------------------------------------

















# ----------------------------------------------------

# ---------------------------------------------------

















# ----------------------------------------------------

# ---------------------------------------------------

















# ----------------------------------------------------

# ---------------------------------------------------

















# ----------------------------------------------------

# ---------------------------------------------------

















# ----------------------------------------------------

# ---------------------------------------------------

















