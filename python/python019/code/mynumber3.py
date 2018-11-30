class Mylist:
    """这是一个自定义的列表类型， 此类型的对象data属性绑定的列表来存储数据"""
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'Mylist(%s)' % self.data

    def __len__(self):
        return len(self.data)

    def __abs__(self):
        return Mylist([abs(x) for x in self.data])




myl = Mylist([1, -2, -3, -4])
print(myl)
print(len(myl))
print(abs(myl))

n1 = Mylist(100)
n = int(n1)
