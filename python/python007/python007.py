# L = [1, 2, 3, 4, 5, ]
# L.pop(1)
# L.pop(1)
# print(L)
# 
# s = "ABCD"
# L = list(s)
# L2 = reversed(s)
# print(L, L2)

# L = [5, 4, 7, 2, 1]
# L2 = [str(x ** 2) for x in L]
# s = '+'.join(L2)

# # 在字典中找四季
# d = P1:dict([
#     ('1', '春季有１，２，３月'), 
#     ('2', '春季有４，５，６月'), 
#     ('3', '春季有７，８，９月'), 
#     ('4', '春季有１０，１１，１２月')])
# print(d)
# a = str(input('请输入整数'))
# if a in d:
#     print(d[a])
# else:
#     print('without')

# # WAY2:
# season = {}
# season[1] = '春季有1, 2, 3月'
# season[2] = '夏季有4, 5, 6月'
# season[3] = '秋季有7, 8, 9月'
# season[4] = '冬季有10,11,12月'
# a = str(input('请输入整数'))
# if a in season:
#     print(season[a])
# else:
#     print('without')


# # 输入一段字符串，打印出这个字符串中出现过的字符的出现次数
# #   如:
# #     输入:
# #       abcdabcaba
# #     打印:
# #       a: 4次
# #       b: 3次
# #       d: 1次
# #       c: 2次
# #     注:
# #        不要求打印的顺序
# d = {}
# s = str(input('请输入一个字符串'))
# for x in s:
#     # x = str(x)
#     if x in d:
#         # d[x] = str(int(d[x]) + 1)
#         d[x] += 1
#     else:
#         d[x] = 1
# # print(d)
# for y, z in d.items():
#     print(y, ':', z, '次')


#  # 有字符串的列表如下:
#  #    L = ['tarena', 'xiaozhang', 'tyke']
#  #    用上述列表生成如下字典:
#  #      d = {'tarena': 6, 'xiaozhang': 9, 'tyke':4}
#  #    注:
#  #      字典的值为键的长度
# L = ['tarena', 'xiaozhang', 'tyke']
# d = {y: len(y) for y in L}
# print(d)

# # Mysql_order 已知有两个等长的列表 list1  和 list2
# #   以list1中的元素为键，以list2中的元素为值，生成相应的字典
# #   list1 = [1001, 1002, 1003, 1004]
# #   list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']
# #   生成的字典为：
# #     {1001: 'Tom', 1002:'Jerry', .....}
# list1 = [1001, 1002, 1003, 1004]
# list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']
# d = {}
# for x in range(0, len(list1)):
#     d[list1[x]] = list2[x]
# print(d)
# # WAY2
# d = {list1[x]: list2[x] for x in range(0, len(list1))}
# print(d)



# # 1.写一个程序模拟现实电子字典
# # 1）输入一些单词和解释，将单词作为键，将解释作用值，
# # 将这些数据输入到字典中，当输入 到字典中，当输入空单词时结束输入
# # 2）输入要查找的词，给出该单词的解释，如果单词不存在则提示用户不存在该单词
# dictionry = {}
# while True:
#     word = input("请输入单词：")
#     if word is not '':
#         explan = input("请输入翻译：")
#         dictionry[word] = explan
#     else:
#         break

# while True:
#     check = str(input("请输入要查找的单词："))
#     if check != '':
#         print(dictionry[check])
#     else:
#         print('该单词不村在')
#         break




# # 2. 输入任意个学生的姓名，年龄，成绩，每个学生的信息存入字典中，然后放入至列表中，每个学生的信息需要手动输入
# # 当输入姓名为空时结束输入:
# #   如:
# #     请输入姓名:  xiaozhang
# #     请输入年龄:  20
# #     请输入成绩:  100
# #     请输入姓名:  xiaoli
# #     请输入年龄:  18
# #     请输入成绩:  98#     请输入姓名:  <回车> 结束输入
# #   要求内部存储格式如下:
# #   [{'name':'xiaozhang', 'age':20, 'score':100}, 
# #    {'name':'xiaoli', 'age':18, 'score':98}]
# #   打印所有学生的信息如下:
# #   +---------------+----------+----------+
# # 　　|     name      |   age    |   score  |
# #   +---------------+----------+----------+
# #   |   xiaozhang   |    20    |   100    |
# #   |     xiaoli    |    18    |    98    |
# #   +---------------+----------+----------+
Lst = []
while True:
    name = input("请输入学生姓名：")
    if name is '':                  #not n
        break
    else:
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生成绩："))
        N = {'name': name, 'age': age, 'score': score}
    Lst.append(N)
for s in Lst:
    s = s['name']
    long = [len([x for x in s if ord(x) > 127])]
a = max(long)
print(a)
L = max(len(n['name']) for n in Lst) + a * 4
print('+' + '-' * (L - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
print(
    '|' + 'name'.center(L - 2) +
    '|' + 'age'.center(11) +
    '|' + 'score'.center(11) +
    '|')
print('+' + '-' * (L - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
for n in Lst:
   # print(
   #  '|' + n['name'].center(L - 2) +
   #  '|' + str(n['age']).center(11) +
   #  '|' + str(n['score']).center(11) +
   #  '|')
   print(
    '|%s|%s|%s|' % (n['name'].center(L - 2), str(n['age']).center(11), str(n['score']).center(11)))
print('+' + '-' * (L - 2) + '+' + '-' * 11 + '+' + '-' * 11 + '+')
# Mysql_order 　（）是元组
#     ［］是列表
#     ｛｝是字典
# ２．　列表的方法
#     列表的推导式注意元素所代表的含义以及和表达式的关系
#     字典的读取是d['键']
