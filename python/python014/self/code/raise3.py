# raise 嵌套反馈路径
def make_except():
    print('开始make_except')
    raise ValueError('我是一个错误')
    print('结束make_except')


def get_except():
    try:
        make_except()
    except ValueError as err:
        print('错误的值是', err)
        raise       # 重新触发刚收到的错误到上一层


try:
    get_except()
except ValueError as err:
    print('get_except内发生值的错误，已捕获', err)


print('程序结束')
