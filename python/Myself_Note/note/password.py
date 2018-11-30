from random import choice


def password(n):
    lst = [chr(x) for x in range(65, 91)]
    print(lst)
    ls = []
    for x in range(n):
        a = choice(lst)
        ls.append(a)
    # l = [str(x) for x in ls]
    l = ''.join(ls)
    return l

print(password(8))