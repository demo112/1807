# 练习:
#   实现有序集合类 OrderSet() 能实现两个集合的交集 &,全集 |,
#   补集 -  对称补集 ^, ==/!= , in/ not in 等操作
#   要求集合内部用 list 存储
#   class OrderSet:
#       ...
#   s1 = OrderSet([1, 2, 3, 4])
#   s2 = OrderSet([3, 4, 5])
#   print(s1 & s2)  # OrderSet([3, 4])
#   print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
#   print(s1 ^ s2)  # OrderSet([1, 2, 5])
#   if OrderSet([1, 2, 3]) != OrderSet([3, 4, 5]):
#       print("不相等")
#   if s2 == OrderSet(3, 4, 5):
#      print('s2 == OrderSet(3, 4, 5) is True')
# if 2 in s1:
#     print('2 in s1　返回真')


class OrderSet:
    def __init__(self, lst):
        self.data = list(lst)

    def __add__(self, other):
        new = self.data + other.data
        return OrderSet(new)

    def __repr__(self):
        return "OrderSet(%s)" % self.data

    def __sub__(self, other):
        new = [x for x in self.data if x not in other.data and ]
        return new

    def __and__(self, rhs):
        new = (self.data + rhs.data) - \
              (self-rhs) - (rhs - self)
        return OrderSet(new)

    def __or__(self, rhs):
        new = self.data + rhs.data
        return OrderSet(new)

    def __xor__(self, rhs):
        new = (self.data - rhs.data) +\
              (rhs.data - self.data)
        return OrderSet(new)


s1 = OrderSet([1, 2, 3, 4])
s2 = OrderSet([3, 4, 5])
print(s1 & s2)  # OrderSet([3, 4])
print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
# print(s1 ^ s2)  # OrderSet([1, 2, 5])
if OrderSet([1, 2, 3]) != OrderSet([3, 4, 5]):
    print("不相等")
if s2 == OrderSet([3, 4, 5]):
    print('s2 == OrderSet([3, 4, 5]) is True')
# if 2 in s1:
#     print('2 in s1　返回真')
