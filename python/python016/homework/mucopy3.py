def mycopy(src_filename, dst_filename):
    try:
        fr = open(src_filename, 'rb')
        try:
            try:
                fw = open(dst_filename, 'wb')
                try:
                    while True:
                        b = fr.read(4096)
                        if not b:
                            break
                        fw.write(b)
                finally:
                    fw.close()
            except OSError:
                print('打开目标文件失败')
        finally:
            fr.close()
    except OSError:
        print('打开源文件失败')


src = input('请输入源文件名')
dst = input('请输入目标文件名')

mycopy(src, dst)

