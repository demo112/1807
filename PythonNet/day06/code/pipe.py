import time
from multiprocessing import Pipe, Process


# 创建管道对象
fd1, fd2 = Pipe(duplex=True)


def fun(name):
    time.sleep(3)
    # 想管道输入内容
    fd1.send("hello " + str(name))


jobs = []

for i in range(5):
    p = Process(target=fun, args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    # 读取管道
    data = fd2.recv()
    print(data)

for i in jobs:
    i.join()
