# del_method.py
# 此示例示意析构方法的调用

class Car:
    def __init__(self,info):
        self.info = info
        print('汽车对象', info, '被创建')

    def __del__(self):
        print('汽车对象', self.info, '被销毁')


c1 = Car('BYD E6')              # 汽车对象 BYD E6 被创建
# C1 = None
del c1                          # 汽车对象 BYD E6 被销毁


lst =[]
lst.append(Car("汽车1"))         # 汽车对象 汽车1 被创建
lst.append(Car("汽车2"))         # 汽车对象 汽车2 被创建
lst.append(Car("汽车3"))         # 汽车对象 汽车3 被创建
del lst
                                 # 汽车对象 汽车3 被销毁
                                 # 汽车对象 汽车2 被销毁
                                 # 汽车对象 汽车1 被销毁
input('请输入回车键继续执行程序')
print("程序推出")
