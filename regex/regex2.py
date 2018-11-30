import re

pattern = r'(?P<dog>ab)cd(?P<pig>ef)'
regex = re.compile(pattern)

match_obj = regex.search('abcdefghij', 0, 8)

# 属性
print(match_obj)                # match对象
print(match_obj.pos)            # 匹配目标字符串的起始位置
print(match_obj.endpos)         # 匹配目标字符串的结束位置
print(match_obj.re)             # 正则表达式
print(match_obj.string)         # 目标字符串
print(match_obj.lastgroup)      # 最后一组的组名
print(match_obj.lastindex)      # 最后一组的编号
print('==================')
# 方法
print(match_obj.start())        # 匹配内容的开始位置
print(match_obj.end())          # 匹配内容的结束位置
print(match_obj.span())         # 匹配内容的起止位置
print(match_obj.group())        # 获取match对象内容
print(match_obj.group('dog', 'pig'))   # 获取match对象内容
print(match_obj.groupdict())    # 获取捕获组字典（组名：内容）
print(match_obj.groups())       # 获取每个子组匹配内容
