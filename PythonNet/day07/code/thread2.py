from threading import Thread, currentThread
from time import sleep
# import os


def fun(sec):
    print("线程属性测试")
    sleep(sec)
    # 线程对象的getName()属性
    print("%s线程结束" % currentThread().getName())


thread = []
for i in range(3):
    t = Thread(target=fun, name="cooper%d" % i, args=(2,))
    thread.append(t)
    t.start()

print("is alive", t.is_alive())
thread[1].setName("COOPER")

for t in thread:
    t.join()


if __name__ == '__main__':
    pass
