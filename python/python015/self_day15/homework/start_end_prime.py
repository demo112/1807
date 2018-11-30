# Mysql_order 用生成器函数，生成素数，给出起始值begin和终止值 end, 生成begin到end范围内的素数
#     如:
#       def prime(begin, end):
#         ...
#
#       L=[x for x in prime(10, 20)]  #L=[11,13,17,19]


def isprime(x):
    if x < 2:
        return False
    else:
        for y in range(2, x):
            if x % y == 0:
                return False
        return True


def range_prime(start, end):
    for x in range(start, end):
        if isprime(x):
            yield x


lst = range_prime(10, 20)
gen = [x for x in range_prime(10, 20)]
print(gen)
