import re


str = '''
hello world
hello kitty
你好，北京'''
pattern = r'Hello'
pattern_dot = r'.+'
pattern_multiline = r'.+'
pattern_verbose = r'''
                        h\w+        # 匹配第一个单词
                        \s+         # 匹配多个空格
                        [a-z]+      # 匹配其他
                    '''

regex = re.compile(pattern, flags=re.IGNORECASE)                        # re.I
regex_dot = re.compile(pattern_dot, flags=re.DOTALL)                    # re.S
regex_multiline = re.compile(pattern_multiline, flags=re.MULTILINE)     # re.M
regex_verbose = re.compile(pattern_verbose, flags=re.VERBOSE)           # re.X
regex_many = re.compile(pattern_verbose, flags=re.VERBOSE | re.I)       # re.X

try:
    s = regex.search(str).group()
    s_dot = regex_dot.search(str).group()
    s_multiline = regex_multiline.search(str).group()
    s_verbose = regex_verbose.search(str).group()
except SyntaxError:
    print('没有匹配到内容')

print(s)
print(s_dot)
print(s_multiline)
print(s_verbose)
