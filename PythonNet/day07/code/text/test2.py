import multiprocessing
import time
import threading
from PythonNet.day07.code.text.de111 import count, write, read


co = []
t = time.time()
for x in range(10):
    th = threading.Thread(target=count, args=(1, 1))
    co.append(th)
    th.start()

for i in co:
    i.join()
print("LIne CPU:", time.time() - t)
x = time.time() - t


for x in range(10):
    p = multiprocessing.Process(target=write)
    p2 = multiprocessing.Process(target=read)
    co.append(p)
    co.append(p2)
    p.start()
    p2.start()

for i in co:
    i.join()
print("LIne IO:", time.time() - x - t)
