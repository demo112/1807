# 练习:
#   Mysql_order 求: 100以内有哪儿些数与自身+1的乘积再对 11
#      求余等于8?
#       x * (x+1)  % 11 == 8

for x in range(101):
    if x * (x + 1) % 11 == 8:
        print(x)
