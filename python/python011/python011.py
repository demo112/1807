# -*- coding:utf-8 -*-
# day11随堂练习


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # 函数式编程

# # WAY1
# def mysum(n):
#     s = 0
#     for x in range(1, n + 1):
#         s += x
#     print(s)
# # WAY2
# def mysum(n):
#     print(sum(range(1, n + 1)))     #可重入函数

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1**3 + 2**3 + 3 ** 3 + .... 9**3 的和
# def each_one(a):
#     return a ** 3
# s = 0
# for x in map(each_one, range(10)):
#     s += x
# print(s)
# WAY2
# print(sum(map(lambda x: x ** 3, range(1, 10))))

# # 1**4 + 2**4 + 3 ** 4 + .... 20**4 的和
# def each_one(a):
#     return a ** 4
# s = 0
# for x in map(each_one, range(21)):
#     s += x
# print(s)
# 拓展
# # 1**1 + 2**2 + 3 ** 3 + .... 9**9 的和
# def each_one(a, b):
#     return a ** b
# s = 0
# n = 4
# for x in map(each_one, range(n), range(n)):
#     s += x
# print(s)







# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# # 生辰一个可迭代对象，此刻迭代对象可以提供１　＊＊　４，　２　＊＊　３，　３　＊＊　２，　４　＊＊　１
# L = []
# def mypow(a, b):
#     return a ** b
# for i in map(mypow, [1, 2, 3, 4], [4, 3, 2, 1]):
#     print(i)

# # WAY2
# for i in map(pow, [1, 2, 3, 4], [4, 3, 2, 1], range(5, 100)):
#     print(i)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 求 1**9 + 2**8 + 3**7 + ...... 9**1的和

# print(sum(map(lambda a, b: a ** b, range(1, 10), range(9, 0, -1))))
# print(list(range(9, 0, -1)))
# print(sum(range(10)))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# filter函数：　
# filter.py
# 示例：
# def isodd(x):
#     return x % 2 == 1
# for x in filter(isodd, range(10)):
#     print(x)

# WAY2
# def isodd(x):
#     return x % 2 == 1
# L = list(filter(isodd, range(10)))
# print(L)

# 练习：
# Mysql_order 将 1 ～　２０　的偶数用filter生成可迭代对象后
#    将可迭代对象生成的数放入到列表L中

# def iseven(x):
#     return x % 2 == 0
# L = []
# for x in filter(iseven, range(1, 21)):
#     L.append(x)
#     # L += [x]
# print(L)

# # # WAY2
# print(list(filter(lambda x: x % 2 ==0, range(1, 21))))

# # # WAY3
# def iseven(x):
#     return True if x % 2 ==0 else False
# print(list(filter(iseven, range(1, 21))))


# # 2.写一个函数is_prime(x) 判断x是否是素数
# #     用filter函数打印出: 20 ~ 30之间的全部素数

# def isprime(x):
#     if x < 2:
#         return False
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#     return True
# L = list(filter(isprime, range(100)))
# print(L)
# # ！！！！！！！！！
# #　拓展求素数的算法


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# sorted 函数
# sorted.py
# 示例

# L = [5, -2, -4, 0, 3, -1]
# L2 = sorted(L)
# L3 = sorted(L, reverse=True)
# L4 = sorted(L, key=abs, reverse=False)
# print(L)
# print(L2)
# print(L3)
# print(L4)

# 按名字长度排续
# names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# L6 = sorted(names)
# L7 = sorted(names, key=len, reverse=False)
# print(L6)
# print(L7)

# 练习：
 # names = ['Tom', 'Jerry', 'Spike', 'Tyke']
 #  排序的依据为字符串的反序:
 #           # 'moT'   yrreJ    ekipS    ekyT
# names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# def back(w):
#     new_w = []
#     L = []
#     new_L = []
#     L = [x for x in w]
#     L.reverse()
#     # new_L = L
#     # new_w = ''.join(new_L)
#     # return new_w
#     return L         #WAY2

# def keyy(a):
#     for y in names:
#         back(y)
#     return back(y)

