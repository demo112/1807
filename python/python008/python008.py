# 集合练习:
#   技术员有: 曹操,孙权,张飞,关羽
#   经理有: 曹操,刘备,孙权
#   用集合求:
#     1 即是经理，也是技术员的有谁?
#     2 是经理，但不是技术员的人员都有谁？
#     3 是技术员，不是经理的都有谁
#     4 张飞是经理吗？
#     5 身兼一职的人都有谁？
#     6 经理和技术员共有几个人?

# ma = {'曹操', '刘备', '孙权'}
# tec = {'曹操', '孙权', '张飞', '关羽'}
# print(ma & tec, '即是经理，也是技术员')
# print(ma - tec, '是经理，但不是技术员')
# print(tec - ma, '是技术员，不是经理')
# print('张飞', '张飞' in ma, '经理')
# print(tec ^ ma, '身兼一职')
# # s = {tec | ma}
# # print(s)
# print('共有%d人' % len(tec | ma))


# # Mysql_order 写一个函数myadd, 此函数中的参数列表里有两个参数x, y
# #     此函数的功能是打印 x + y 的和

# def myadd(x, y):
#     a = x + y
#     print(a)
# myadd(100, 200)
# myadd('ABC', '123')

# # print_even, n代表终止整数打印２～n之间的所有偶数

# def print_even(n):
#     for x in range(2, n + 1, 2):
#         # if x % 2 == 0:
#         #     print(x)
#         # else:
#         #     continue
#         print(x)
# print_even(100)


# def myadd2(x, y):
#     a = x + y
#     return(a)         # 返回给函数参数值
# a = int(input("请输入一个数："))
# b = int(input("请输入一个数："))
# print("您输入的两个数的和是：", myadd2(a, b))

# # print(s)    # 不可以　局部变量只会在函数内有用，函数执行结束后自动销毁



# # 写一个函数 mymax, 给函数传递两个参数，返回两个实参中最大的一个
# #     def mymax(a, b):
# #          ....

# #     v = mymax(100, 200)
# #     print('v =', v)  # v = 200
# #     print(mymax('ABC', 'abc'))  # abc
# def mymax(a, b):
#     if a > b:
#         m = a
#     else:
#         m = b
#     return m
# v = mymax(100, 200)
# print('v =', v)  # v = 200
# print(mymax('ABCD', 'ABC'))  # abc 

# # WAY2
# def mymax(a, b):
#     if a > b:
#        return a
#     return b
# v = mymax(100, 200)
# print('v =', v)  # v = 200
# print(mymax('ABCD', 'ABC'))  # abc 

# # WAY3
# def mymax(a, b):
#     return max(a,b)
# v = mymax(100, 200)
# print('v =', v)  # v = 200
# print(mymax('ABCD', 'ABC'))  # abc 



# # 2. 写一个函数 input_number
# #       def input_number():
# #           ....
# #       此函数用来获取用户循环输入的整数，
# #       当用户输入负数时结束输入。
# #       将用户输入的数字以列表的形式返回，
# #       再用内建函数max, min, sum取出户输入的
# #       最大值，最小值及和
# #       L = input_number()
# #       print(L)  # 打印此列表
# #       print("用户输入的最大数是:", max(L))
# #       print("用户输入的最小数是:", min(L))
# #       print("用户输入的数的和是:", sum(L))


# def input_number():
#     L =[]
#     while True:
#         a = int(input("请输入数字："))
#         if a >= 0:
#             L += [a]
#             # L.append(a)
#         else:
#             break
#             # return(L)
#     return(L)
# L = input_number()
# print("用户输入的最大数是:", max(L))
# print("用户输入的最小数是:", min(L))
# print("用户输入的数的和是:", sum(L))



# # Mysql_order 写一个函数 print_odd, 打印从begin开始，
# #     到end结束(不包含end)内的全部的奇数
# #       def print_odd(begin, end):
# #         print_odd(1, 10)  # 打印 1 3 5 7 9d
# #         ptint_odd(10, 20) # 打印 11 13 15 17 19

# def print_odd():
#     begin = int(input("请输入开始数字"))
#     end = int(input("请输入结束数字"))
#     for x in range(begin, end):
#         if x % 2 == 1:
#             print(x, end=' ')
#         else:
#             continue
#     print()
# print_odd()



