# 题目：输出 9*9 乘法口诀表。
import time
for x in range(1, 10):
    for y in range(1, x + 1):
        s = y * x
        print(s, '=', y, '*', x, sep='', end=' ')
    print()
    time.sleep(1)
# 暂停一秒输出