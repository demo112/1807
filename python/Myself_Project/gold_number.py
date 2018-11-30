def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a+b
        yield a


def few(n):
    it = iter(fib(n))
    lst = list(it)
    return lst


def gold(n):
    lst = few(n)

    num = lst[n - 2] / lst[n - 1]
    print(num)


def write(n):
    f = open('fibonacci.txt', 'wt')
    for i in few(n):
        f.writelines('%s\n' % i)
    f.close()
    gold(n)


write(200)
# gold(1000)
# gold(10000)
# gold(100000)
# gold(1000000)
# gold(10000000)
# gold(100000000)
# gold(1000000000)
