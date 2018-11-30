def isprime(b, n):
    # print(b, n)
    lst = []
    while n > 0:
        print(b, n, lst)
        if b < 2:
            b += 1
        else:  # n大于等于2
            for i in range(2, b):
                if b % i == 0:  # 如果整除
                    b += 1
            else:
                lst += [b]
                n -= 1
                # print(b, n, lst)
    else:
        return lst

print(isprime(10, 4))