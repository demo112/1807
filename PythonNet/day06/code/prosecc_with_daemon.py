from multiprocessing import Process
from time import sleep


# 分开传参
def tm():
    while True:
        sleep(1)
        print('1')


p = Process(target=tm)
p.daemon = False
p.start()
sleep(5)
print('主进程退出')
