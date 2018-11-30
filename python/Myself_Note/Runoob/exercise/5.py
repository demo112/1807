# 输入三个整数x,y,z，请把这三个数由小到大输出。
def reverse():
    n = int(input('请输入需要对几个数排序'))
    if n == 0:
        raise ZeroDivisionError
    lst = []
    for x in range(n):
        x = int(input("请输入数字"))
        lst += [x]
    lst.sort()
    for x in lst:
        print(x, end=' ')
    print()


def run():
    try:
        reverse()
    except ZeroDivisionError:
        print('finish')
    except:
        print('您输入的内容有误请重新输入')
        run()

   
run()
