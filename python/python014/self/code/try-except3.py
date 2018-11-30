

def div_apple(n):
    print("%d个苹果您想分给几个人" % n)
    s = input('请输入人数')
    cnt = int(s)            # 可能触发ValueError错误而进入异常
    result = n / cnt        # 可能触发ZeroDivisionError错误而进入异常
    print("每个人分了", result, '个苹果')


# div_apple(10)
# print("分苹果完成")


try:
    div_apple(10)
    print("分苹果完成")
except ValueError:
    print('分苹果失败，不分了')
except:
    print("收到除ValueError以外的错误通知")
print('程序正常退出')
