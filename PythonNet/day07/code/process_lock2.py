from multiprocessing import *
import sys
from time import *


def writer1():
    for i in range(500000000):
        # sleep(0.1)
        lock.acquire()
        sys.stdout.write("1想先向终端写入\n")
        lock.release()


def writer2():
    for i in range(500000000):
        # sleep(0.1)
        lock.acquire()
        sys.stdout.write("2想先向终端写入\n")
        lock.release()


lock = Lock()


w1 = Process(target=writer1)
w2 = Process(target=writer2)

w1.start()
w2.start()

w1.join()
w2.join()
