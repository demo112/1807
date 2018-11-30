def num():
    f = open('numbers.txt', 'wt')
    lst = []
    while True:
        n = int(input("请您输入整数"))
        if n >= 0:
            lst.append(str(n))
        else:
            print('停止输入')
            break
    lst = ' '.join(lst)
    f.writelines(lst)
    print('内容已保存至numbers.txt')
    f.close()
    return lst

try:
    num()
except ValueError:
    print('您的输入被迫结束,没有保存')

# 方法二请参考teach day17/excesice