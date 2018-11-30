# 2. 写一个生成器函数，生成斐波那契数列的前n个数
#      1 1 2 3 5 8 13
#       def fibonacci(n):
#           ...
#           yield...
#     1) 输出前20个数:
#       for x in fibonacci(20):
#           print(x)
#     2) 打印前40个数的和:
#        print(sum(fibonacci(40)))


def fibonacci(n):
    n = n
    def fi(n):
        L = [0, 1]
        x = 0
        while x < n:
            a = L[0]
            b = L[1]
            c = a + b
            x += 1
            L[0] = L[1]
            L[1] = c
            yield c
    return [1] + [x for x in fi(n)]
print(fibonacci(20))
