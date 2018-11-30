s = {'唐僧', '悟空', '八戒', '沙僧'}
for x in s:
    print(x)
else:
    print('遍历结束')

# change the code behind it to below!

# WAY1
s = {'唐僧', '悟空', '八戒', '沙僧'}
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        print("遍历结束")
        break


# WAY2
s = {'唐僧', '悟空', '八戒', '沙僧'}
it = iter(s)
try:
    while True:
        print(next(it))
except StopIteration:
    print("遍历结束")