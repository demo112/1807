# myeven(start, stop)
# 此函数用来生成从 start开始到stop结束(不包含)区间内的一系列偶数
#   def myeven(start, stop):
#       ....
#
#   evens = list(myeven(10, 20))
#   print(evens)  # [10, 12, 14, 16, 18]
#   for x in myeven(21, 30):
#       print(x)  # 22, 24, 26, 28
#
#   L = [x**2 for x in myeven(3, 10)]
#   print(L)  # 16 36 64


def myeven(start, stop):
    while start  < stop:
        if start % 2 == 0:
            yield start
        start += 1


evens = list(myeven(10, 20))
print(evens)  # [10, 12, 14, 16, 18]
for x in myeven(21, 30):
  print(x)  # 22, 24, 26, 28

L = [x ** 2 for x in myeven(3, 10)]
print(L)  # 16 36 64