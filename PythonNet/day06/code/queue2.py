from multiprocessing import Queue, Process
from time import *


# 创建队列
q = Queue()


def fun1():
    sleep(1)
    q.put({'a': 1, "b": 2})


def fun2():
    sleep(2)
    print('收到：', q.get())


p1 = Process(target=fun1)
p2 = Process(target=fun2)
p1.start()
p2.start()
p1.join()
p2.join()
