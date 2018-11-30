def input_student():
    # Lst = [{'name': '4', 'age': 4, 'score': 4}, {'name': '2', 'age': 2, 'score': 2},
    #        {'name': '3', 'age': 3, 'score': 3}, {'name': '1', 'age': 1, 'score': 1}]
    Lst = []
    while True:
        name = input("请输入学生姓名：")
        if name is not '':
            age = int(input("请输入学生年龄："))
            score = int(input("请输入学生成绩："))
            N = {'name': name, 'age': age, 'score': score}
            Lst.append(N)
        else:
            break
    return(Lst)
def output_student(Lst):
    for s in Lst:
        s = s['name']
        long = [len([x for x in s if ord(x) > 127])]
    a = max(long)
    # print(a)
    L = max(len(n['name']) for n in Lst) + a * 2 + 10
    print('+' + '-' * (L - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
    print(
        '|' + 'name'.center(L - 2) +
        '|' + 'age'.center(11) +
        '|' + 'score'.center(11) +
        '|')
    print('+' + '-' * (L - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
    for n in Lst:
       print(
        '|%s|%s|%s|' % (n['name'].center(L - 2 - a), str(n['age']).center(11), str(n['score']).center(11)))
    print('+' + '-' * (L - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
def myui():
    a = "1)  添加学生信息"
    b = "2)  显示学生信息"
    c = "3)  删除学生信息"
    d = "4)  修改学生信息"
    e = "5)  按学生成绩高-低显示学生信息"
    f = "6)  按学生成绩低-高显示学生信息"
    g = "7)  按学生年龄高-低显示学生信息"
    h = "7)  按学生年龄低-高显示学生信息"
    q = "q)  退出"


    L = 34
    print('+' + '-' * (L + 22) + '+')
    print('|' + a + ' ' * (L - len(a)) + '|')
    print('|' + b + ' ' * (L - len(b)) + '|')
    print('|' + c + ' ' * (L - len(c)) + '|')
    print('|' + d + ' ' * (L - len(d)) + '|')
    print('|' + e + ' ' * (L - len(e) - 5) + '|')
    print('|' + f + ' ' * (L - len(f) - 5) + '|')
    print('|' + g + ' ' * (L - len(g) - 5) + '|')
    print('|' + h + ' ' * (L - len(h) - 5) + '|')
    print('|' + q + ' ' * (L - len(q) + 5) + '|')
    print('+' + '-' * (L + 22) + '+')
    choose = str(input("请选择："))
    return(choose)
def delete_student(Lst):
    name = input("请输入学生姓名：")
    for n in Lst:
        if name == n['name']:
            Lst.remove(n)
            break
    return(Lst)
# way1
# def change_student(Lst):
#     name = input("请输入要修改的学生姓名：")
#     for n in Lst:
#         if name == n['name']:
#             Lst.remove(n)
#             age = int(input("请输入新学生年龄："))
#             score = int(input("请输入新学生成绩："))
#             N = {'name': name, 'age': age, 'score': score}
#             Lst.append(N)
#             break
#     return(Lst)
# WAY2
def change_student(Lst):
    name = input("请输入要修改的学生姓名：")
    for n in Lst:
        if name == n['name']:
            age = int(input("请输入新学生年龄："))
            score = int(input("请输入新学生成绩："))
            N = {'name': name, 'age': age, 'score': score}
            n.update(N)
            break
    return(Lst)


def score_U2L(Lst):
    def k(n):
        return n['score']
    LU2L = sorted(Lst, key=k, reverse=True)
    return output_student(LU2L)

def score_L2U(Lst):
    def k(n):
        return n['score']
    LU2L = sorted(Lst, key=k, reverse=False)
    return output_student(LU2L)
def age_L2U(Lst):
    def k(n):
        return n['age']
    LU2L = sorted(Lst, key=k, reverse=True)
    return output_student(LU2L)
def age_U2L(Lst):
    def k(n):
        return n['age']
    LU2L = sorted(Lst, key=k, reverse=False)
    return output_student(LU2L)







def main():
    Lst = []
    while True:
        choose = myui()
        if choose == 'q':
            break
        elif choose == '1':
            Lst += input_student()
        elif choose == '2':
            output_student(Lst)
        elif choose == '3':
            Lst = delete_student(Lst)
        elif choose == '4':
            Lst = change_student(Lst)
        elif choose == '5':
            score_U2L(Lst)
        elif choose == '6':
            score_L2U(Lst)
        elif choose == '7':
            age_L2U(Lst)
        elif choose == '8':
            age_U2L(Lst)
        elif choose == 'show':
            print(Lst)



main()


# def mysum(n):
#     S = n / 2 * (n + 1)
#     return(S)
# print(mysum(1000000000000000000))

# def mysum(n):
#     L = 0
#     for x in range(1,n):
#         L += x
#     return L
# print(mysum(1000000000000000000))