
try:
    fbw = open('mynote.bin', 'wb')
    s = '你好'
    b = s.encode('utf-8')
    print(b)
    fbw.write(b)
    ba = bytearray(range(256))
    fbw.write(ba)
    fbw.close()
except OSError:
    print("打开二进制文件失败")
