# # 写一个实现迭代器协议的类,让此类可以生成从b 开始的n个素数
# #     class Prime:
# #         def __init__(self, b, n):
# #             ...
# #         def __iter__(self):
# #            ....
# #
# #     L = [x for x in Prime(10, 4)]
# #     print(L)  # L = [11, 13, 17, 19]
#
#
# class Prime:
#     def __init__(self, b, n):
#         self.data = [x for x in Prime.isprime(b, n)]
#
#     def __iter__(self):
#         return PrimeIterable(self.data)
#
#     @staticmethod
#     def isprime(b, n):
#         lst = []
#         while n > 0:
#             if b < 2:
#                 b += 1
#             else:  # n大于等于2
#                 for i in range(2, b):
#                     if b % i == 0:  # 如果整除
#                         b += 1
#                 else:
#                     lst += [b]
#                     b += 1
#                     n -= 1
#         else:
#             return lst
#
#
# class PrimeIterable:
#     def __init__(self, lst):
#         self.data = lst
#         self.l_index = 0
#
#     def __next__(self):
#         print('用到__next__')
#         if self.l_index >= len(self.data):
#             raise StopIteration
#         r = self.data[self.l_index]
#         self.l_index += 1
#         return r
#
#
# L = [x for x in Prime(20, 4)]
# print(L)  # L = [11, 13, 17, 19]


class Prime:
    def __init__(self, b, n):
        self.begin = b
        self.count = n

    def __iter__(self):
        return PrimeIterator(self.begin, self.count)


class PrimeIterator:
    def __init__(self, b, n):
        self.begin = b
        self.count = n
        self.cur_count = 0
        #  表示已生成的素数的个数

    def __next__(self):
        # 判断已提供的数据个数和要提供的数据个数是否相等
        if self.cur_count >= self.count:
            raise StopIteration
        while True:
            if PrimeIterator.isprime(self.begin):
                r = self.begin
                self.begin += 1
                self.cur_count += 1
                return r
            self.begin += 1

    @staticmethod
    def isprime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


# lst = []
# it = iter(Prime(10, 4))
# while True:
#     try:
#         x = next(it)
#         lst.append(x)
#     except StopIteration:
#         break
# print(lst)
lst = [x for x in Prime(10, 4)]
print(lst)
