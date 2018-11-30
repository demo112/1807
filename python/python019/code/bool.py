class Mylist:
    """这是一个自定义的列表类型， 此类型的对象data属性绑定的列表来存储数据"""
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        print('__len__方法被调用')
        return 'Mylist(%s)' % self.data

    # def __bool__(self):
    #     print("__bool__方法被调用")
    #     return any(self.data)


myl = Mylist([False, 0, 0.0, 1])
print(bool(myl))
if myl:
    print(myl, '的布尔值为True')
else:
    print(myl, '的布尔值为False')
