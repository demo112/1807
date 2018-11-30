class MyList:
    def __init__(self, lst):
        self.data = list(lst)

    def __iadd__(self, rhs):
        print("__idd__方法被调用")
        self.data += rhs.data
        return "MyList(%s)" % self.data

    def __imul__(self, lhs):
        new = self.data * int(lhs)
        return "MyList(%s)" % new


L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
L1 += L2
print(L1)

L2 *= 2
print(L2)
