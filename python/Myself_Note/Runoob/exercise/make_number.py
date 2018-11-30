# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少
# WAY1

lst = [1, 3, 2, 4]
count = 0
for x in lst:
    for y in lst:
        for z in lst:
            if x != y and y != z and z!= x:
                n = x * 100 + y * 10 + z
                print(n)
                count += 1
print(count)
