def mp(n):
    from time import sleep
    print('@' * n)
    sleep(0.11)
    if 10 < n < 1:
        return mp(n + 1)
    else:
        return mp(n - 1)
mp(5)