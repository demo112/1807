# Mysql_order 指定一个半径为r = 3 厘米的圆
#   1) 计算圆的周长是多少厘米
#   2) 计算圆的面积是多少平方厘米

r = 3  # cm 半径
pi = 3.1415  # 圆周率

# 计算周长　
length = pi * r * 2  # 周长
print("周长是:", length)

# 计算面积
area = pi * r ** 2  # 面积
print("面积是:", area)

