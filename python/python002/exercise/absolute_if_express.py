# 2. 写一个程序,输入一个数,用条件表达式计
# 算这个数的绝对值,并打印出来

n = int(input("请输入一个数: "))

r = n if n > 0 else -n

print("绝对值是:", r)