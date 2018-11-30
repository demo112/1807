try:
    try:
        n = int(input('请输入整数'))
    except ValueError:
        print('在内层try语句内出现错误，已转为正常状态')
    else:
        print('在内层语句没有出现异常')
except:
    print('在外层try语句内出现错误，已转为正常状态')
else:
    print('在外层try语句没有出现异常')


