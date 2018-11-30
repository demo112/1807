from multiprocessing import *
import sys
from time import *


def writer1():
    lock.acquire()
    for i in range(50000000000):
        sys.stdout.write("1想先向终端写入\n")
    lock.release()


def writer2():
    lock.acquire()
    for i in range(50000000000):
        sys.stdout.write("2想先向终端写入\n")
    lock.release()


lock = Lock()


w1 = Process(target=writer1)
w2 = Process(target=writer2)

w1.start()
w2.start()

w1.join()
w2.join()
