# python02.py

# pi = 3.14
# i = int(pi,base=10)
# f = pi-i
# print(f == 0.14)




# s = input("请输入一些文字：")
# print('您刚才输入的内容是',s)

# s2 = input()
# print('您刚才第二次输入的内容是',s2)

# r = input("请输入一个整数：")
# r = int(r)
# print(r,'/2=',r/2,sep='')

# h = input('请输入当前小时：')
# h = int(h)
# m = input('请输入当前分钟：')
# m = int(m)
# s = input('请输入当前秒：')
# s = int(s)
# s += h*60*60+m*60
# print("当前时间据0时过去了：",s,"秒")

# x = int(input('请输入x:'))
# y = int(input('请输入y:'))
# print(x,'+',y,'=',x+y)
# print(x,'*',y,'=',x*y)
# print(x,'**',y,'=',x**y)

# x = int(input('请输入一个整数：'))
# if x==x:
#     if x > 100:
#         print('x大于１００')
#     elif x < 0:
#         print('x小于０')
#     elif 80 < x < 100:
#         print('x在８０～１００之间')

# season = int(input("请输入季节"))
# if season == 1 :
#     print("１～３月")
# elif season==2:
#     print("4~6月")
# elif season==3:
#     print("7~9月")
# elif season==4:
#     print("10~12月")
# else:
#     print("您输错了")


# month = int(input("请输入月份"))
# if 1<=month<=3:
#     print("春季")
# elif 4<=month<=6:
#     print("夏季")
# elif 7<= month<=9:
#     print("秋季")
# elif 10<= month<=12:
#     print("冬季")
# else:
#     print("您输错了")



# number = int(input("请输入一个数字"))
# number = number if number>=0 else -number
# print("该数的绝对值是：",number)

# number = int(input("请输入一个数字"))
# if number>=0:
#     print("该数的绝对值是：",number)
# else:
#     print("该数的绝对值是：",-number)

# number = int(input("请输入一个数字"))
# if number<0:
#     number = -number
# print("该数的绝对值是：",number)

# score=input("请输入学生成积")or'0'
# print(score)
# score=int(score)
# print(score)


# #-----------------------------------------------------------------------------------------------------------------------------------------------------------
# money = 13
# gap = int(input("请输入行驶公里数：") or '0')
# if gap<=3:
#     pass
# else:
#     if gap<=15:
#         money = 13 + 2.3*(gap-3)
#     elif gap>15:
#         money = 13 + 2.3*(15-3) + 3.45*(gap - 15)
# money = int(round(money,0))
# print("您此次行程：",gap,"公里","共计车费：",money,"元")
# #-----------------------------------------------------------------------------------------------------------------------------------------------------------
# ascore = int(input("请输入A课程成绩：") or '0')
# bscore = int(input("请输入B课程成绩：") or '0')
# cscore = int(input("请输入C课程成绩：") or '0')
# dscore = (ascore + bscore + cscore) / 3
# if ascore > bscore and ascore > cscore:
#     Max = ascore
# elif bscore > ascore and bscore > cscore:
#     Max = bscore
# else:
#     Max = cscore

# if ascore < bscore and ascore < cscore:
#     Min = ascore
# elif bscore < ascore and bscore < cscore:
#     Min = bscore
# else:
#     Min = cscore
# print("这三门的平均成绩是：", dscore, "最高成绩是：", Max, "最低成绩是", Min)
# #-----------------------------------------------------------------------------------------------------------------------------------------------------------
# year = int(input("请输入年份：") or '0')
# if year%400==0:
#     print("该年份是润年")
# elif year%100==0:
#     print("该年份不是润年")
# elif year%4==0:
#     print("该年份是润年")
# else:
#     print("该年份不是润年")
# #-----------------------------------------------------------------------------------------------------------------------------------------------------------
# weight = int(input("请输入体重（kg）：") or '0')
# leight = int(input("请输入身高（cm）：") or '0')
# BMI = weight/(leight/100)**2
# if BMI>24:
#     print("您的体重过重")
# elif BMI<18.5:
#     print("您的体重过轻")
# else:
#     print("您的体重正常")
