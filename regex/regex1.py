import re
"""
    共同属性都能生成match对象
"""


# finditer
it = re.finditer(r'\d+', '2008-2018 10年中国发生了变化')
for i in it:
    # print(dir(i))
    print(i.group())

# fullmatch（）
obj = re.fullmatch(r'\w+','abcdef123')
print(obj.group())
try:
    obj = re.fullmatch(r'\w+','abcdef123#')     # 返回None
    print(obj.group())      # 报错
except AttributeError as a:
    print('Error:', a)

# match
obj = re.match(r'foo', 'foo, food on the table')
print(obj.group())

# search
obj = re.search(r'foo', 'foo, food on the table')
print(obj.group())