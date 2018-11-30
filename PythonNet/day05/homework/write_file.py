from time import sleep


class Write:
    def __init__(self, name, part, n, size):
        self.n = n
        self.name = name
        self.part = part
        self.size = size

    def write_file(self):
        lst = self.name.split('.')
        new_name = lst[0] + str(self.part) + '.' + lst[1]
        f = open('%s' % self.name, 'rb')
        fn = open('%s' % new_name, 'wb')

        start = (self.part - 1) * self.n
        stop = self.part * self.n - 1

        f.seek(start)
        if stop <= self.size:
            lst = f.read(self.n)
            fn.write(lst)
        else:
            n = self.n - start
            lst = f.read(n)
            fn.write(lst)
            print('复制完成')
        f.close()
        fn.close()
