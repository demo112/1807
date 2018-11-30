def lines(lst):
    f = open('dictionary.txt', 'wt')
    for x in lst:
        f.write(x)
        f.write('\n')
