# 3. 写一个类Fibonacci实现迭代器协议,此类的对象可以作为可迭代对象生成斐波那契数列
#          1 1 2 3 5 8 13 ....
#     class Fibonacci:
#         def __init__(self, n):
#             ...
#         ...
#     for x in Fibonacci(10):
#         print(x)  # 打印 1 1 2 3 5 8 ...


class Prime:
    def __init__(self, n):
        self.data = [__x for __x in Prime.is_fibonacci(n)]

    def __iter__(self):
        return PrimeIterable(self.data)

    @staticmethod
    def is_fibonacci(n):
        a, b = 1, 1
        lst = []
        for i in range(n - 1):
            lst.append(a)
            a, b = b, a + b
        return lst


class PrimeIterable:
    def __init__(self, lst):
        self.data = lst
        self.l_index = 0

    def __next__(self):
        # print('用到__next__')
        if self.l_index >= len(self.data):
            raise StopIteration
        r = self.data[self.l_index]
        self.l_index += 1
        return r


for x in Prime(20):
    print(x, end=' ')
print()
