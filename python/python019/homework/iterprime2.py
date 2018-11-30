class Prime:
    def __init__(self, b, n):
        self.begin = b
        self.count = n
        self.cur_count = 0

    def __iter__(self):
        return self         # iter 会自动调用self的next方法

    def __next__(self):
        # 判断已提供的数据个数和要提供的数据个数是否相等
        if self.cur_count >= self.count:
            raise StopIteration
        while True:
            if self.isprime(self.begin):
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
