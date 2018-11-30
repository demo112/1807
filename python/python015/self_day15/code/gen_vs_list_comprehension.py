L = [2, 3, 5, 7]
L2 = [x ** 2 for x in L]
it = iter(L2)
print(next(it))
L[1] = 30
print(next(it))
# 4
# 9
# 列表推导式是一次性生成静态数据

L = [2, 3, 5, 7]
gen = (x ** 2 for x in L)
it = iter(gen)
print(next(it))
L[1] = 30
print(next(it))
# 4
# 900
# 生成器表达式是边用便生成