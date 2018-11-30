from os import stat


class ReadFile:
    """
        输入每个字文件的最大体积，以MB为单位
        自动切割文件
    """
    def __init__(self, each_size):
        self.each_size = each_size

    def cut(self):
        while True:
            try:
                name = input('请输入需要打开的文件名')
                f = open('%s' % name, 'rb')
                break
            except FileNotFoundError:
                print("文件名输入有误")
        part = 1
        print('正在分割文件')
        while True:
            size = stat(name).st_size
            n = int(round(size / part, 0))
            if n >= self.each_size * 1024 * 1024:
                part += 1
            else:
                return name, part, int(n), size
            f.close()
# movie.mkv