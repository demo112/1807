# 写一个生成器函数myxrange([start, ], stop[, step]) 来生成一系列整数
#     要求:
#       myxrange功能与range功能相同（不允许调用range函数)
#     用自己写的myxrange函数结合生成器表达式求1~10内奇数的平方和


def myrange(start, end=0, step=1):
    while True:
        start, end = end, start
        if start > end:
            yield end
            end += step
            start, end = end, start
        else:
            break


gen = [x for x in myrange(1, 10)]
print(gen)
lst = [x ** 2 for x in myrange(1, 10)]
print(lst)
print(sum(lst))
print(sum([x ** 2 for x in myrange(1, 10, 2)]))
print(sum([x ** 2 for x in myrange(1, 10, -2)]))
print(sum([x ** 2 for x in range(1, 10)]))
print(sum(myrange(1, 10)))
print(sum(range(1, 10)))