# L2 = sorted(names, key=back)
# print(L2)

# WAY2
# names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# def k(s):
#     return s[::-1]
# L = sorted(names, key=k)


# 调试：

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# recursion.py   递归函数 recursion

# def f():
#     print("从前有座山，山里有座庙，庙里有个老和尚讲故事")
#     f()  # 调用自己
# print("开始讲故事")
# f()
# print("递归完成")

# 示例：
    # 限制递归层数
# def fx(n):
#     print('递归进入第：', n, "层" )
#     if n == 3:
#         return
#     fx(n + 1)
#     print('递归退出第：', n, "层" )
# fx(1)
# print("递归结束")

# # 解释：相当于
# def fx(1):
#     print('递归进入第：', 1, "层" )
#     if n == 3:
#         return
#     fx(1 + 1)
#     -------------------------------------
#         fx(1 + 1):
#         print('递归进入第：', 2, "层" )
#         if 2 == 3:
#             return
#         fx(2 + 1)
#         ---------------------------------
#             fx(2 + 1)
#             fx(n):
#             print('递归进入第：', 3, "层" )
#             if n == 3:
#               return
#         ---------------------------------
#         print('递归退出第：', 2, "层" )
#     -------------------------------------
#     print('递归退出第：', 1, "层" )
# fx(1)
# print("递归结束")


# recurtion
# def myfac(n):
#     s = 1
#     for i in range(1, n + 1):
#         s *= i
#     return s

# print(myfac(5))
# print(myfac(100))


# # 用递归来实现
# def myfac(n):
#     if n == 1:              #先给出结束条件
#         return 1
#     # print(n, '*', (n - 1), '!')   #展示过程
#     return n * myfac(n - 1) #返回结果

# print(myfac(5))
# print(myfac(50))



# 用递归来实现求和
# def mysum(n):
#     if n == 1:
#         return 1
#     return n + mysum(n - 1)
# print(mysum(998))





# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 闭包  closure.py
# def make_power(y):
#     def fn(x):
#         return x ** y
#     return fn

# pow2 = make_power(2)        #实际上pow2调用的是fn（x）
# print(pow2(5))


# closure2.py

# 用闭包来创建任意的函数
# f(x) = ax2 + bx + c

# def get_fx(a, b, c):
#     def fx(x):
#         return a * x ** 2 + b * x + c
#     return fx
# f123 = get_fx(1, 2, 3)
# print(f123(10))
# print(f123(20))

# f654 = get_fx(6, 5, 4)
# print(f654(10))
# print(f654(20))


# def age(n):
#     if n == 1:
#         return 10
#     return 2 + age(n - 1)

# print(age(5))
# print(age(3))


# 2. 已知有列表:
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数print_list(lst) 打印出所有元素
#       print(L)  # 打印 3 5 8 10 13 14 ....
#       type(x) 可以返回一个变量的类型
#       如:
#          >>> type(20) is int # True
#          >>> type([1, 2, 3]) is list # True

# L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# def print_list(L):
#     L2 = []
#     for x in L:
#         if type(x) is int:
#             L2 += [x]
#         else:
#             L2 += print_list(x)
#     return L2 
# print(print_list(L))


# 2) 写一个函数sum_list(lst) 返回这个列表中所有元素的和
#       print(sum_list(L))  # 86
#
L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
def print_list(L):
    L2 = []
    for x in L:
        if type(x) is int:
            L2 += [x]
        else:
            L2 += print_list(x)
    return L2
def sum_list(lst):
    s = 0
    for x in lst:
        s += x
    return s
def main(L):
    lst = print_list(L)
    Sum = sum_list(lst)
    return Sum
print(main(L))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# # 算出1～20阶乘的和
# def mysum(n):
#     if n == 1:
#         return 1
#     return n + mysum(n - 1)
# def jiecheng(m):
#     if m == 1:
#         return 1
#     return m * jiecheng(m - 1)
# m = 4
# # s = 0
# # for x in map(jiecheng, range(1, m + 1)):
# #     s += x
#
# s = sum(map(jiecheng, range(1, m + 1)))
# print(s)











