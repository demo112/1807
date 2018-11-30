

def drop(t):
    s = 0
    n = 100
    for _ in range(1, t + 1):
        s = s + n + n / 2
        n =n / 2
    return s, n
print(drop(10))

# lst = ['a', 'b', 'c']
# s = '*'.join(lst)
# print(s)