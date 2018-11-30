y = 370105199208263718


def isprime(x):
    if x < 2:
        return False
    else:
        for y in range(2, x):
            if x % y == 0:
                return False
        return True


def prime(y):
    y = y
    lst = []
    for x in range(1, y):
        if x < 2:
            pass
        else:  # n大于等于2
            for i in range(2, x):
                if x % i == 0:  # 如果整除
                    break
            else:
                lst += [x]
    print("素数列表完成")
    return lst


def bn(y):
    while not isprime(y):
        # for x in prime(y):
        for x in range(2,y):
            if y % x == 0:
                y = int(y / x)
                yield x
                break
    else:
        yield y


st = [x for x in bn(y)]
print(st)
