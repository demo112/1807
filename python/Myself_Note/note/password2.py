import math


def is_odd(n):
    return n % 2 == 1

newlist = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(newlist)


def is_sqr(x):
    return math.sqrt(x) % 1 == 0

newlist = list(filter(is_sqr, range(1, 101)))
print(newlist)
