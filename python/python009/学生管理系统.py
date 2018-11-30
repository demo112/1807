def input_student():
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
    e = "q)  退出        "
    L = 16 + 10
    print('+' + '-' * (L - 2) + '+')
    print('|' + a + ' ' * 8 + '|')
    print('|' + b + ' ' * 8 + '|')
    print('|' + c + ' ' * 8 + '|')
    print('|' + d + ' ' * 8 + '|')
    print('|' + e + ' ' * 8 + '|')
    print('+' + '-' * (L - 2) + '+')
    choose = str(input("请选择："))
    return(choose)
def delete_student(Lst):
    name = input("请输入学生姓名：")
    for n in Lst:
        if name == n['name']:
            Lst.remove(n)
            break
    return(Lst)
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