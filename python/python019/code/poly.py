class Shape:
    def draw(self):
        print('Share的draw被调用')


class Point(Shape):
    def draw(self):
        print('正在画一个点！')


class Circle(Point):
    def draw(self):
        print('正在画一个园！')


def my_draw(s):
        s.draw()


s1 = Circle()
s2 = Point()
my_draw(s1)
my_draw(s2)
