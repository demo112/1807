# Mysql_order 打印 1 ~ 20 的整数,打印在一行内
#   1 2 3 4 5 6 .... 18 19 20
#   print(i, end=' ')

i = 1
while i <= 20:
    print(i, end=' ')
    i += 1
else:
    print()  # 换行
    # print(end='\n')  # 换行