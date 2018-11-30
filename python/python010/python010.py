# # globals_locals.py
# a = 100#全局变量
# b = 200#全局变量

# def fn(c):#局部变量
#     d = 300#局部变量
#     a = 1000000
#     print(a, b, c, d)
# fn(300)
# print(a, b)

# #示例：
# 可以改变列表，不能改变变量
# L = []
# def input_number():
#     L2 = []
#     while True:
#         n = int(input('请输入正整数'))
#         if n < 0:
#             break
#         L2.append(n)
#     # L = L2
#     L.append(L2)        #改变变量绑定的对象
#     # L += L2             #报错，因为L是全局变量
# input_number()
# print()

# a = 1
# b = 2
# c = 3

# def fn(c, d):
#     e = 300
#     print("locals()返回：", locals())
#     print("globals()返回：", globals())
#     print(c)
#     print(globals()['c'])
# fn(100, 200)




# # function_variable.py
# #示意函数是一个变量，他绑定了一个函数对象
# def fn():
#     print("hello world")

# f1 = fn
# print(f1)           #<function fn at 0xXXXXXXXX>
# print(fn)           #<function fn at 0xXXXXXXXX>
# print(f1())         #  None
# def f1():
#     print("函数被f1调用")

# def f2():
#     print("函数被f2调用")

# f1, f2 = f2, f1
# f1()        #f2()被调用

# f2()        #f1()被调用

# # give_function_as_args.py
# # 函数作为另外一个函数的实参
# def f1():
#     print("函数被f1调用")

# def f2():
#     print("函数被f2调用")

# def fx(fn):
#     print(fn)
#     fn()

# fx(f1)
# fx(f2)
# -------------------------------------------------------------------------------------------------------
# Exm2：
# def myinput(fn):
#   L = [5, 3, 1, 9, 7]
#   return fn(L)

# print(myinput(max))
# print(myinput(min))
# print(myinput(sum))
# print(myinput(len))

# # 等同于：
# def make_number(fn):
#     print(fn(L))

# L = [5, 3, 1, 9, 7]
# make_number(max)
# make_number(min)
# make_number(sum)
# make_number(len)

# shiyan
# def make_number(fn):
#     for a in L:
#         for b in L2:
#             print(fn(a, b))

# L = [5, 3, 1, 9, 7]
# L2 = [5, 3, 1, 9, 7]
# make_number(pow)

# -------------------------------------------------------------------------------------------------------


# def goodbye(L):
#     for x in L:
#         print('再见', x)

# def hello(L):
#     for x in L:
#         print("你好", x)
# def do_things(fn, L):
#     fn(L)
# L = ['Tom', 'jerry', 'Spike']
# do_things(hello, L)#调用上面函数处理L中的内容

# -------------------------------------------------------------------------------------------------------
# １
# # return_function.py
# # 函数可以作为另一个函数的返回值

# def get_function():
#     s = input("请输入您需要的操作：")
#     if s == '求最大':
#         return max
#     elif s == '求最小':
#         return min
#     elif s == '求和':
#         return sum
# ２
# L = [2, 4, 6, 8, 10]
# f = get_function()　　# 让get_function返回给我们一个函数
# print(f(L))

# 数据
#     选择函数１（选择出来的处理数据的函数２）
# 呈现结果　＝　函数２处理数据


# 练习：
# 写一个计算公式的解释执行器：
# 已知有如下函数：
# def myadd(x,y):
#     return x + y
# def mysub(x,y):
#     return x - y
# def mymul(x,y):
#     return x * y
# def get_fun(op):
#     if op == '+' or op == "加":          # get_fun(op)函数传入字符串＂加＂或＂＋＂返回myadd
#         return myadd
#     elif op in ('-', '减'):        # get_fun(op)函数传入字符串＂乘＂或＂*＂返回mymul
#         return mysub
#     elif op == '*' or op == "乘":
#         return mymul
# # 也可以直接将上方的创建函数替换进来

# # 在主函数中的程序｀如下：
# def main():
#     while True:
#         s = input("请输入计算公式：")
#         L = s.split()                           # L = ['10', '加'，'20']
#         a = int(L[0])
#         b = int(L[2])
#         fn = get_fun(L[1])
#         print("结果是：", fn(a, b))
# main()

