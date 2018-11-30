# #!/usr/bin/python3

# a = input('输入')
# b = input('输入')
# c = input('输入')


# print('% 20s' % a)
# print('% 20s' % b)
# print('% 20s' % c)

# #以最长字符串为宽度
# # 方法一
# d = max(len(a), len(b), len(c))
# print(d)
# print(" " * (d - len(a)) + a)
# print(" " * (d - len(b)) + b)
# print(" " * (d - len(c)) + c)

# # 方法二
# fmt = "%" + str(d) + "s"     # 为什么一定要用str　不能用　int
# print(fmt % a)
# print(fmt % b)
# print(fmt % c)

# 循环语句　　　#没有这一句的化会一直循环
# i = 1
# while i <= 100:
#     print("hello!", i)
#     i += 1
# else:
#     print("i=", i)

# i = 1
# while i <= 20:
#     print(i)
#     i += 1
# else:
#     print("i=", i)


# i = 1
# while i <= 20:
#     print(i, end = " ")
#     i += 1
# else:
#     print()

# i = 1
# n = 1
# while i <= 200:
#     while n <= 5:
#         print(i, end = " ")
#         n += 1
#         i += 1
#     else:
#         print()
#         n = 1


# i = 1
# while i <= 20:
#     print(i, end = " ")
#     i += 1
#     if i % 5 == 1:
#         print()

# i = 10
# while i >= 1:
#     print(i, end = " ")
#     i -= 1
# else:
#     print()

#i = 0.0
# while i <= 9.5:
#     print(i, end = "\n")
#     i += 0.5

# i = 1
# a = 0
# while i <= 100:
#     a = a + i
#     i += 1
# else:
#     print(a)


# begin = int(input("请输入开始整数："))
# end = int(input("请输入结束整数："))
# Sum = 0
# n = 0
# while begin < end:
#     print(begin, end = " ")
#     begin += 1
#     n += 1
#     if n % 5 == 0:
#         print()
#         n = 0



# 练习：
# 输入一个整数代表正方形宽度，　用变量n绑定，　
# 打印指定宽度的正方形

# n = int(input("请输入正方形宽度："))
# l = 1
# while l <= n:
#     h = 1
#     while h <= n:
#         print(h, end = " ")
#         h += 1
#     else:
#         print()
#     l += 1

#  # 任意输入一些整数，当属输入负数的时候输入结束
#   # 当属入完成后打印输入这些数的和
# Sum = 0
# while True:
#     s = int(input("请输入正整数:") or "0")
#     if s < 0:
#         break
#     Sum += s
# print(Sum)


# 输入一个整数n，　打印宽度n个字符的正方形

# n = int(input("请输入正方形边长"))
# y = 1
# print('#' * n)
# while y <= (n - 2):
#     print('#' + ' ' * (n - 2) + '#')
#     y += 1
# if n != 1:
#     print('#' * n)


# end = 1
# while a <= 9:
#     a = 1
#     b = 1
#     while b <= end:
#         print(a + "*" + b + "=" + a * b)
#         b += 1
#     end += 1



#  # １求下列多项式的和
#  #    １＋１／２＋１／４＋１／４＋．．．．．．＋１／２＊＊１０００
# n = 1
# S = 0
# while n <= 1001:
#     s = 1 / 2 ** (n - 1)
#     S += s
#     n += 1
# print("求和等于：", S)
# print("求和等于：", S * 4)

# #  # １－　１／３＋　１／５－１／９．．．．．．．．＋　１／（２＊n－１）
# #  #    求当n＝１００００时，此公式的和

n = 1
S = 0
while n <= 1000000000000000000:
    s = 1 / (2 * n - 1)
    if n % 2 == 0:
        S -= s
    else:
        S += s
    n += 1
print("求和：", S)
print("求和：", S * 4)

# # 1
# i = int(input('请输入行数'))
# n = 1
# while n <= i:
#     s = '%' + str(i) + 's'
#     print(s % ('*' * n))
#     n += 1
# print()
# # 2
# i = int(input('请输入行数'))
# n = i
# while 1 <= n:
#     s = '%' + str(i) + 's'
#     print(s % ('*' * n))
#     n -= 1
# print()
# # 3
# i = int(input('请输入行数'))
# n = i
# while 1 <= n:
#     s = '%' + '-' + str(i) + 's'
#     print(s % ('*' * n))
#     n -= 1
# print()
# # 4
# i = int(input('请输入行数'))
# n = 1
# while n <= i:
#     s = '%' + '-' + str(i) + 's'
#     print(s % ('*' * n))
#     n += 1
# print()




# i = 9
# a = 1
# while a <= i:
#     b = 1
#     while b <= a:
#         c = a * b
#         s = str(b) + '*' + str(a) + '=' + str(c)
#         print(s, end=' ')
#         b += 1
#     print()
#     a += 1

# s = '123456789'
# s.startswith('1')


# n = 1
# S = 0
# while n >= 1:
#     s = 1 / (2 * n - 1)
#     if n % 2 == 0:
#         S -= s
#     else:
#         S += s
#     S = round(S, 100)
#     print("求和：", S)
#     n += 1

x = "My name is %(name)s and i am %(age)s years old" % {"name": "cooper", "age": "26"}
print(x)
