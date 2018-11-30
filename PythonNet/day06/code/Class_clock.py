from multiprocessing import Process
from time import *


class ClockProcessing(Process):
    def __init__(self, value):
        self.value = value
        super(ClockProcessing, self).__init__()

    def run(self):
        for i in range(5):
            print("The time is {}".format(ctime()))
            sleep(self.value)
        pass


# 创建自定义进程类的对象
p = ClockProcessing(2)

# 自动调用父类的方法
p.start()
p.join()
