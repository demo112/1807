try:
    # f = open('newfile.txt', 'w')
    # f = open('newfile.txt', 'x')        # 如果原文件存在则报错
    f = open('newfile.txt', 'a')        # 如果原文件存在则报错
    print("打开成功")
    f.write('hello')
    f.write('world')
    f.writelines(['123', 'abc', 'ABC'])
    f.close()
    print('写入成功')
except OSError:
    print("创建文件失败")
