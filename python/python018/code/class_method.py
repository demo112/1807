

class A:
    v = 0       # 类变量（类属性）

    @classmethod
    def get_v(cls):
        return cls.v        # 用cls访问变量v

    @classmethod
    def set_v(cls, n):
        A.v = n             # 注意变量的作用域

# A.v = 100               #不建议这样使用


print('A.v = ', A.get_v())
A.set_v(200)
print('A.v = ', A.get_v())


