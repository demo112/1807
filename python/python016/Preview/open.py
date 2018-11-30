try:
    file = open("while.py")
    file.close()
except OSError:
    print("打开文件失败")


try:
    file = open("/etc/passwd")
    print('文件已经打开')
    s = file.reading()
    print(s, end='')
    file.close()
except IOError:
    print('打开文件失败！')