class A:
    def work(self):
        print("A.work被调用")


class B(A):
    """B类继承A类"""
    def work(self):
        print("B.work被调用")


b = B()
b.work()

a = A()
a.work()

# "当调用发生时，子类如何调用父类中被覆盖的方法
# 基类名.方法名（实例，实际调用参数）"
b = B()
A.work(b)
