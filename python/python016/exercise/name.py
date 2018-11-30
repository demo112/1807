# 自己写一个文件 'info.txt' 内部存一些文字信息
#     如:
#       张三 20 100
#       李四 21 96
#       小王 22 98
#     写程序将这些数据读取出来，打印到终端上
# 此示例示意文件的打开和关闭

#
# try:
#     f = open("si.txt")
#     print("文件打开成功")
#     lst = f.readlines()
#     print(lst)
#     for x in range(len(lst)):
#         print(lst[x][0] + '今年' +
#               lst[x][1] + '岁，成绩是：' +
#               lst[x][2], end='')
#     print()
#     f.close()
#     print("文件已关闭")
# except OSError:
#     print('文件打开失败')

# WAY2


def read_info_txt():
    rl = []
    try:
        f = open("si.txt", 'rt')
        lst = f.readlines()
        for line in lst:
            s = line.strip()
            name, age, score = s.split()
            age = int(age)
            score = int(score)
            rl.append({"name": name, "age": age, "score": score})
        f.close()
        return rl
    except OSError:
        print('文件打开失败')


def print_info(lst):
    for d in lst:
        print(d['name'], '今年',
              d['age'], '岁，成绩是：',
              d['score'])

lst = read_info_txt()
print_info(lst)
