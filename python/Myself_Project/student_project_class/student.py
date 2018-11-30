class Student:
    def __init__(self, name='无名氏', age=0, score=0):
        """此方法用来给人对象添加'姓名', '年龄', '家庭住址'三个属性"""
        self.name = name
        self.age = age
        self.score = score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.score = score

    def show_info(self):
        """显示此人的全部信息"""
        print('这个人的name是：', self.name)
        print('这个人的age是：', self.age)
        print('这个人的score是：', self.score)


lst = []
lst.append(Student('小张', 20, 100))
lst.append(Student('小李', 18, 95))
lst.append(Student('小魏', 20))
lst[2].set_score(50)

for obj in lst:
    obj.show_info()
# s1 = Student('张三', 20, 98)
# s1.show_info()
# lst.append({...}) 改为对象
# def new_input():
#     # 字典转换备用方案
#     # for d in lst:
#     #     name = d['name']
#     #     age = d['age']
#     #     score = d['score']
#     lst = []
#     while True:
#         name = input('请输入姓名')
#         if name:
#             age = int(input('请输入年龄'))
#             score = int(input('请输入分数'))
#             lst.append(Student(name, age, score))
#         else:
#             break
#     return lst
# lst = new_input()
# print(lst)
