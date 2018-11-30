# * 创建父子进程分别表示司机和售票员
# * 当售票员捕捉到SIGINT信号时，给司机发送SIGUSER1信号
#   此时司机打印 "老司机开车了"
#   当售票员捕捉到SIGQUIT信号时，给司机发送SIGUSER2信号。此时司机打印 "车速有点快，系好安全带"
#   当司机捕捉到SIGTSTP信号时，给售票员发送SIGUSER1信号。此时售票员打印 "到站了请下车"
# # * 到站后 售票员先下车（子进程先退出）然后司机下车
import os
from signal import *
from time import sleep
from multiprocessing import Process


def saler_handler(sig, fram):
    if sig == SIGINT:
        os.kill(os.getppid(), SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(), SIGUSR2)
    elif sig == SIGUSR1:
        print("到站了请下车")
        os._exit(0)


def drive_handler(sig, fram):
    if sig == SIGUSR1:
        print("老司机开车了")
    elif sig == SIGUSR2:
        print("车速快")
    elif sig == SIGTSTP:
        os.kill(p.pid, SIGUSR1)


# 子进程代表售票员
def saler():
    signal(SIGINT, saler_handler)
    signal(SIGQUIT, saler_handler)
    signal(SIGUSR1, saler_handler)
    signal(SIGTSTP, SIG_IGN)
    while True:
        sleep(2)
        print("Python带你去远方")


p = Process(target=saler)
p.start()


# 父进程

signal(SIGINT, SIG_IGN)
signal(SIGQUIT, SIG_IGN)
signal(SIGUSR1, drive_handler)
signal(SIGUSR2, drive_handler)
signal(SIGQUIT, drive_handler)

p.join()