# -------------------------------------------------------------------------------------------------------
# function_embed_def.py
# 函数的嵌套
# def fn_outter():
#     print("fn_outter被调用")
#     def fn_inner():
#         print("fn_inner被调用")
#     fn_inner()
#     fn_inner()
#     print("fn_outter调用结束")
#     return fn_inner()
# fn_outter()
# L = fn_outter()
# L
# -------------------------------------------------------------------------------------------------------
# # namespace.py  python的四个作用域

# v = 100         #全局变量
# def fun1():
#     v = 200             #外部嵌套函数作用域：　对嵌套函数来说是全局变量，对外部来说是局部变量
#     print("fun.v=", v)
#     def fun2():
#         v = 300         #局部变量，当本变量不存在时函数自动向上查找
#         print("fun2.v=", v)
# fun1()
# print("全局变量v =", v)

# # -------------------------------------------------------------------------------------------------------
#  # global.py

# v = 100       
# def fu():
#     v = 200 
# fu()
# print("v =", v)     #100


# v = 100
# def fu():
#     global v         #global声明
#     v = 200
# fu()
# print("v =", v)     #200


# nonlocal 

















# -------------------------------------------------------------------------------------------------------
# lambda.py  
# def myadd(x, y):
#     return(x + y)
# 等同于

# myadd = lambda x, y: x + y
# #变量　＝　lambda形参　　：表达式

# print('20+30=', myadd(20, 30))
# print('40+50=', myadd(40, 50))

 # Mysql_order 写一个lambda 表达式，判断这个数的2次方+1是否能被5整除，如果能被整除返回True, 否则返回False
 #     例:
 #        fa = lambda x: .....
 #        print(fa(2))  # True
 #        print(fa(4))  # False


# jiou = lambda x: (x ** 2 + 1) % 5 == 0
# # jiou = lambda x: True if (x ** 2 + 1) % 5 == 0 else False
# print(jiou(4))
# print(jiou(2))

# def mymax(x, y):
#     if x >= y:
#         return x
#     else:
#         return y
# mymax = lambda x, y: x if x > y else y
# # mymax = lambda x, y: max(x, y)

# print(mymax(100, 200))
# 有问题
# 有问题
# 有问题
# 有问题
# 有问题
# 有问题

# 有问题
# 有问题有问题
# 有问题
# 有问题
# 有问题
# 有问题

# def mymax(f, x, y):
#     print(f(x, y))
# mymax = ((lambda x, y:x if x > y else y), 100, 200)


# 看懂下面的函数
# def fn(f, x, y):
#     print(f(x, y))

# fn(lambda a, b: a + b, 100, 200)

# fn (lambda a, b: a ** b, 100, 200)
# -------------------------------------------------------------------------------------------------------
# eval示例见:
#    eval.py
#    eval2.py

# exec 示例见:
#   exec.py
# 补全示例


# -------------------------------------------------------------------------------------------------------
# 练习：

# def myfac(n):
#     s = 1
#     for x in range(1, n + 1):
#         s *= x
#     return(s)

# def factorial(n):
#     if n < 1:
#         return 1
#     else:
#         return factorial(n - 1) * n
# print(myfac(100))
# print(factorial(100))


# def myfn(n):
#     s = 0
#     for x in range(1, n + 1):
#         s += (x ** x)
#     return(s)
# print(myfn(3))

# def ou(d, x):
#     d2 = [1, 1]
#     for y in range(1, x + 1):
#         d2[y:y] = [d[y - 1] + d[y]]
#     return d2


# 杨辉三角

def yang(n):
    Lst = [[1], [1, 1]]
    d = []
    for x in range(n):
        d = Lst[x]
        Lst += [ou(d, x)]
    return(Lst)
# print(yang(6))
def ou(d, x):
    d2 = [1, 1]
    for y in range(1, x + 1):
        d2[y:y] = [d[y - 1] + d[y]]
    return d2

def yang(n):
    Lst = [[1], [1, 1]]
    d = []
    for x in range(1, n - 1):
        d = Lst[x]
        Lst += [ou(d, x)]
    return(Lst)
# print(yang(n))

def p(Lst, n):
    for a in range(0, n):
        hang = Lst[a]
        print(' ' * ((n - a)), end='')
        for b in range(0, a + 1):
            ge = hang[b]
            print(ge, '', end='')
        print()


def main():
    n = 6#int(input("LINE"))
    Lst = yang(n)
    p(Lst, n)
main()
