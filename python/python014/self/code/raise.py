

def make_except():
    print('开始')
    # raise ValueError

    # e = ValueError('这是一个故意制作的错误')
    # raise e

    e = ZeroDivisionError
    print('结束')


try:
    make_except()
except ValueError as err:
    print('make_except发出了ValueError类型的错误，已捕获', err)

print('程序结束')
