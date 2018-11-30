from time import sleep


def choose_file():
    f = open('base.txt', 'rt')
    return f


def break_word(f):
    words = []
    while True:
        lst = f.readline()      # this code is VERY important of judgment
        ls = lst.rstrip()
        ls = ls.split(' ')
        if lst is not '':
            for x in ls:
                words.append(x)
                # print(x)
                # print(type(x))
        else:
            return words


def check_list(lst):
    ls = []
    for x in lst:
        print(x)
        s = ''
        for y in range(len(x)):
            m = ord(x[y])
            if 65 <= m <= 122:
                # print(x[y])
                s += x[y]
            else:
                pass
        if s != '':
            ls.append(s)
        print(s)
        sleep(0.001)
        # yield s
    return ls


def sort(lst):
    lst.sort()
    ls = []
    print(lst)
    print(len(lst))
    for x in lst:
        if x not in ls:
            ls += [x]
    return ls


def lines(lst):
    f = open('dictionary.txt', 'wt')
    for x in lst:
        f.write(x)
        f.write('\n')
    f.close()


def main():
    words = break_word(choose_file())
    lst = sort(check_list(words))
    lines(lst)
main()

# lst = list(x for x in check_list(words))
# print(lst)
