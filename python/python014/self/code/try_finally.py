

# def fry_egg():
#     print('打开天然气')
#     count = int(input("请输入鸡蛋个数："))
#     print('完成煎鸡蛋，共煎了%d个鸡蛋' % count)
#     print("关闭天然气")
#
#
# try:
#     fry_egg()
# finally:
#     print("关闭天然气")



def fry_egg():
    print('打开天然气')
    count = int(input("请输入鸡蛋个数："))
    print('完成煎鸡蛋，共煎了%d个鸡蛋' % count)
    print("关闭天然气")


try:
    fry_egg()
except:
    print('程序出现过异常，已转为正常状态')
finally:
    print("关闭天然气")
