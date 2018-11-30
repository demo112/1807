
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


def input_phonenumber(lst):
    try:
        f = open("si.txt", 'w')
        for d in lst:
            a = [str(d['name']), str(d['age']), str(d['score'])]
            f.write(' '.join(a))
            f.write('\n')       # 写入换行符，用来区分行
        print('文件创建完毕')
        f.close()
    except OSError:
        print("写入文件失败")

# lst = [{'name': 'dq', 'age': '23', 'score': '99'},
#        {'name': 'ca', 'age': '1', 'score': '1'},
#        {'name': 'casc', 'age': '3', 'score': '3'},
#        {'name': 'asv', 'age': '5', 'score': '5'}]
lst = input_student()
input_phonenumber(lst)