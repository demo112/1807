from .menu import menu


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

# 输入学生信息并存入文件
def input_student_info(lst):
    f = open("si.txt", 'wt')
    for d in lst:
        a = str(d.name) + str(d.age) + str(d.score) + '\n'
        b = ' '.join(a)
        f.write(b)
    f.close()
    print('文件创建完成并关闭')


# 从文件中读取学生信息
def read_info_txt():
    rl = []
    try:
        f = open("si.txt", 'rt')
        lst = f.readlines()
        for line in lst:
            s = line.rstrip()
            name, age, score = s.split(' ')
            age = int(age)
            score = int(score)
            rl.append(Student(name, age, score))
        f.close()
        print_list(rl)
        return rl
    except OSError:
        print('文件打开失败')


# 获取名字中中文的个数
def get_chinese_char_count(lst):
    count = 0  # 先假设个数为0
    ls = []
    for x in lst:
        for ch in x.name:
            # 如果ch为中文字典,则count 做加一操作
            if ord(ch) > 127:
                count += 1
        ls += [count]
    return max(ls)


# 打印列表
def print_list(lst):
    n = get_chinese_char_count(lst)
    k = int(max(len(n.name) for n in lst) + n + 10)
    print('+' + '-' * k + '+' + '-' * 11 + '+' + '-' * 11 + '+')
    print(
        '|' + 'name'.center(k) +
        '|' + 'age'.center(11) +
        '|' + 'score'.center(11) +
        '|')
    print('+' + '-' * k + '+' + '-' * 11 + '+' + '-' * 11 + '+')
    for m in lst:
        if get_chinese_char_count([m]) == 0:
            print('|%s|%s|%s|' % (str(m.name).center(k),
                                  str(m.age).center(11),
                                  str(m.score).center(11)))
        else:
            print('|%s|%s|%s|' % (str(m.name).center(k - int(n * 2 / 3)),
                                  str(m.age).center(11),
                                  str(m.score).center(11)))

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
        if name == n.name:
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
            if name == n.name:
                n.age = int(input("请输入新学生年龄："))
                n.score = int(input("请输入新学生成绩："))
        return lst
    except:
        output_student(lst)


# 按照成绩从上到下排序
def score_u2l(lst):
    def k(n):
        return n.score
    m = sorted(lst, key=k, reverse=True)
    return output_student(m)


# 按照成绩从下到上排序
def score_l2u(lst):
    def k(n):
        return n.score
    m = sorted(lst, key=k, reverse=False)
    return output_student(m)


# 按照年龄从下到上排序
def age_l2u(lst):
    def k(n):
        return n.age
    m = sorted(lst, key=k, reverse=True)
    return output_student(m)


# 按照年龄从上到下排序
def age_u2l(lst):
    def k(n):
        return n.age
    m = sorted(lst, key=k, reverse=False)
    return output_student(m)
