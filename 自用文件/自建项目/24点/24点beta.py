import time
from typing import List


list = List[int]


class Twentyfour():
    def __init__(self, no:list=None):
        self.opt = ["+", "-", "*", "/"]
        if not no:
            self.num = self.get_number()
        else:
            self.num = no

    def get_number(self):
        cards = []
        for i in range(1,5):
            card = int(input("Please input 4 number as 24Game %s card" % i))
            if True:
                """判断输入合法性"""
                cards.append(card)
        # print(cards)
        return cards

    def operator(self):
        # i = 0
        l = []
        for n in range(4):
            a = self.opt[n]
            for m in range(4):
                if m != n:
                    b = self.opt[m]
                else:
                    continue
                for p in range(4):
                    if self.opt[p] != a and self.opt[p] != b:
                        c = self.opt[p]

                        l.append([a, b, c])
                        # i += 1
                        # print(a, b, c, i)
        return l

    def numbers(self):
        """将数字排序"""
        l = []
        for n in range(4):
            a = self.num[n]
            for m in range(4):
                if m != n:
                    b = self.num[m]
                else:
                    continue
                for p in range(4):
                    if self.num[p] != a and self.num[p] != b:
                        c = self.num[p]
                        d = sum(self.num) - a - b - c
                        l.append([a, b, c, d])
                        # print(a, b, c, d, i)
        return l

    def do_make(self) -> list:
        """增强用多线程"""
        opy_list = self.operator()
        num_list = self.numbers()
        # print(opy_list, num_list)
        """
            这个不行
            用每次生成的计算符完全匹配每次生成的数字排列
        """
        for i in num_list:
            for j in opy_list:
                print(i, j)
                while True:
                    l = []
                    for n in range(4):
                        l.append(i[n])
                        if n < 3:
                            l.append(j[n])
                    break
                print(l)
                jieguo = self.jisuan(l)
                if jieguo:
                    print(jieguo)
                else:
                    continue
                return jieguo
                # print("\b")
            
    def jisuan(self, l: list) -> list:
        """
            这个不行
            计算每个组合的结果
        """
        l_jisuan = l
        # 乘除计算
        for i in range(3):
            # print(l)
            if "*" in l:
                x = l.index("*")
                front = l[x + 1]
                after = l[x - 1]
                a = front * after
                l.pop(x - 1)
                l.pop(x - 1)
                l[x - 1] = a
            elif "/" in l:
                x = l.index("/")
                front = l[x + 1]
                after = l[x - 1]
                a = front / after
                l.pop(x - 1)
                l.pop(x - 1)
                l[x - 1] = a
        # 加减计算
        for i in range(3):
            # print(l)
            if "+" in l:
                x = l.index("+")
                front = l[x + 1]
                after = l[x - 1]
                a = front + after
                l.pop(x - 1)
                l.pop(x - 1)
                l[x - 1] = a
            elif "-" in l:
                x = l.index("-")
                front = l[x + 1]
                after = l[x - 1]
                a = front - after
                l.pop(x - 1)
                l.pop(x - 1)
                l[x - 1] = a
        print(l,l_jisuan)
        if l[0] == 24 and len(l) == 1:
            return l_jisuan
        else:
            return []






if __name__ == "__main__":
    twentyfour = Twentyfour([1, 2, 3, 4])
    print(twentyfour.do_make())
    # twentyfour.numbers()
    # twentyfour.operator()
