import multiprocessing
from time import *

a = 1


def fun():
    sleep(1)
    global a
    print('a =', a)
    a = 10000
    print("子进程事件")


# 创建进程对象
p = multiprocessing.Process(target=fun)

# 启动进程
p.start()

sleep(2)
print("这是父进程")
# 回收进程
p.join()

print('Parent a =', a)
