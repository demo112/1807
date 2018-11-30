import re
f = open('test.txt')
pattern = r'[A-Z]\w+'
pattern1 = r'-?\d+\.?/?%?\d*'

l = []
for line in f:
    l += re.findall(pattern, line)

l1 = []
for line in f:
    l1 += re.findall(pattern1, line)

# print(l)
print(l1)
f.close()
