import re


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    letter = re.split(r'\B', line)
    l = len(letter)
    L = []
    for x in range(l):
        n = 0
        a = letter[x]
        for y in range(x, l):
            b = letter[y]
            # print(a, b)
            if a == b == '':
                return 0
            elif a == b :
                n += 1
            else:
                break
        L.append(n)
    return max(L)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

from itertools import groupby

def long_repeat(line):
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')