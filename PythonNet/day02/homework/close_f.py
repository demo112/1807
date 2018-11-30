# def funX():
#    x=5
#    def funY():
#        nonlocal x
#        x += 1
#        return x
#    return funY
# a = funX()
# print(a())
# print(a())
# print(a())
#
#
# def fun_A(x, y=3):
#     return x * y


for a in map(lambda x, y = 3: x * y, [1]):
    print(a)
print(list(x for x in range(3, 101, 3)))
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
