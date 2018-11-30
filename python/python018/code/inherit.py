class Human:

    @staticmethod
    def say(what):
        print("说", what)

    @staticmethod
    def walk(distance):
        print('走了', distance, '公里')


class Student(Human):

    @staticmethod
    def study(subject):
        print("今天学了", subject)


class Teacher(Student):

    @staticmethod
    def teach(subject):
        print("教", subject)


h1 = Human()
h1.walk(5)
h1.say('今天天气正好')


s1 = Student()
s1.walk(4)
s1.say('有点累')
s1.study('python')


t1 = Teacher()
t1.walk(6)
t1.say('吃点啥')
t1.teach('面向对象')
t1.study('英雄联盟')


print(Student.__bases__)
print(Teacher.__bases__)
