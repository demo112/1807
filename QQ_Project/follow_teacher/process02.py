import multiprocessing
from time import *
import os


def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(), '父_______子', os.getpid())


def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(), '父_______子', os.getpid())


def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(), '父_______子', os.getpid())


lst = [th1, th2, th3]
process = []
for i in lst:
    p = multiprocessing.Process(target=i)
    process.append(p)
    p.start()
for i in process:
    i.join()
    print(i.getpid(), '被关闭')