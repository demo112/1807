def op():
    choose = input('请输入您需要复制的文件名')
    try:
        f = open('%s' % choose, 'rb')
        fc = open('%s_copy.txt' % choose, 'ab')
        while True:
            lst = f.readline()
            if lst == b'':
                break
            print('1111')
            fc.write(lst)
        f.close()
        fc.close()
    except OSError:
        print('copy finish')

op()

# numbers.txt
