# 在班级所有人的名字中的名字中随机抽取一个人的名字且不可复现
import random as R


def input_name():
    lst = []
    while True:
        try:
            name = input('请输入姓名')
            if name:
                lst.append(str(name))
            else:
                raise ZeroDivisionError
        except TypeError:
            print('您输入的姓名有误请重新输入')
        except ZeroDivisionError:
            print('输入结束')
            # print(lst)

            return lst


def InFile(lst):
    try:
        f = open('student_name.txt', 'xt')
        for x in lst:
            f.writelines(x)
            f.writelines('\n')
        f.flush()
        f.close()
    except FileExistsError:
        f = open('student_name.txt', 'wt')
        for x in lst:
            f.writelines(x)
            f.writelines('\n')
        f.flush()
        f.close()


def choo(lst):
    a = R.choice(lst)
    lst.remove(a)
    InFile(lst)
    return a, lst


def read_file():
    rls = []
    f = open('student_name.txt', 'r')
    ls = f.readlines()
    try:
        for x in ls:
            rls.append(x.strip())
    except StopIteration:
        f.close()
    finally:
        f.close()
        return rls


def read_checked_file():
    lst = []
    f = open('checked_name.txt', 'rt')
    try:
        for x in f.readlines():
            lst.append(x.strip())
    except StopIteration:
        pass
    f.close()
    return lst


def InFile_checked(a):
    try:
        f = open('checked_name.txt', 'at')
        f.writelines(a)
        f.writelines('\n')
        f.flush()
    except FileExistsError:
        f = open('checked_name.txt', 'wt')
        f.writelines(a)
        f.writelines('\n')
        f.flush()
        f.close()
    menu()


def menu():
    print('1:Input')
    print('2:Choise')
    print('3:All_people')
    print('4:Checked')
    print('0:Quit')

    choose = int(input('Please make a choice'))
    if choose == 1:
        InFile(input_name())
        menu()
    elif choose == 2:
        # print(read_file())
        # print(read_file())
        a, lst = choo(read_file())
        print(a)
        InFile_checked(a)
    elif choose == 3:
        print(read_file())
        menu()
    elif choose == 4:
        print(read_checked_file())
        menu()
    elif choose == 0:
        print("程序结束")

    # if choose == 4:2
    #     name_list = input_name()
    # if choose == 5:
    #     name_list = input_name()


menu()
