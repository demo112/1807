names = ['中国移动', '中国电信', '中国联通']
for t in enumerate(names):
    print(t)
# (0, '中国移动')
# (1, '中国电信')
# (2, '中国联通')


names = ['中国移动', '中国电信', '中国联通']
for t in enumerate(names, 10):
    print(t)
# (10, '中国移动')
# (11, '中国电信')
# (12, '中国联通')


def myenum(iterable):
    it = iter(iterable)
    i = 0
    while True:
        a = next(it)
        yield (i, a)
        i += 1
names = ['中国移动', '中国电信', '中国联通']
print(myenum(names))