# Mysql_order 输入一个季度 1~4 输出这个季度有哪几个月
# ,如果用户输入的不是1~4的整数,则提示用户您输错了

s = int(input("请输入季度(1~4): "))

if s == 1:
    print("春季有1,2,3月")
elif s == 2:
    print("夏季有4,5,6月")
elif s == 3:
    print("秋季有7,8,9月")
elif s == 4:
    print("冬季有10,11,12月")
else:
    print("您输错了")





