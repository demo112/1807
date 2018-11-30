from multiprocessing import Queue
from time import *

# 创建队列
q = Queue(3)


q.put(1)
sleep(0.00000000000000001)
print(q.empty())

q.put(2)
print(q.full())

q.put(3)
print(q._maxsize)

# q.put(4, True, 3)

# 取消息
print(q.get())
q.close()
