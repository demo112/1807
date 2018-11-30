# # position_give_args.py
# 位置传参
# def myfun(a, b, c):
#     print('a的值是', a)
#     print('b的值是', b)
#     print('c的值是', c)
# myfan(1, 2, 3)
# myfan(1, 2, 3)
# myfan(1, 2, 3)


# # sequence_give_args.py
# # 序列传参：
# def myfun(a, b, c):
#     print('a的值是', a)
#     print('b的值是', b)
#     print('c的值是', c)

# s1 = [11, 22, 33]
# s2 = (44, 55, 66)
# s3 = 'ABC'
# # myfun(s1)     #wrong
# myfun(*s1) == myfun(s1[0], s1[1], s1[2])
# myfun(*s2) == myfun(s2[0], s2[1], s2[2])
# myfun(*s3) == myfun(s3[0], s3[1], s3[2])




# keywords_give_args.py
# 关键字传参

# def myfun(a, b, c):
#     print('a的值是', a)
#     print('b的值是', b)
#     print('c的值是', c)
# myfun(c=33, b=22, a=11)
# 无所谓顺序


# dict_keywords_give_args.py
# 字典关键字传参

# def myfun(a, b, c):
#     print('a的值是', a)
#     print('b的值是', b)
#     print('c的值是', c)
# d1 = {'c': 300, 'b': 200, 'a': 100}
# mufun(**d1) == myfun(a = d1['a'], b = d1['b'], c = d1['c'])


# 练习：写一个函数getminmax(a, b, c)有三个参数，这回这三个参数中的最小值和最大值，
#   要求，形成元组，最小值在前，最大值在后
#   形成元组后返回
#     格式（最小值，　最大值）

# # 可以尝试上述传参方式

# def getminmax(a, b, c):
#     return(tuple([min(a, b, c), max(a, b, c)]))

# # WAY1
# print(getminmax(100, 1, 500))
# # WAY2
# def getminmax(a, b, c):
#     xiao = min(a, b, c)
#     da = max(a, b, c)
#     return xiao, da
# # WAY3
# a = int(input("请输入"))
# b = int(input("请输入"))
# c = int(input("请输入"))
# t = getminmax(a, b, c)
# print(t)

# # WAY4
# L = []
# for i in range(1, 4):
#     L.append(int(input('请输入第%d个数' % i)))
# t = getminmax(*L)
# print(t)
# print('最小数是:%d, 最大数是：%d' % t)

# # WAY5序列赋值
# L = []
# for i in range(1, 4):
#     L.append(int(input('请输入第%d个数' % i)))
# t = getminmax(*L)
# x, y = t
# print(x)
# print(y)



# # efault_args.py
# def info(name, age=1, address='不详'):
#     print('我叫', name, '我今年', age, '岁，我的地址：', address)


# i = info('cooper', 35, '北京')
# i = info('TAREna', 35)              #　缺省参数
# i = info('张飞')
# print(i)




# def myrange(a, b=None, c=1):
#     if b is None:          #if b is None:
#         b = a
#         a = 0
#     L = []
#     x = a
#     if c > 0:
#         while a <= x < b:
#             L += [x]
#             x += c
#     elif c < 0:
#         while b < x <= a:
#             L += [x]
#             x += c
#     return(L)
# print(myrange(5))
# print(myrange(5, 10))
# print(myrange(5, 10, 2))
# print(myrange(10, 0, -2))


# # star_tuple_args.py
# # 星号元组传参
# def func(*args):
#     print("实参的个数是", len(args))
#     print('args=', args)
# func(1, 2, 3, 4, 6)
# func()

# # 和位置传参结合
# def func(a, b, *args):
#     print('a=', a)
#     print('b=', b)
#     print("实参的个数是", len(args))
#     print('args=', args)
# func(1, 2, 3, 4, 6)
# func()



# # 写一个函数 myadd, 此函数可以计算两个数的和,也可以计算三个数的和

# def myadd_plus(*L):
#     s = 0
#     for x in L:
#         s += x
#     print(s)
# myadd_plus(1, 2, 3, 4, 5, 6)
# myadd_plus(20, 1, 321, 132)




# 制作高仿max语句：
# 写一个函数，mymax类似于 内键的函数max
#   详见:
#     >>> help(max)
#  仿造 max 写一信mymax函数，功能与max完全相同
#  (要求不允许调用max函数)
#  print(mymax([6, 8, 3, 5]))  # 8
#  print(mymax(100, 200))  # 200
#  print(mymax(1, 3, 5, 9, 7))  # 9
# way1
# def mymax(a, *m):
#     if not m:
#         for p in a:
#             L.append(p)
#     else:
#         L += [a]

#     for x in m:
#         L.append(x)
#     z = L[0]
#     for y in L:
#         if y >= z:
#             da = y
#             z = y
#     return(da)
# print(mymax([993, 33, 314, 1]))
# print(mymax((993, 33)))
# print(mymax(993, 33, 314, 1))
# WAY2
# def mymax(a, *m):
#     if not m:
#         z = a[0]
#         for y in a:
#             if y >= z:
#                 z = y
#         return(z)
#     else:
#         z = a
#         for y in m:
#             if y >= z:
#                 z = y
#         return(z)
# print(mymax([993, 33, 314, 1]))
# print(mymax((993, 33)))
# print(mymax(993, 33, 314, 1))
# WAY3
# def mymax(a, *m):
#     if not m:
#         z = a[0]     
#     else:
#         z = a
#     for y in m:
#         if y >= z:
#             z = y
#     return(z)
# print(mymax([993, 33, 314, 1]))
# print(mymax((993, 33)))
# print(mymax(3, 33, 314, 1))




