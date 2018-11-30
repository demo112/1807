# 此示例示意含有yield语句的生成器函数的调用顺序
# 生成器函数只有在next（it）函数调用时才会执行，
# 且遇到yielld后返回相应的值给next（it）函数


def myyield():                 # 生成器函数
    print("即将生成2")          #
    yield 2                    # 包含yield
    print("即将生成3")          # 用生成器语句来生成生成器函数
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print('生成器生成结束')

#
# for x in myyield():          # 调用生成器函数来生成2， 3， 5， 7
#     print(x)


# gen = myyield()                # 用生成器拿到迭代器
# it = iter(gen)                 # 获取迭代器
# 此时生成器函数开始执行，并遇到yeild停止
it = iter(myyield())
print(it)
print(next(it))                # 访问迭代器     2
print(next(it))                # 访问迭代器     3
print(next(it))                # 访问迭代器     5
print(next(it))                # 访问迭代器     7
# print(next(it))                # 访问迭代器     '生成器生成结束'
