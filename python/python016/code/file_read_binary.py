try:
    fr = open('mynote.txt', 'rb')
    b = fr.read()
    c = b.decode()
    print(b)
    print(c)
    fr.close()     # 返回的是字节串

except OSError:
    print("打开二进制文件失败")
