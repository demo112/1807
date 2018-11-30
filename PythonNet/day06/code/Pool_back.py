from multiprocessing import Pool
from time import *


def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

# 创建进程池
pool = Pool(processes=4)
result = []
for i in range(10):
    msg = "hello%d" % i
    # 将事件放入进程池队列，等待执行
    r = pool.apply_async(func=worker, args=(msg,))          # 异步
    result.append(r)    # r只是这个事件进程返回的一个对象
# 关闭进程池
pool.close()
# 回收进程池进程
pool.join()



for r in result:
    print(r.get())      # 通过该对象的方法来获取内容
