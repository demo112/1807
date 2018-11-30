from .menu import menu


class Student:
    def __init__(self, name='无名氏', age=0, score=0):
        """此方法用来给人对象添加'姓名', '年龄', '家庭住址'三个属性"""
        self.__name = name
        self.__age = age
        self.__score = score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score

    def get_info(self):
        """次方法用来返回学生信息的元组"""
        return self.__name, self.__age, self.__score

    def get_score(self):
        return self.__score

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def show_info(self):
        """显示此人的全部信息"""
        print('这个人的name是：', self.__name)
        print('这个人的age是：', self.__age)
        print('这个人的score是：', self.__score)

    def save_info(self, file):
        file.write(self.__name)
        file.write(' ')
        file.write(str(self.__age))
        file.write(' ')
        file.write(str(self.__score))
        file.write('\n')


# 输入学生信息
def input_student(lst):
    while True:
        try:
            name = input("请输入学生姓名：")
            if len(name) == 0:
                print("学生信息录入结束")
                break
            elif len(name) != 0:
                age = int(input("请输入学生年龄："))
                score = int(input("请输入学生成绩："))
                lst.append(Student(name, age, score))
            else:
                pass
        except ValueError:
            print("您输入的学生信息有误")
            break
    return lst


# 获取名字中中文的个数
def get_chinese_char_count(lst):
    count = 0  # 先假设个数为0
    ls = []
    for x in lst:
        for ch in x.get_name():
            # 如果ch为中文字典,则count 做加一操作
            if ord(ch) > 127:
                count += 1
        ls += [count]
    return max(ls)


# 打印列表
def print_list(lst):
    n = get_chinese_char_count(lst)
    k = int(max(len(n.get_name()) for n in lst) + n + 10)
    print('+' + '-' * k + '+' + '-' * 11 + '+' + '-' * 11 + '+')
    print(
        '|' + 'name'.center(k) +
        '|' + 'age'.center(11) +
        '|' + 'score'.center(11) +
        '|')
    print('+' + '-' * k + '+' + '-' * 11 + '+' + '-' * 11 + '+')
    for m in lst:
        name, age, score = m.get_info()
        if get_chinese_char_count([m]) == 0:
            print('|%s|%s|%s|' % (str(name).center(k),
                                  str(age).center(11),
                                  str(score).center(11)))
        else:
            print('|%s|%s|%s|' % (str(name).center(k - int(n * 2 / 3)),
                                  str(age).center(11),
                                  str(score).center(11)))

    # print('aaa'.center(k), 'age'.center(11))# , str(n['score']).center(11))
    print('+' + '-' * k + '+' + '-' * 11 + '+' + '-' * 11 + '+')


# 显示学生信息
def output_student(lst):
    try:
        print_list(lst)
    except (TypeError, ValueError):
        print("您还没有输入学生信息")
        menu()


# 删除学生信息
def delete_student(lst):
    name = input("请输入学生姓名：")
    for n in lst:
        if name == n.get_name():
            lst.remove(n)
            break
    return lst


# way1
# def change_student(lst):
#     name = input("请输入要修改的学生姓名：")
#     for n in lst:
#         if name == n['name']:
#             lst.remove(n)
#             age = int(input("请输入新学生年龄："))
#             score = int(input("请输入新学生成绩："))
#             N = {'name': name, 'age': age, 'score': score}
#             lst.append(N)
#             break
#     return(lst)
# WAY2
# 修改学生信息

def change_student(lst):
    name = input("请输入要修改的学生姓名：")
    try:
        for n in lst:
            if name == n.get_name():
                lst.remove(n)
                age = int(input("请输入新学生年龄："))
                score = int(input("请输入新学生成绩："))
                lst.append(Student(name, age, score))
                return lst
    except OSError:
        output_student(lst)


# 按照成绩从上到下排序
def score_u2l(lst):
    def k(n):
        return n.get_score()
    m = sorted(lst, key=k, reverse=True)
    return output_student(m)


# 按照成绩从下到上排序
def score_l2u(lst):
    def k(n):
        return n.get_score()
    m = sorted(lst, key=k, reverse=False)
    return output_student(m)


# 按照年龄从下到上排序
def age_l2u(lst):
    def k(n):
        return n.get_age()
    m = sorted(lst, key=k, reverse=True)
    return output_student(m)


# 按照年龄从上到下排序
def age_u2l(lst):
    def k(n):
        return n.get_age()
    m = sorted(lst, key=k, reverse=False)
    return output_student(m)


# 输入学生信息并存入文件
def input_student_info(lst):
    try:
        f = open("si.txt", 'wt')
        for d in lst:
            d.save_info(f)
        f.close()
        print('文件创建完成并关闭')
    except OSError:
        print('写文件失败')


# 从文件中读取学生信息
def read_info_txt():
    rl = []
    try:
        f = open("si.txt", 'rt')
        lst = f.readlines()
        for line in lst:
            name, age, score = line.rstrip().split(' ')
            age = int(age)
            score = int(score)
            rl.append(Student(name, age, score))
        f.close()
        # print_list(rl)
        return rl
    except OSError:
        print('文件打开失败')
