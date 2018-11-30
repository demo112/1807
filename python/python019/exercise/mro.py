class Peasant:
    def farm(self, plant):
        print('正在种植', plant)


class Worker:
        def work(self, that):
            print('正在制造', that)


class MigrantWorker(Peasant, Worker):
    pass


person = MigrantWorker()
person.farm('水稻')
person.work('汽车')

for x in MigrantWorker.__mro__:
    print(x)
print()

for x in Peasant.__mro__:
    print(x)
print()
for x in Worker.__mro__:
    print(x)
print()
