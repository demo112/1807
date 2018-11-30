import time



def ip():
    y = 2018    # input('year')
    m = 7       # input('month')
    d = 23      # input('day')
    n = time.localtime()
    lst = list(n)
    lst[0:3] = y, m, d
    return lst
    # 自然日
def nuture_day():
    s = time.time() - time.mktime(tuple(ip()))
    print(s)
    d = s / 60 / 60 // 24
    return d
    # 工作日
def work_days():
    a = tuple(ip())
    b = tuple(time.localtime())
    d = 0
    print(a, b)
    while True:
        if time.mktime(a) < time.mktime(b):
            if a[5] ==  5 or a[5] ==  6:
                d = d
            else:
                d += 1
                a = time.localtime(a + 24 * 60 * 60 * d)
                # print(time.localtime(time.mktime(tuple(ip()))))
        else:
            break
    return d

work_days()


# def days():
#     t = time.time()
#     print(t)
#     d = time.localtime(t)
#     print(d)
#     l = 0
#
# days()
