class MyList:
    def __init__(self, lst):
        self.data = list(lst)

    def __repr__(self):
        return

    def __add__(self, rhs):
        new = self.data + rhs.data
        return "MyList(%s)" % new

    def __radd__(self, lhs):
        new = self.data + lhs.data
        return "MyList(%s)" % new

    def __mul__(self, rhs):
        new = self.data * int(rhs)
        return "MyList(%s)" % new

    def __rmul__(self, lhs):
        new = self.data * int(lhs)
        return "MyList(%s)" % new
        # 只有左手边为内建类型的时候才会调用反向

L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
L3 = L1 + L2
print(L3)

L4 = L2 + L1
print(L4)

L4 = L2 + L1
print(L4)


L5 = L1 * 2
print(L5)
L5 = 3 * L1
print(L5)
