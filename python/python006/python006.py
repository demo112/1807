# L = [3, 5]
# L[0:0] = [1, 2]
# L[3:3] = [4]
# L[5:5] = [6]
# L[::] = L[::-1]
# del L[-1]
# print(L)\

# L = []
# while True:
#     a = int(input("请输入整数") or '0')
#     if a == -1:
#         break
#     else:
#         L[0:0] = [a]
# print(len(L))
# print(sum(L) / (len(L) or 1))
# print(max(L + [0]))
# print(min(L + [0]))


# L = []
# while True:
#     a = int(input("请输入整数") or '0')
#     if a < 0:
#         break
#     else:
#         L.append(a)
# print(L)
# L2 = L.copy()

# L2.sort(reverse=True)
# print(max(L2))
# a = L2.count(max(L2))
# L2[0:a] = []
# print(max(L2))


# L = [x for x in range(0, 101) if x % 2 == 1]
# L2 = [x ** 2 for x in range(2, 10, 2)]

# 未成功
# s = '100,200,300,500,800'
# L = s.split(',')

# 未成功
# L = [sum() for x in range(0, 40)]
# print(L)

# 找范围内偶数
# begin = int(input("输入开始"))
# end = int(input("输入结束")) + 1
# L = [x for x in range(begin, end) if x % 2 == 0]
# print(L)

# [1, 2, 3] * [10, 20, 30]列表
# L = [x + y
#         for y in [1, 2, 3]
#             for x in [10, 20, 30]]
# print(L)

# L = [x + y
#         for y in ['1', '2', '3']
#             for x in ['A', 'B', 'C']]
# print(L)

# L = [x + y
#         for y in '123'
#             for x in 'ABC']
# print(L)




# 有一些数存于列表中
# 如L = [5, 609, 59, 4946, 494, 89, 44, 79, 489, 1, 4610, 494, 89, 1, 20, 6, 14]
# 将L 中出现的数字存于L2列表中
# 要求：
# #     去重
# L = [5, 609, 59, 4946, 44, 79, 494, 89, 44, 79, 
# 489, 1, 4610, 494, 89, 44, 79, 20, 6, 14]
# L2 = []
# L3 = []
# L.sort(reverse=False)
# for x in L:
#     if x not in L2:
#         L2 += [x]
#     else:
#         if x not in L3:
#             L3 += [x]
#         else:
#             pass
# print(L2, '\n', L3, sep='')

# # WAY2:
# L = [5, 609, 59, 4946, 44, 79, 494, 89, 44, 79, 
# 489, 1, 4610, 494, 89, 44, 79, 20, 6, 14]
# L2 = []
# L3 = []
# L.sort(reverse=False)
# for x in L:
#     if L.count(x) == 2:
#         L3 += [x]
#     if L.count(x) >=2:
#         L.remove(x)
#     L2.append(x)
# print(L2, '\n', L3, sep='')


#     将列表中出现２次的数字存于L3中另保留一份


# # 计算出１００以内的素数，将这些素数存于列表内打印出来

# s = 0
# i = 100
# L = []
# for i in range(0,100):
#     for y in range(2,i):
#         if i % y == 0:
#             break
#     else:
#         L += [i]
# print(L)

# # 生成前４０个斐波那契数列
# # 将其存于列表中答打印这些数
L = [1, 1]
while len(L) < 10:
    s = L[0]
    s = L[len(L) - 1] + L[len(L) - 2]
    L += [s]
# # WAY2
# #     L.append(L[-1] + L[-2])
print(L)
