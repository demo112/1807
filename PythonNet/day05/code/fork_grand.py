import os
from time import sleep


def f1():
    sleep(3)
    print("ONE")


def f2():
    sleep(4)
    print("TWO")


pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    p = os.fork()
    if p == 0:
        f2()
    else:
        os._exit(0)
else:
    os.wait()
    f1()
