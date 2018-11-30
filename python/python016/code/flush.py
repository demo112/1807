
f = open('myflush.txt', 'w')
f.write('aaaa')
f.flush()       # 强制将缓冲区的内容写到磁盘下
s = input('请输入回车键继续')
f.close()
