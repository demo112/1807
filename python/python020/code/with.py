try:
    f = open('../../python019/day19.txt')
    try:
        for l in f:
            x = int('aaa')
            print(l)
    finally:
        f.close()
        print('文件已经关闭')
except OSError:
    print('文件打开失败')
