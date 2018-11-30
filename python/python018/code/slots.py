class Human:
    __slots__ = ['name', 'age']

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def info(self):
        print(self.name, '今年', self.age, '岁')


h1 = Human('小张', 8)
h1.info()
h1.age = 9
h1.info()

# print(h1.__dict__)
print(h1.__slots__)