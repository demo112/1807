class Student:
    def __init__(self, s):
        self.__score = s

    def set_score(self, __s):
        """
        setter是用来改变数据的"""
        if 0 <= __s <= 100:
            self.__score = __s

    def get_score(self):
        """getter只能用来获取数据"""
        return self.__score


s = Student(50)
print(s.get_score())
s.set_score(100)
print(s.get_score())


# s.__score = 100
# print(s.__score)
# s.__score = 10000
# print(s.score)