# 2. 定义两个函数:
#       sum3(a, b, c) 用于返回三个数的和
#       pow3(x)  用于返回x的三次方
#       用以上函数计算:
#         Mysql_order 计算1的立方 + 2的立方 + 3的立方的和
#           即:  1**3 + 2**3 + 3**3的和 
#         2. 计算1 + 2 + 3 的和的立方,
#           即:(1+2+3)**3




# # 编写函数fun，　功能是：计算并返回下列多项式的值
# # Sn = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + .... 1/n
# # 函数如def fun(n):

# def fun(n):
#     n = int(input("请输入多项式个数"))
#     S = 0
#     for x in range(1, n + 1):
#         Sn = 1 / x
#         S += Sn
#     return(S)
# print(fun(n))


# fun2 
# Sn = 1/(1*2) + 1/(2*3) + ....+ 1/(n*(n+1))

# n = int(input("请输入多项式个数"))
# def fun2(n):
#     S = 0
#     for x in range(1, n + 1):
#         Sn = 1 / (x * (x + 1))
#         S += Sn
#     return(S)
# print(fun2(n))




# # 2. 写一个函数isprime(x) 判断x是否为素数，如果为素数，返回True,否则返回False
# #      如:
# #        print(isprime(5))  # True
# #        print(isprime(6))  # False
# x = int(input("请输入数字"))
def isprime(x):
    if x < 2:
        return False
    for a in range(2,x):
        if x % a == 0:
            return False
    else:
        return True
# print(isprime(x))


# 3. 写一个函数prime_m2n(m, n) 返回从m开始，到n结束范围内的素数，返回这些素数的列表，并打印．
#     如:
#       L = prime_m2n(10, 20)
#       print(L)  # [11, 13, 17, 19]

m = 10#int(input("请输入开始数字"))
n = 20#int(input("请输入结束数字"))
def prime_m2n(m, n):
    L = []
    for x in range(m, n):
        if isprime(x) is True:
            L += [x]
    return(L)
print(prime_m2n(m, n))


# 4. 写一个函数 primes(n)  返回指定范围内n(不包含n)的全部素数的列表，并打印这些列表
#     如:
#       L = primes(10)
#       print(L)  # [2, 3, 5, 7]
#     1) 打印100以内全部素数的和
#     2) 打印200以内全部素数的和
n = int(input("请输入数字范围"))
def prime(n):
        return prime_m2n(1, n)

print(prime(n))
print(sum(prime(100)))
print(sum(prime(200)))

# WAY2
# n = int(input("请输入数字范围"))
# def prime(n):
#     L = []
#     for x in range(1, n + 1):
#         for y in range(2,x):
#             if x % y == 0:
#                 break
#         else:
#             L += [x]
#     return(L)

# print(prime(n))
# print(sum(prime(100)))
# print(sum(prime(200)))



# # 5.  改写之前的学生信息管理程序，将其改为两个函数：
# #     def input_student():
# #           ...
# #     def output_student(L):
# #         ....
# #     input_student用于从键盘读取学生数据，形成列表并返回列表
# #     output_student(L) 用于将传和的列表L 打印成为表格
# #    测试代码：
# #      L = input_student()
# #      print(L)
# #      output_student(L)  # 打印表格

# def input_student():
#     Lst = []
#     while True:
#         name = input("请输入学生姓名：")
#         if name is '':                  #not n
#             break
#         else:
#             age = int(input("请输入学生年龄："))
#             score = int(input("请输入学生成绩："))
#             N = {'name': name, 'age': age, 'score': score}
#         Lst.append(N)
#     return(Lst)


# L = input_student()
# def output_student(L):
#     Lst = L
#     for s in Lst:
#         s = s['name']
#         long = [len([x for x in s if ord(x) > 127])]
#     a = max(long)
#     # print(a)
#     L = max(len(n['name']) for n in Lst) + a * 2 + 10
#     print('+' + '-' * (L - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
#     print(
#         '|' + 'name'.center(L - 2) +
#         '|' + 'age'.center(11) +
#         '|' + 'score'.center(11) +
#         '|')
#     print('+' + '-' * (L - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
#     for n in Lst:
#        # print(
#        #  '|' + n['name'].center(L - 2) +
#        #  '|' + str(n['age']).center(11) +
#        #  '|' + str(n['score']).center(11) +
#        #  '|')
#        print(
#         '|%s|%s|%s|' % (n['name'].center(L - 2 - a), str(n['age']).center(11), str(n['score']).center(11)))
#     print('+' + '-' * (L - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
# output_student(L)




