# 有两个人(Human):
#     Mysql_order
#       姓名: 张三
#       年龄: 35
#     2.
#       姓名: 李四
#       年龄: 8
#     行为:
#       Mysql_order 教别人学东西 teach
#       2. 赚钱 works
#       3. 借钱 borrow
#     事情:
#       张三 教 李四 学 python
#       李四 教 张三 学 跳皮筋
#       张三 上班赚了 1000 元钱
#       李四 向 张三 借了 200 元钱
#       打印张三的信息: 35岁 的 张三 有钱 800元, 它学会跳皮筋
#       打印李四的信息: 8岁 的 李四 有钱 200元, 它学会python
from python017.code.zhang_li_class import Human

zhang3 = Human('张三', 35)
li4 = Human('李四', 8)

li4.teach(zhang3, 'python')
zhang3.teach(li4, '跳皮筋')

zhang3.works(1000)

li4.borrow(zhang3, 200)

print(zhang3.age, '岁的', zhang3.name, '有钱', zhang3.money, '元，他学会了', zhang3.skill, sep='', end='。\n')
print(li4.age, '岁的', li4.name, '有钱', li4.money, '元，他学会了', li4.skill, sep='', end='。\n')

zhang3.show_info()
li4.show_info()

print(Human.__dict__)

# __module__': 'python017.code.zhang_li_class
# __init__'  : <function Human.__init__ at 0x1032cb598>
# teach'     : <function Human.teach at 0x1032cb620>
# works'     : <function Human.works at 0x1032cb6a8>
# borrow'    : <function Human.borrow at 0x1032cb730>
# show_info' : <function Human.show_info at 0x1032cb7b8>
# __dict__'  : <attribute '__dict__' of 'Human' objects>
# __weakref__': <attribute '__weakref__' of 'Human' objects>
# __doc__'   : None