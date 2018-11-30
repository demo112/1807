class Mynumber:
    def __init__(self, val):
        self.data = val         # 在每个对象内部都传遍一个实例变量来绑定数据

    def __str__(self):
        return '自定义的数字：%s' % self.data

    def __repr__(self):
        """此方法返回的字符串一定是能表示self对象的表达式的字符串"""
        return 'Mynumber(%d)' % self.data


n1 = Mynumber(100)
n2 = Mynumber(200)
n3 = Mynumber(300)

# 两个等效
print('str(n1)  =', str(n1))
print('str(n2)  =', n2.__str__())
print('str(n3)  =', n3)             # 在print内部会将n3用str()转为字符串再写到sys.stdout

print('repr(n1) =', repr(n1))           # 调用的是
print('repr(n2) =', n2.__repr__())           # 调用的是
