# import1.py

import math  # 导入数学模块

print(math.factorial(5))
print(math.factorial(4))

print(math.cos(0))  # 1

# ---------------------------------------------

import sys, time # 导入数学模块

dir(time)


# -----------------------------------------------

import math as m # 导入数学模块
print(m.factorial(5))
print(m.factorial(4))
print(m.cos(0))
# -----------------------------------------------
# from time_sleep import *
from .time_sleep import run
# import .time_sleep.run
# import time_sleep
# print(dir(time_sleep))
# print(help(time_sleep))
run()
