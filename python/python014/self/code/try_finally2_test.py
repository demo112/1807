x = 100
y = 200
try:
    save_x = x
    save_y = y
    try:
        x = int(input("请输入x"))
        y = int(input("请输入y"))
        print("x=%d, y=%d" % (x, y))
    finally:
        x = save_x
        y = save_y
except:
    pass
