
from turtle import *
import random

def gogo():
    colormode(255)
    width(2)
    for i in range(255):
        r=int(random.uniform(0,255))
        g=int(random.uniform(0,255))
        b=int(random.uniform(0,255))
        fd(100)
        if(i%2==0):
            pencolor(r,g,b)
            rt(155)
        else:
            pencolor(r,g,b)
            lt(100)
    done()

gogo()