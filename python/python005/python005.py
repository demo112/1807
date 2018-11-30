
# 任意输入一段字符串
# 计算出输入字符a的个数，并打印出字符
# 计算出空格的个数，并打印出个数


# s = input("请输入字符串")
# h = input("请输入要检索字符")
# count_a = 0

# for c in s:
#     if c == h:
#         count_a += 1
# print(count_a)


# for_else.py
# 输入一段字符串，判断这个字符串是否有h 并打印结果

# s = input("请输入：")
# for ch in s:
#     if ch == "H":
#         print(s, "中含有字符＇Ｈ＇")
#         break
# else:
#     print(s, '中不包含＂Ｈ＂')


# # 用ｗｈｉｌｅ实现

# s = input("请输入：")
# i = 0
# while i< len(s):
#     ch = s[i]
#     if ch == "H":
#         print(s, "中含有字符＇Ｈ＇")
#         break
#     i += 1
# else:
#     print(s, '中不包含＂Ｈ＂')


# # range.py
# i = 1
# while i <= 20:
#     for x in range(1, 21):
#         print(x, end=" ")
#     print()
#     i += 1


# 计算１，３，５，　　　　　９９的和
# s = 0
# for x in range(1, 100, 2):
#     s = s + x
# print(s)

# n = 1
# s = 0
# while n <= 99:
#     s += n
#     n += 2
# print(s)



# for x in range(0, 4):
#     print(x)
# print("绑定的是", x)

# for x in range(4, 0):    #报错
#     print(x)
# print("绑定的是", x)



# for_range_time.py
# i = 9

# for x in range(1,i):    #b值已经生成，range(1, 6)不会被改变
#     print(x)
#     i -= 1





# for x in "ABC":
#     for y in "123":
#         print(x + y)

# 99乘法表
# for x in range(1,10):
#     for y in range(1,10):

#         print(x, "*", y, end=" ")
#         b -= 1
#     print()
#     a -= 1


# # 求１００以内由那些数与自身加一的成绩在对１１求余等于８

# for x in range(1, 101):
#     if x * (x + 1) % 11 == 8:
#         print(x)
# # s输入一个数，打下方正方形（for）
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# i = int(input("请输入整数") or '0') + 1

# for line in range(1, i):
#     for y in range(1, i):
#         print(y, end=' ')
#     print()

# # 请输入整数11
# #  1  2  3  4  5  6  7  8  9 10 11 
# #  2  3  4  5  6  7  8  9 10 11 12 
# #  3  4  5  6  7  8  9 10 11 12 13 
# #  4  5  6  7  8  9 10 11 12 13 14 
# #  5  6  7  8  9 10 11 12 13 14 15 
# #  6  7  8  9 10 11 12 13 14 15 16 
# #  7  8  9 10 11 12 13 14 15 16 17 
# #  8  9 10 11 12 13 14 15 16 17 18 
# #  9 10 11 12 13 14 15 16 17 18 19 
# # 10 11 12 13 14 15 16 17 18 19 20 
# # 11 12 13 14 15 16 17 18 19 20 21 
# i = int(input("请输入整数") or '0')
# for line in range(1, i + 1):
#     for y in range(line, i + line):
#         print("%2d" % y, end=' ')
#     print()

# # 用程序生成如下字符串
# # AbCdEfGhIjKlMnOpQrStUvWxYz 
# s = ''
# for x in range(26):
#     if x % 2 == 0:
#         s += chr(ord('A') + x)
#     else:
#         s += chr(ord('a') + x)
# print(s)

# # 方法二：
# for x in range(26):
#     if x % 2 == 0:
#         s += chr(ord('A') + x)
#     else:
#         s += chr(ord('A') + x).lower()
# print(s)

# # AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz
# s = ''
# for x in range(26):
#     s += chr(ord('A') + x) + chr(ord('A') + x).lower()
# print(s)

# 
# s = ''
# for x in range(0,65536):
#     s = chr(x)
#     print(s, end='')



# for x in range(10):
#     if x % 2 == 0:
#         continue
#     print(x)

# x = 0
# while x < 5:
#     if x == 2:
#       x += 1
#       continue
#     print(x)


# L = []
# n = m =0
# while True:
#     i = input('请输入：')
#     if i != '':
#         L += [i]
#         n += 1
#         m += len(i)
#     else:
#         break
# print(L)
# print(n)
# print(m)


# 找素数
# s = 0
# i = int(input("请输入区间："))
# for x in range(i + 1):
#     for y in range(2,x):
#         if x % y == 0:
#             break
#     else:
#         print(x)

# s = 0
# i = int(input("请输入一个数"))
# for y in range(2,i):
#     if i % y == 0:
#         print("N")
#         break
# else:
#     print("Y")

# 打印圣诞树
# h = int(input("请输入一个整数"))
# for x in range(0, h):
#     s = "*" * int(x) + '*' + "*" * int(x)
#     s = s.center(2 * h - 1)
#     print(s)
# i = 1
# while True:
#     if i <= h:
#         print("*".center(2 * h - 1))
#         i += 1
#     else:
#         break


# Start = int(input("输入开始数字"))
# End = int(input("输入结束数字")) + 1
# for x in range(Start, End):
#     n = len(str(x))
#     s = e = 0
#     for m in range(0, n):
#         e = int(str(x)[m])
#         s += e ** 3
#     if s == x:
#         print(x)
#     else:
#         continue


# Start = int(input("输入开始数字"))
# End = int(input("输入结束数字")) + 1
# for x in range(Start, End):
#     n = len(str(x))
#     s = e = 0
#     for m in range(0, n):
#         e = int(str(x)[m])
#         s += e ** 5
#     if s == x:
#         print(x)
#     else:
#         continue





# Start = int(input("输入开始数字"))
# End = int(input("输入结束数字")) + 1
# for x in range(Start, End):
#     s = str(x)
#     a = int(s[0])
#     b = int(s[1])
#     c = int(s[2])
#     if x == (a ** 3) + (b ** 3) + (c ** 3):
#         print(x)
#     else:
#         continue