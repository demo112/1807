import threading
from time import sleep
import os


a = 1


def music():
    global a
    print(a)
    a = 1000000000000000000000000000000000000
    for x in range(5):
        sleep(0.2)
        print('播放葫芦娃🎵👅', os.getpid())


# 创建线程对象
t = threading.Thread(target=music)
t.start()
t.join()
print(a)

for i in range(5):
    sleep(0.15)
    print('听音乐灌篮高手', os.getpid())


if __name__ == '__main__':
    pass
