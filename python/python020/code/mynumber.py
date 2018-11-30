class MyNumeber:
    def __init__(self, v):
        self.data = v

    def __repr__(self):
        return "MyNumber(%d)" % self.data

    def __add__(self, other):
        __add = self.data + other.data
        return MyNumeber(__add)     # 此处一定要返回一个此类的对象

    def __sub__(self, other):
        __sub = self.data - other.data
        return MyNumeber(__sub)     # 此处一定要返回一个此类的对象

    def __mul__(self, other):
        __mul = self.data * other.data
        return MyNumeber(__mul)     # 此处一定要返回一个此类的对象

    def __truediv__(self, other):
        __truediv = self.data / other.data
        return MyNumeber(__truediv)     # 此处一定要返回一个此类的对象

    def __floordiv__(self, other):
        __truediv = self.data // other.data
        return MyNumeber(__truediv)     # 此处一定要返回一个此类的对象

    def __mod__(self, other):
        __mod = self.data % other.data
        return MyNumeber(__mod)     # 此处一定要返回一个此类的对象

    def __pow__(self, other):
        __pow = self.data ** other.data
        return MyNumeber(__pow)     # 此处一定要返回一个此类的对象


n1 = MyNumeber(8)
n2 = MyNumeber(5)
# n3 = n1.add(n2)
n3 = n1 + n2            # Same as n3 = n1.__add__(n2)
n4 = n1 - n2            # Same as n4 = n1.__sub__(n2)
n5 = n1 * n2            # Same as n5 = n1.__mul__(n2)
n6 = n1 / n2            # Same as n6 = n1.__truediv__(n2)
n7 = n1 // n2            # Same as n7 = n1.__floordiv__(n2)
n8 = n1 % n2            # Same as n8 = n1.__mod__(n2)
n9 = n1 ** n2            # Same as n9 = n1.__pow__(n2)


print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)
