A = [1, 2, [3, 4, ['434']]]
print(len(A))

def show(lst):
    for x in lst:
        if type(x) is not list:
            print(x, end=' ')
        else:
            show(x)


show(A)
