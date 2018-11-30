# 此示例示意用函数生成器函数生成从0到n结束的一些列整数


def myinteger(n):
    i = 0
    while i < n:
        yield i
        i = i + 1


for x in myinteger(300):
    print(x)


L = [x for x in myinteger(100) if x % 2 == 1]
print('L=', L)
