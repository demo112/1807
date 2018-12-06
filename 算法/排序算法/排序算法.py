# 冒泡排序

def bubble(values):
    for i in range(len(values) - 1):
        # 标志至于for循环内部，只针对乱序数字进行冒泡
        flag = True
        for j in range(len(values) - 1 - i):
            if values[j] < values[j + 1]:
                pass
            else:
                values[j], values[j + 1] = values[j + 1], values[j]
                flag = False
        # 如果全部是顺序则直接跳出
        print(i)
        if flag:
            break

if __name__ == '__main__':
    values = [23, 45, 2, 67, 34, 9, 86, 39, 52, 73, 19, 98, 27]
    # values = [2, 9, 19, 23, 27, 34, 39, 45, 52, 67, 73, 86, 98]
    # values = [2, 9, 19, 23, 27, 34, 39, 45, 52, 100, 103, 67, 73, 86, 98]
    bubble(values)
    print('原始数据:%s' % values)
