import time
from PythonNet.day07.code.text.de111 import write, read, count


t = time.time()
for i in range(10):
    count(1, 1)
print("LIne cpu:", time.time() - t)
x = time.time() - t

for i in range(10):
    write()
    read()
print("LIne IO:", time.time() - t - x)
