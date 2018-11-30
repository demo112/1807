

class Human:
    def set_info(self, name, age, score=0):
        """此方法用来给人对象添加'姓名', '年龄', '家庭住址'三个属性"""
        self.name = name
        self.age = age
        self.score = score

    def show_info(self):
        """显示此人的全部信息"""
        print('这个人的name是：', self.name)
        print('这个人的age是：', self.age)
        print('这个人的score是：', self.score)


human1 = Human()
human2 = Human()

human1.set_info('xiaozhang', 25, 89)
human2.set_info('xiaoli', 22, 97)


human1.show_info()
human2.show_info()
