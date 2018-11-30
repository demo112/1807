import os
from time import sleep


def wait_pid():
    pid = os.fork()

    if pid < 0:
        pass
    elif pid == 0:
        sleep(3)
        print('Child process exit', os.getpid())
        os._exit(2)
    else:
        while True:
            sleep(0.1)
            # 通过非阻塞的形式捕获子进程的退出
            pid, status = os.waitpid(-1, os.WNOHANG)
            print(pid, status)                  # 或取退出时子进程的PID 和 256*退出状态
            print(os.WEXITSTATUS(status))       # 获取子进程的退出状态
            if status != 0:
                break
        while True:
            pass


if __name__ == '__main__':
    try:
        wait_pid()
    except KeyboardInterrupt:
        print('被强制退出')
