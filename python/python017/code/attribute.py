# attribute.py
# 此示例示意为对象添加实例变量（实例属性）及访问实例变量（实例属性


class Dog:
    def eat(self, food):
        """此方法用来描述小狗吃东西的行为"""
        print(self.color, '的', self.kinds, '小狗正在吃', food)
        self.last_food = food

    def show_last_food(self):
        print(self.color, '的', self.kinds, '上次吃的是', self.last_food)


dog1 = Dog()
dog1.kinds = '京巴'       # 添加实例属性
dog1.color = '白色'       # 添加实例属性
dog1.color = '黄色'       # 修改实例属性的绑定关系


dog2 = Dog()             # 另一个对象
dog2.kinds = '藏獒'       # 添加实例属性
dog2.color = '棕色'       # 添加实例属性


print(dog1.color, '的', dog1.kinds)
print(dog2.color, '的', dog2.kinds)


dog1.eat('骨头')
dog2.eat('狗粮')

dog1.show_last_food()
dog2.show_last_food()
