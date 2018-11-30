# class Car:
#     """汽车类"""
#     def run(self, speed):
#         print("汽车以%s公里/小时的速度行驶" % speed)
#
#
# class Plane:
#     """飞机类"""
#     def fly(self, height):
#         print("飞机以海拔%s米的高度飞行" % height)
#
#     def run(self, speed):
#         print("飞机以%s公里/小时的速度行驶" % speed)
#
# class PlaneCar(Car, Plane):
#     """PlaneCar类同时继承汽车类和飞机类"""
#
#
# p = PlaneCar()
# p.fly(10000)
# p.run(300)
# p.run(300)


class A:
    def m(self):
        print("A.m()被调用")


class B:
    def m(self):
        print("B.m()被调用")


class AB(A, B):
    def m(self):
        print("AB自己的方法被调用")

ab = AB()
ab.m()
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B
