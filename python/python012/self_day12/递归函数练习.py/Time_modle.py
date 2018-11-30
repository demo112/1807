from time import *
# time.altzone	夏令时时间与UTC时间差(秒为单位)
print(altzone)
# -28800

# 时区名字的元组， 第一个名字为未经夏令时修正的时区名,
# 第二个名字为经夏令时修正后的时区名
print(tzname)
# ('CST', 'CST')
sleep(1)
print(time())
print(mktime(gmtime()))
print(time() - mktime(gmtime()))
print(gmtime(1534423042.914826))
# time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16, tm_hour=12, tm_min=37, tm_sec=22, tm_wday=3, tm_yday=228, tm_isdst=0)
print(gmtime(10))
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=10, tm_wday=3, tm_yday=1, tm_isdst=0)
print(gmtime())
# time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16, tm_hour=12, tm_min=41, tm_sec=58, tm_wday=3, tm_yday=228, tm_isdst=0)
print(asctime())
print(mktime(gmtime(10)) - mktime(gmtime()))
