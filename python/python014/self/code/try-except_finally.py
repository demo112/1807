

def div_apple(n):
    print("%d个苹果您想分给几个人" % n)
    s = input('请输入人数')
    cnt = int(s)            # 可能触发ValueError错误而进入异常
    result = n / cnt        # 可能触发ZeroDivisionError错误而进入异常
    print("每个人分了", result, '个苹果')


try:
    div_apple(10)
    print("分苹果完成")
except ValueError as err:
    print('错误值是', err)
else:
    print('else语句被执行')
finally:        # finally子句无论是正常流程还是已成流程都会被执行
    print("这条语句一定会被执行的")


print('程序正常退出')
