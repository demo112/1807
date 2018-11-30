import re

pattern = r'(ab)cd(ef)'
s = 'abcdefghijklmnabcdef'

# re模块直接调用
l = re.findall(pattern, s)
print(l)

# compile对象调用
regex = re.compile(pattern)
l = regex.findall(s, 0, 17)     # 从0开始16结束
print(l)

l = re.split(r'\s+', 'hello world nihao China')
print('split:', l)

s = re.sub(r'\s+','#!#', 'hello world nihao China', 2)
print('sub:', s)

s1 = re.subn(r'\s+','#!#', 'hello world nihao China')
print('sub:', s1)
