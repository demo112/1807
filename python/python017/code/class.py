# class.py
class Dog:
    '''创建一个Dog类， 此类用于描述一种小动物的行为和属性'''
    pass


dog1 = Dog()            # 创建Dog类的第一个实例
print(id(dog1))
# 4364993368

dog2 = Dog()            # 创建Dog类的第二个实例
print(id(dog2))
# 4364993480

# ID不同

print('----------------------------------------')

lst1 = list()
print(id(lst1))

lst2 = list()
print(id(lst2))
