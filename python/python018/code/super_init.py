class A:
    def work(self):
        print("A.work被调用")


class B(A):
    """B类继承A类"""
    def work(self):
        print("B.work被调用")

    def super_work(self):
        self.work()
        super(B, b).work()
        super(__class__, b).work()
        super().work()          # 此中调用方式只能在示例方法内


b = B()
b.work()
b.super_work()
