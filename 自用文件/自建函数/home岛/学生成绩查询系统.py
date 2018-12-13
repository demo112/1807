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