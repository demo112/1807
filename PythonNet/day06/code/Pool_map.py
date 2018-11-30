from multiprocessing import Pool
from time import sleep


def fun(n):
    sleep(1)
    print('')
    return n ** 2


pool = Pool(4)
r = pool.map(fun, range(10))
pool.close()
pool.join()
print(r)
