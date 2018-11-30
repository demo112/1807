def hang(a):
    lst = []
    for n in range(1, a + 1):
        lst += ['%02s *%02s =%03s' % (n, a, n * a)]
    return lst


def each(a):
    lst = hang(a)
    for m in lst:
        print(m, end='  ')
    print()


def main(n):
    for a in range(1, n + 1):
        each(a)


main(9)


# WAY2
for x in range(1, 10):
    for y in range(1, x + 1):
        print('%02s *%02s =%03s' % (x, y, x * y), end=' ')
    print()



