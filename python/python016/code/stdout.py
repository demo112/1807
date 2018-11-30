import sys
sys.stdout.write('我是一个标准输出\n')
sys.stderr.write('我的出现是一个错误\n')
print('hello', ' world', file=sys.stdout)
f = open('wenjian.txt', 'w')
print('hello', ' world', file=f)
f.close()