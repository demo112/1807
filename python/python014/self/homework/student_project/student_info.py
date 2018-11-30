
from student_project.menu import menu
# 这个位置有毛病，待修改
# 用finally
def input_student():
    lst = []
    while True:
        try:
            name = input("请输入学生姓名：")
            if len(name) == 0:
                print("学生信息录入结束")
                break
            elif len(name) != 0:
                age = int(input("请输入学生年龄："))
                score = int(input("请输入学生成绩："))
                m = {'name': name, 'age': age, 'score': score}
                lst.append(m)
            else:
                pass
        except ValueError:
            print("您输入的学生信息有误")
            break
    return lst


def get_chinese_char_count(lst):
    count = 0  # 先假设个数为0
    ls = []
    for x in lst:
        for ch in x['name']:
            # 如果ch为中文字典,则count 做加一操作
            if ord(ch) > 127:
                count += 1
        ls += [count]
    return max(ls)


def output_student(lst):
    def output_st(lst):
        n = get_chinese_char_count(lst)
        k = int(max(len(n['name']) for n in lst) + n + 10)
        print('+' + '-' * k + '+' + '-' * 11 + '+' + '-' * 11 + '+')
        print(
            '|' + 'name'.center(k) +
            '|' + 'age'.center(11) +
            '|' + 'score'.center(11) +
            '|')
        print('+' + '-' * k + '+' + '-' * 11 + '+' + '-' * 11 + '+')
        for m in lst:
            if get_chinese_char_count([m]) == 0:
                print('|%s|%s|%s|' % (str(m['name']).center(k),
                                      str(m['age']).center(11),
                                      str(m['score']).center(11)))
            else:
                print('|%s|%s|%s|' % (str(m['name']).center(k - int(n * 2 / 3)),
                                      str(m['age']).center(11),
                                      str(m['score']).center(11)))

        # print('aaa'.center(k), 'age'.center(11))# , str(n['score']).center(11))
        print('+' + '-' * k + '+' + '-' * 11 + '+' + '-' * 11 + '+')
    try:
        output_st(lst)
    except (TypeError, ValueError):
        print("您还没有输入学生信息")
        menu()

def delete_student(lst):
    name = input("请输入学生姓名：")
    for n in lst:
        if name == n['name']:
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


def change_student(lst):
    name = input("请输入要修改的学生姓名：")
    for n in lst:
        if name == n['name']:
            age = int(input("请输入新学生年龄："))
            score = int(input("请输入新学生成绩："))
            x = {'name': name, 'age': age, 'score': score}
            n.update(x)
            break
    return lst


def score_u2l(lst):
    def k(n):
        return n['score']
    m = sorted(lst, key=k, reverse=True)
    return output_student(m)


def score_l2u(lst):
    def k(n):
        return n['score']
    m = sorted(lst, key=k, reverse=False)
    return output_student(m)


def age_l2u(lst):
    def k(n):
        return n['age']
    m = sorted(lst, key=k, reverse=True)
    return output_student(m)


def age_u2l(lst):
    def k(n):
        return n['age']
    m = sorted(lst, key=k, reverse=False)
    return output_student(m)


# def text():
#     def main():
#         lst = []
#         while True:
#             choose = menu()
#
#             if choose == 'q':
#                 break
#             elif choose == '1':
#                 lst += input_student()
#             elif choose == '2':
#                 output_student(lst)
#             elif choose == '3':
#                 lst = delete_student(lst)
#             elif choose == '4':
#                 lst = change_student(lst)
#             elif choose == '5':
#                 score_u2l(lst)
#             elif choose == '6':
#                 score_l2u(lst)
#             elif choose == '7':
#                 age_l2u(lst)
#             elif choose == '8':
#                 age_u2l(lst)
#             elif choose == 'show':
#                 print(lst)
#
#
#     main()
#
#
# text()
