class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skill = None
        self.money = 0

    def teach(self, teacher, sth):
        self.skill = sth
        print(teacher.name, "教", self.name, sth)

    def works(self, money):
        self.money += money
        print(self.name, '上班赚了', money, '元钱')

    def borrow(self, rich, charge):
        if self.money >= charge:
            self.money += charge
            rich.money -= charge
            print(self.name, '向', rich.name, '借了', charge, '元钱')
        else:
            print(self.name, '向', rich.name, '借钱', rich.name, "说没钱，滚！")

    def show_info(self):
        print(self.__dict__)
