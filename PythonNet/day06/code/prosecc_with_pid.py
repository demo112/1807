from multiprocessing import Process
from time import sleep

# # 带参数的进程函数
# def worker(sec, name):
#     for i in range(3):
#         sleep(sec)
#         print("I'm %s" % name)
#         print("I'm working")
#
# p = Process(target=worker, args=(2,'zhang'))
# p.start()
# p.join()


# 分开传参
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working")

p = Process(target=worker, name='worker', args=(2,), kwargs={'name':'zhang'})
p.start()
print('Process name:', p.name)
print('Process PID:', p.pid)

p.join()