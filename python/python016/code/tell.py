f = open('20.txt', 'rb')
pos = f.tell()
print(pos)

b = f.read(3)
pos = f.tell()
print(b, pos)

b2 = f.read(1)
pos = f.tell()
print(b2, pos)
