# instance_method.py


class Dog:
    """创建一个Dog类， 此类用于描述一种小动物的行为和属性"""
    def eat(self, food):
        """此方法用来描述小狗吃东西的行为"""
        print('id 为', id(self), '小狗正在吃', food)

    def sleep(self, hour):
        """此方法用来描述小狗睡觉的行为"""
        print('小狗睡了', hour, '小时')

    def play(self, thing):
        """此方法用来描述小狗睡觉的行为"""
        print('小狗正玩', thing)


dog1 = Dog()        # 创建一个小狗对象
dog1.eat('骨头')
dog1.sleep(10)
dog1.play('shit')


dog2 = Dog()        # 创建另外一个小狗对象
dog2.eat('狗粮')
dog2.sleep(8)
dog2.play('蛋')
