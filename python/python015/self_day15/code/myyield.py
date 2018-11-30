

def myyield():                 # 生成器函数
    yield 2                    # 包含yield
    yield 3
    yield 5
    yield 7
    print('生成器生成结束')

#
# for x in myyield():          # 调用生成器函数来生成2， 3， 5， 7
#     print(x)


gen = myyield()                # 用生成器拿到迭代器
it = iter(gen)
print(next(it))                # 访问迭代器     2
print(next(it))                # 访问迭代器     3
print(next(it))                # 访问迭代器     5
print(next(it))                # 访问迭代器     7
print(next(it))                # 访问迭代器     '生成器生成结束'
