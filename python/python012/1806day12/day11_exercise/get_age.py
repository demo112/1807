# Mysql_order　已知五位朋友在一起
#   第五位朋友比第四位朋友大2岁
#   第四位朋友比第三位朋友大2岁
#   第三位朋友比第二位朋友大2岁
#   第二位朋友比第一位朋友大2岁
#   第一位朋友说它10岁
#   写程序打印出第五位朋友　和第三位朋友　的年龄


def get_age(n):
    if n == 1:
        return 10
    return get_age(n - 1) + 2

print("第五位朋友%d岁" % get_age(5))
print("第三位朋友%d岁" % get_age(3))
