import random
kinds = ['\u2660', '\u2663', '\u2665', '\u2666']
shu = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# print(kinds)


def pai():
    pokes = []
    for x in shu:
        for y in kinds:
            pokes.append(y + x)
    pokes = pokes + ['KING', 'king']
    # print(pokes)
    return pokes


def sam(pokes):
    a = random.sample(pokes, 17)
    for x in a:
        pokes.remove(x)
    return a, pokes


def fa(pokes):
    n = input("按回车开始发牌")
    if n is '':
        a = sam(pokes)[0]
        print("这个人发牌：", a)
    return pokes


def main():
    pokes = pai()
    while True:
        if len(pokes) > 3:
            pokes = fa(pokes)
        else:
            print('抢地主！！！！')
            return print(pokes)


main()
