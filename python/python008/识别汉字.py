def hanzishibie(a):
    a = input('输入')
    L = len([x for x in a if ord(x) > 127])
    print(L)
