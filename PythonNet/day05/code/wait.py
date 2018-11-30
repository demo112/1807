import os
from time import sleep

pid = os.fork()

if pid < 0:
    pass
elif pid == 0:
    sleep(3)
    print('Child process exit', os.getpid())
    os._exit(2)
else:
    pid, status = os.wait()
    print(pid, status)                  # 或取退出时子进程的PID 和 256*退出状态
    print(os.WEXITSTATUS(status))       # 获取子进程的退出状态
    while True:
        pass
