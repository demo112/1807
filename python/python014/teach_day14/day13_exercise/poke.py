# Mysql_order 模拟斗地主发牌，牌共 54张
#   黑桃('\u2660'), 梅花('\u2663'), 方块('\u2665'), 红桃('\u2666')
#   A2-10JQK
#   大王,小王
#   三个人，每个人发17张，底牌留三张
#   要求:
#     输入回车,打印第1个人的17张牌
#     输入回车,打印第2个人的17张牌
#     输入回车,打印第3个人的17张牌
#     输入回车,打印三张底牌


kinds = ['\u2660', '\u2663', '\u2665', '\u2666']
numbers = ['A'] + [str(x) for x in range(2, 11)] + list("JQK")
pokes = ['大王', '小王']
for k in kinds:
    for n in numbers:
        pokes.append(k + n)  # 生成一张牌并加入pokes列表中


L = pokes.copy()  # 从新牌复制一份
import random
random.shuffle(L)  # 洗牌
# print(L)

input()  # 等待键盘输入
print("第1个人的17张牌是:", L[:17])
#   输入回车,打印第2个人的17张牌
input()  # 等待键盘输入
print("第2个人的17张牌是:", L[17:34])
#   输入回车,打印第3个人的17张牌
input()  # 等待键盘输入
print("第3个人的17张牌是:", L[34:51])
#   输入回车,打印三张底牌
input()
print("底牌是:", L[51:])