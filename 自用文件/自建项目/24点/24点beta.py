from typing import List


def get_number():
    """获取卡牌"""
    cards = []
    for i in range(1, 5):
        card = int(input("Please input 4 number as 24Game %s card" % i))
        if True:
            """判断输入合法性"""
            cards.append(card)
    # print(cards)
    return cards


class Twentyfour(object):
    def __init__(self, no: list=None):
        self.opt = ["+", "-", "*", "/"]
        if not no:
            self.num = get_number()
        else:
            self.num = no

    def operator(self) -> List[List[str]]:
        """获取计算符排列种类"""
        # i = 0
        jisuanfu = []
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

                        jisuanfu.append([a, b, c])
                        # i += 1
                        # print(a, b, c, i)
        return jisuanfu

    def numbers(self):
        """将数字排序"""
        shuju = []
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
                        shuju.append([a, b, c, d])
                        # print(a, b, c, d, i)
        return shuju


if __name__ == "__main__":
    twentyfour = Twentyfour([1, 2, 3, 4])
