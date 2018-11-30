import time
from multiprocessing import Pipe, Process


# 创建管道对象
fd1, fd2 = Pipe(duplex=False)


# 创建管道两端进程
def fun(name):
    time.sleep(3)
    # 向管道输入内容
    fd2.send("hello " + str(name))


# Process进程类运行进程
jobs = []
for i in range(5):
    p = Process(target=fun, args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    # 读取管道
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()
