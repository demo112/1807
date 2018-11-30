class Human:
    total_count = 0     # 类变量，用来记录Human对象的个数
    pass


print(Human.total_count)        # 类变量可以通过该类直接访问
Human.total_count += 1          # 类变量可以通过该类修改

h1 = Human()
print(h1.total_count)           # 借助此类的实例来查看此类的类变量  /  类变量可以通过类的实例直接访问

print(dir(Human))
print(dir())

h1.total_count = 1000
print(h1.total_count)
print(Human.total_count)


print(h1.__class__)
h1.__class__.total_count += 1  # 类变量可以通过此类的对象的__class__属性间接访问
print(Human.total_count)
