from multiprocessing import Event

e = Event()
# 设置事件
e.set()

print(e.is_set())

e.wait(3)

# 清除设置
e.clear()
e.wait()
