from multiprocessing import *
from time import *

#
# # 创建共享内存，开辟5个空间
# shm = Array('i', 5)
#

# 存入字符串,要求Bytes格式
shm = Array("c", b'Hello')


def fun():
    for i in shm:
        sleep(0.01)
        print(i)
    shm[0] = b'h'


p = Process(target=fun)
p.start()
p.join()

for x in shm:
    print(x)
print(shm.value.decode())
