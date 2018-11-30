from menu import menu


def input_student():
    # lst = [{'name': '4', 'age': 4, 'score': 4}, {'name': '2', 'age': 2, 'score': 2},
    #        {'name': '3', 'age': 3, 'score': 3}, {'name': '1', 'age': 1, 'score': 1}]
    lst = []
    while True:
        name = input("请输入学生姓名：")
        if name is not '':
            age = int(input("请输入学生年龄："))
            score = int(input("请输入学生成绩："))
            m = {'name': name, 'age': age, 'score': score}
            lst.append(m)
        else:
            break
    return lst


def output_student(lst):
    for s in lst:
        s = s['name']
        long = [len([x for x in s if ord(x) > 127])]
        n = int(max(long))
    k = max(len(n['name']) for n in lst) + n * 2 + 10
    print('+' + '-' * (k - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
    print(
        '|' + 'name'.center(k - 2) +
        '|' + 'age'.center(11) +
        '|' + 'score'.center(11) +
        '|')
    print('+' + '-' * (k - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
    for n in lst:
        print(
            '|%s|%s|%s|' % (n['name'].center(k - 2 - n), str(n['age']).center(11), str(n['score']).center(11)))
    print('+' + '-' * (k - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')


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
