# 用类来描述一个学生的信息(可以修改之前写的Student类)
#     class Student:
#          .... 此处自己实现
#
#     学生信息有:
#        姓名, 年龄, 成绩
#
#     将一些学生的对象存于列表中,可以任意添加和删除学生信息
#       1) 打印出学生的个数
#       2) 打印出所有学生的平均成绩
#       3) 打印出所有学生的平均年龄


class Student:
    """描述一个学生的信息"""
    student_count = 0
    student_age = 0
    student_score = 0
    lst = []

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        Student.lst.append(self)
        Student.student_count += 1
        Student.student_age += age
        Student.student_score += score

    @classmethod
    def show_student_info(cls):
        print('学生的个数是：', Student.student_count)
        print('学生的平均年龄是：', Student.student_age / Student.student_count)
        print('学生的平均分数是：', Student.student_score / Student.student_count)

    def delete_student_info(self):
        Student.lst.remove(self)
        Student.student_count -= 1
        Student.student_age -= self.age
        Student.student_score -= self.score


a = Student('zhangsan', 12, 89)
b = Student('lisi', 13, 89)
v = Student('lisi', 12.7, 30)
v.delete_student_info()
Student.show_student_info()
