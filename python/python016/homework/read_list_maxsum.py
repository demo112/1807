

def read_list():
    f = open('numbers.txt', 'rt')
    lst = f.readline()
    lst.rstrip()
    lst = lst.split(' ')
    ls =[]
    for x in lst:
        ls.append(int(x))
    f.close()
    return ls
print(read_list())
print(sum(read_list()))
print(max(read_list()))
