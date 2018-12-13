class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while True:
        if unit_1.health <= 0 and unit_2.health > 0:
            unit_1.is_alive = False
            return False

        unit_2.health -= unit_1.attack
        if unit_1.health > 0 >= unit_2.health:
            unit_2.is_alive = False
            return True
        elif unit_1.health > 0 and unit_2.health > 0:
            unit_1.health -= unit_2.attack
        else:
            unit_1.is_alive = False
            return False
        # unit_1.health -= unit_2.attack


class Army(object):
    def __init__(self):
        self.army = []

    def add_units(self, bg, Sergeant):
        # print(kind,Sergeant)
        for i in range(Sergeant):
            self.army.append(bg())


class Battle(object):
    def fight(self, unit_1, unit_2):
        unit_1 = unit_1.army
        unit_2 = unit_2.army
        while True:
            print(len(unit_1))
            print(len(unit_2))
            if unit_1 == []:
                return False
            elif unit_2 == []:
                return True
            s1 = unit_1[0]
            s2 = unit_2[0]
            print('1',unit_1.index(s1), s1.health, s1.attack)
            print('2', unit_2.index(s2), s2.health, s2.attack)

            resort = fight(s1, s2)
            print(resort)

            if resort:
                print('1', unit_1.index(s1), s1.health, s1.attack)
                print('2', unit_2.index(s2), s2.health, s2.attack)
                unit_2.remove(s2)
            else:
                unit_1.remove(s1)
                print('2', 2)

        # print(unit_1, unit_2)
        # for i in unit_1:
        #     for n in unit_2:
        #         resort = fight(i, n)
        #         if resort == True:
        #             unit_2.remove(n)
        #         else:
        #             unit_1.remove(n)
        #         if unit_2 is []:
        #             return True
        #         else:
        #             return False





if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()
    #
    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
