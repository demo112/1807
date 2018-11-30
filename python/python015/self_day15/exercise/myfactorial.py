# myfactorial()(start, stop)
# 此函数用来生成n个从一开始的阶乘
#
import math


def myfactorial(stop):
    x = 1
    while x <= stop:
        yield math.factorial(x)
        x += 1


evens = list(myfactorial(5))
it = iter(evens)
while True:
    print(next(it))  # [10, 12, 14, 16, 18]


