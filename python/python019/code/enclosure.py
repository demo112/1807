class A:
    def __init__(self):
        self.__p1 = 100
        self.p2 = 200

    def show_info(self):
        print(self.__p1, '此对象的实例方法可以访问和修改私有属性')
        a.__m()

    def __m(self):
        print("A类对象的__m方法被show_info调用")


a = A()
# print(a.__p1)   # AttributeError: 'A' object has no attribute '__p1'
print(a.p2)
a.show_info()
# AttributeError: 'A' object has no attribute '__m'
# a.__m               # 出错，除A类的实例方法外，不能调用a对象的私有方法
