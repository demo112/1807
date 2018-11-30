import re

pattern = r"(\w+):(\d+)"
s = "zhang:1994 li:1993"
# # re直接调用
# l = re.findall(pattern, s)
# print(l)
# # [('zhang', '1994'), ('li', '1993')]

# compile对象调用
regex = re.compile(pattern)
l = regex.findall(s)
print(l)

