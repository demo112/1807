# globals_locals.py


a = 100#全局变量
b = 200#全局变量


def fn(c):#局部变量
    d = 300#局部变量
    a = 1000000
    print(a, b, c, d)
fn(300)
print(a, b)


#示例
L = []
def input_number():
    L2 = []
    while True:
        n = int(input('请输入正整数'))
        if n < 0:
            break
        L2.append(n)
    # L = L2
    L.append(L2)        #改变变量绑定的对象
input_number()
print()