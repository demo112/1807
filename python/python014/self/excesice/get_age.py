def get_age():
    n = int(input("请输入年龄"))
    if 1 > n:
        raise ValueError("年龄太小...")
    elif n > 100:
        raise ValueError("年龄超出了正常值")
    return n


try:
    age = get_age()
    print("用户输入的年龄是:", age)
except ValueError as err:
    print('用户输入的不是1~140的整数,获取年龄失败')
    print("原因是:", err)
