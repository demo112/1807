# 测试函数：计算密集型
def count(x, y):
     c = 0
     while c < 6000000:
         c += 1
         x += 1
         y += 1


def write():
    f = open('text.txt', 'w')
    for i in range(100000000):
        f.write("hello world\n")
    f.close()


def read():
    f = open('text.txt', 'r')
    lines = f.readlines()
    f.close()

