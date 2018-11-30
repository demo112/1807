
# 输入某年某月某日，判断这一天是这一年的第几天？
import time


def whichday(y, m, d):
    t = time.localtime()
    t2 = (y, m, d) + t[3:9]
    t22 = (y, 1, 1) + t[3:9]
    t3 = time.mktime(t2)
    t32 = time.mktime(t22)
    day = (t3 - t32) / 60 / 60 // 24
    print(day)


whichday(1992, 1, 1)
