from multiprocessing import *
from time import *


# 创建初始内存，初始放入列表
shm = Array('i', [1, 2, 3, 4, 5])

def fun():
    for i in shm:
        sleep(0.01)
        print(i)
    shm[3] = 10000

p = Process(target=fun)
p.start()
p.join()

for i in shm:
    print(i)