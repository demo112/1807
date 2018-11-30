class Mylist:
    """这是一个自定义的列表类型， 此类型的对象data属性绑定的列表来存储数据"""
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        # print('__len__方法被调用')
        return 'Mylist(%s)' % self.data

    def __iter__(self):
        # print('__iter__方法被调用')
        return MyListIterrater(self.data)
        # return iter(self.data)
        # for x in self.data:
        #     yield x


class MyListIterrater:
    """此类用来描述能够访问Mylist类型的对象的迭代器"""
    def __init__(self, lst):
        self.data_lst = lst
        self.cur_index = 0

    def __next__(self):
        """此方法用来实现迭代器协议"""
        # print('next方法被调用')
        if self.cur_index >= len(self.data_lst):
            raise StopIteration
        r = self.data_lst[self.cur_index]
        self.cur_index += 1
        return r


myl = Mylist([2, 3, 5, 7])
it = iter(myl)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print()

# for x in myl:
#     print(x)
L = [x ** 2 for x in myl]
print(L)