import os
from time import sleep

pid = os.fork()
if pid < 0:
    print('创建进程失败')
elif pid == 0:
    sleep(0.1)
    print('这是新的进程')
    print('Child Get PID:', os.getpid())
    print('Child Get Parent PID:', os.getppid())
else:
    print("这是原有进程")
    print('Parent get PID:', os.getpid())
    print('Parent get Child PID:', pid)

print('演示完毕')
