from random import choice
from time import sleep

a = b = 0
n = 1
while True:
    a += 1 / 2 ** n
    b += 1 / 2 ** (n + 1)
    n += 1
    p = a / (a + b)
    print(p)