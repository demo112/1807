# 练习：
# 　　Mysql_order 写一个程序，任意输入一个数，判断这个数是否是
#     素数(prime)
#     素数（也叫质数),是只能被１和自身整除的正整数
#      如: 2 3 5 7 11 13 17 19 ....
#     提示:
#       用排除法: 当判断x是否为素数时，只要让x分别除以
#     2, 3, 4, 5 ... x-1，只要能整数则x不是素数,否
#     则x是素数

x = int(input('请输入一个整数: '))
if x < 2:
    print(x, '不是素数')
else:  # n大于等于2
    for i in range(2, x):
        if x % i == 0:  # 如果整除
            print(x, '不是素数')
            break
    else:
        print(x, '是素数')


