'''该函数通过交互揭界面来返回用户的选择'''


def menu():
    a = "1)  添加学生信息"
    b = "2)  显示学生信息"
    c = "3)  删除学生信息"
    d = "4)  修改学生信息"
    e = "5)  按学生成绩高-低显示学生信息"
    f = "6)  按学生成绩低-高显示学生信息"
    g = "7)  按学生年龄高-低显示学生信息"
    h = "7)  按学生年龄低-高显示学生信息"
    q = "q)  退出"
    lst = 34
    print('+' + '-' * (lst + 22) + '+')
    print('|' + a + ' ' * (lst - len(a)) + '|')
    print('|' + b + ' ' * (lst - len(b)) + '|')
    print('|' + c + ' ' * (lst - len(c)) + '|')
    print('|' + d + ' ' * (lst - len(d)) + '|')
    print('|' + e + ' ' * (lst - len(e) - 5) + '|')
    print('|' + f + ' ' * (lst - len(f) - 5) + '|')
    print('|' + g + ' ' * (lst - len(g) - 5) + '|')
    print('|' + h + ' ' * (lst - len(h) - 5) + '|')
    print('|' + q + ' ' * (lst - len(q) + 5) + '|')
    print('+' + '-' * (lst + 22) + '+')
    choose = str(input("请选择："))
    return choose
