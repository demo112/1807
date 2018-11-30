import threading
from threading import Thread
from time import sleep


# 设置通信载体
s = None
e = threading.Event()


def bar():
    print("bar拜山头")
    global s
    s = '天王盖地虎'


def foo():
    print("说出口令就是自己人")
    sleep(2)
    if s == '天王盖地虎':
        print("我是座山雕，自己人")
    else:
        print("弄死他")
    e.set()


def fun():
    print("呵呵。。。")
    sleep(1)
    global s
    s = "小鸡炖蘑菇"


b = Thread(target=bar)
f = Thread(target=foo)
b.start()
f.start()
# 表示运行b,f之后其他内容不允许运行
e.wait()
fun()
b.join()
f.join()
