class Mynumber:
    def __init__(self, val):
        self.data = val         # 在每个对象内部都传遍一个实例变量来绑定数据

    def __str__(self):
        return '自定义的数字：%s' % self.data

    def __repr__(self):
        """此方法返回的字符串一定是能表示self对象的表达式的字符串"""
        return 'Mynumber(%d)' % self.data

    def __int__(self):
        return int(self.data)

    def __float__(self):
        return float(self.data)

    def __complex__(self):
        return complex(self.data)


n1 = Mynumber(100)
n2 = Mynumber(200)
n3 = Mynumber(300)

print(n1)       # print(str(n1))

n4 = Mynumber(400.987)
n11 = int(n4)
print(n11)

n22 = float(n4)
print(n22)

n33 = complex(n4)
print(n33)
