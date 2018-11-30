def InFile(lst):
    f = open('student_name.txt', 'xt')
    f.writelines('%s' % lst)
    f.close()

InFile(['ds', 'as', 'fs', 'as'])
