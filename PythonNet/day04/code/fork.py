import os


print("**************")
pid = os.fork()

if pid < 0:
    print('创建进程失败')
elif pid == 0:
    print('这是新的进程')
else:
    print("这是原有进程")

print('演示完毕')
