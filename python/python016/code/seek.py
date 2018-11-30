f = open('20.txt', 'rb')
pos = f.tell()
print(pos)

b = f.read(3)
pos = f.tell()
print(b, pos)

b2 = f.read(1)
pos = f.tell()
print(b2, pos)

# seek方法
# f.seek(5, 0)        #等效
# f.seek(1, 1)        #等效
# f.seek(-15, 2)       #等效
b2 = f.read(5)
pos = f.tell()
print(b2, pos)
