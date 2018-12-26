import re

obj = re.fullmatch(r'\w+','abcdef123')
print(obj.group())

try:
    obj = re.fullmatch(r'\w+','abcdef123#')     # 返回None
    print(obj.group())      # 报错
except AttributeError as a:
    print('Error:', a)
