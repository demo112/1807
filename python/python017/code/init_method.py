# init_method.py
# c此示例示意初始化方法的定义，即用初始化方法对新建对象添加属性

class Car:
    """小汽车"""
    def __init__(self, c, b, m):
        self.color = c
        self.brand = b
        self.model = m
    def __name__(self):
        print(self)

    def run(self,speed):
        print(self.color, '的', self.brand, self.model, '正在以', speed, '公里/小时的速度行驶', sep='', end='!\n')


a4 = Car('红色', '奥迪', 'A4')
a4.run(199)
# a4.__name__()

t1 = Car('蓝色', 'TESLA', 'S')
t1.run(230)

