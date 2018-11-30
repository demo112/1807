numbers = [10086, 10000, 10010, 9558]
names = ['中国移动', '中国电信', '中国联通']
for t in zip(numbers, names):
    print(t)
for x, y in zip(numbers, names):
    print(y, '的客服电话是:', x)
x, y = (10086, '中国移动')      # 序列赋值
# zip函数的实现示例2:


def myzip(iter1, iter2):
    it1 = iter(iter1)  # 拿出一个迭代器
    it2 = iter(iter2)
    while True:
        a = next(it1)
        b = next(it2)
        yield (a, b)


for t in myzip(numbers, names): #能实现与zip同样的功能
  print(t)