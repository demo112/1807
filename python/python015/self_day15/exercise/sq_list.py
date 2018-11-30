L = [2, 3, 5, 7]
gen = iter(L)
L2 = [x ** 2 for x in gen]
print(L2)


#
# 思考:
#    L = [2, 3, 5, 7]
#    L2 = [x ** 2 for x in L]  # 列表推导式
#    it = iter(L2)
#    print(next(it))  # 4
#    L[1] = 10
#    print(next(it))  # 9
#
#    L = [2, 3, 5, 7]
#    G3 = (x ** 2 for x in L)  # 生成器表达式
#    it = iter(G3)
#    print(next(it))  # 4
#    L[1] = 10
#    print(next(it))  # 100