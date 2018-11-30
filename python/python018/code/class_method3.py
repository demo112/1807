
#
# class A:
#     v = 0       # 类变量（类属性）
#
#     @classmethod
#     def set_v(cls, a):
#         """请问此方法不能访问a.color属性"""
#         cls.v = a
#         print(cls.color)
#
# a = A()
# a.color = '#FF0000'
# a.set_v(100)
