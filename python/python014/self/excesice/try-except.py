# 写一个函数 get_score() 来获取学生成绩,
#     要求用户输入 1~100的整数,输果输入出现异常,返此函数返回0,
#     否则返回用户输入的成绩
# 示例:
#     def get_score():
#         ...
#     score = get_score()
#     print("学生的成绩是:", score)


# WAY1
# 在调用处加入异常处理语句进行处理


def get_score():
    n = int(input("请输入学生的车成绩"))
    if 0 <= n <= 100:
        return n
    else:
        return 0


try:
    score = get_score()
except ValueError:
    score = 0
print("学生的成绩是:", score)


# WAY2


def get_score2():
    try:
        n = int(input("请输入学生的车成绩"))
    except ValueError:
        return 0
    if 0 <= n <= 100:
        return n
    else:
        return 0


score = get_score2()
print("学生的成绩是:", score)
