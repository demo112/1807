#!/user/bin/env python3.py
# -*- coding:utf-8 -*-


# Author:cooper
# Date  :2018


import random
import math

__mataclass__ = type  

class map2048():
    def reset(self):
        self.__row = 4
        self.__col = 4
        self.data = [
            [0 for x in range(self.__col)]
            for y in range(self.__row)
        ]
        # self.data = [[x + 4 * y for x in range(self.__col)]
        # for y in range(self.__row)]
        # self.data = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
self.fill2()        