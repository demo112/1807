
class Bicycle:
    def run(self, km):
        print('用脚登骑行了%skm' % km)


class EBicycle(Bicycle):
    def __init__(self, vol):
        self.vol = vol
        print('新买的电动车里有', vol, '度电')

    def __volume__(self, vol):
        print('还剩下%s度电。' % int(vol))
        self.vol = vol

    # def run(self, km):
    #     if self.vol >= km / 10:
    #         self.vol -= km / 10
    #         print("电动骑行了%skm,还剩%s度电" % (km, self.vol))
    #
    #     else:
    #         km_e = km - self.vol * 10
    #         km = self.vol * 10
    #         self.vol = 0
    #         print("电动骑行了%skm,还剩%s度电" % (km, self.vol), end=', ')
    #         super().run(km_e)

    # WAY2
    def run(self, km):
        e_km = min(km, self.vol * 10)
        if e_km > 0:
            self.vol -= e_km / 10
            print("电动骑行了%dkm, 还剩%f度电" % (e_km, self.vol))
        if km > e_km:
            super().run(km - e_km)

    def fill_charge(self, vol):
        """充电"""
        self.vol = vol
        print("充电%s度" % vol)


b = EBicycle(5)  # 新买的电动车内有5度电
b.run(10)  # 电动骑行了10km还剩4度电
b.run(100)  # 电动骑行了40km还剩0度电, 用脚登骑行了60km
b.fill_charge(10)  # 充电10度
b.run(50)  # 电动骑行了50km还剩5度电
