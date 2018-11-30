# 古典问题：
# 有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
# 问每个月的兔子总数为多少？

# def rabbit(n):
#     lst = [1, 1]
#     while 0 < n - 2:
#         lst.append((lst[-1] + lst[-2]))
#         n -= 1
#     return lst[-1]
#
# print(rabbit(6))


# 牛逼
all_rabbit = []


class Rabbit:
    def __init__(self, birthday):
        self.birthday = birthday
        all_rabbit.append(self)

    def makechild(self, month):
        if month - self.birthday >= 2:
            Rabbit(month)


Rabbit(1)

for i in range(1, 22):
    [j.makechild(i) for j in all_rabbit[:]]
    print(len(all_rabbit))
