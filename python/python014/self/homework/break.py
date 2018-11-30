

# def prime(y):
#     y = y
#     lst = []
#     for x in range(1, y):
#         if x < 2:
#             pass
#         else:  # n大于等于2
#             for i in range(2, x):
#                 if x % i == 0:  # 如果整除
#                     break
#             else:
#                 lst += [x]
#     return lst
#
#
# def isprime(x):
#     if x < 2:
#         return False
#     else:
#         for y in range(2, x):
#             if x % y == 0:
#                 return False
#         return True
#
# def re(y):
#     lst = []
#     for x in range(2, y):
#         while True:
#             if y % x == 0:
#                 y = y / x
#                 lst += [str(x)]
#             else:
#                 break
#     return lst
# y = 370105199208263718
# print('%s=' % y, '*'.join(re(y)), sep='')

# WAY2
def bre():
    n = int(input('请输入一个正整数'))
    num = n
    lst = []
    while n != 1:
        for x in range(2, n + 1):
            if n % x == 0:
                lst.append(str(x))
                n = int(n / x)
                break
    print(lst)
    return lst, num
# print(bre(90))
a = bre()
print('%s=%s' % (a[1], '*'.join(a[0])))
