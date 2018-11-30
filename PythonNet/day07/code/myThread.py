from threading import Thread
from time import ctime, sleep


class MyThread(Thread):
    def __init__(self, group=None, target=None, name='cooper', args=(), kwargs=None):
        # def __init__(self, group, target, name, args, kwargs):
        # 必须要有super继承父类
        super().__init__(group, target, name, args, kwargs)

        if kwargs is None:
            kwargs = {}

        self.group = group
        self.target = target
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            if self.target:
                # 注意星号传参
                self.target(*self.args, **self.kwargs)
        finally:
            del self.target, self.args, self.kwargs


def player(song, sec):
    for i in range(2):
        print("Playing %s %s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, kwargs={'song': '凉凉', 'sec': 2})

t.start()
t.join()
