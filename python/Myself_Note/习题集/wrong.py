def dec(f):
    n = 3

    def wrapper(x):
        print('2')
        return f(x) * n
    print('3')
    return wrapper


@dec
def foo(m):
    print('1')
    return m * 2


print(foo(2))
