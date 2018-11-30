class Car:
    """汽车类"""
    def run(self, speed):
        print("汽车以%s公里/小时的速度行驶" % speed)


class Plane:
    """飞机类"""
    def fly(self, height):
        print("飞机以海拔%s米的高度飞行" % height)


class PlaneCar(Car, Plane):
    """PlaneCar类同时继承汽车类和飞机类"""


p = PlaneCar()
p.fly(10000)
p.run(300)
