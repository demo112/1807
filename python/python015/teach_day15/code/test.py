
L = [1, 2, 3, 4, 5]
def cc():
    for x in L:
        yield x
it = iter(L)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
