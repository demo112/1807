from multiprocessing import Process
from PythonNet.day05.homework.read_file import ReadFile
from PythonNet.day05.homework.write_file import Write


process = []
f = ReadFile(8)
name, part, n, size = f.cut()
# print(part, n)

for i in range(1, part + 1):
    new = Write(name, i, n, size)
    p = Process(target=new.write_file())
    print(name, i, n)
    p.start()
    process.append(p)

for i in process:
    i.join()
