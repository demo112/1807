# 练习：
#   写一个程序，从键盘输入一段字符串存入s变量
#     Mysql_order 将此字符串转为字节串用变量b绑定,并打印出b
#     2. 打印字符串s的长度和字节串b的长度
#     3. 将b字节串再转换为字符串用变量s2 绑定，
#        判断 s2 和 s是否相同?

s = input('请输入: ')

# Mysql_order 将此字符串转为字节串用变量b绑定,并打印出b
b = s.encode('utf-8')
print(b)

# 2. 打印字符串s的长度和字节串b的长度
print("字符串s的长度是:", len(s))
print("字节串b的长度是:", len(b))

# 3. 将b字节串再转换为字符串用变量s2 绑定，
s2 = b.decode('utf-8')
print('s == s2 :', s == s2)



