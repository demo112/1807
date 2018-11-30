from time import sleep

#
# def myfn(n):
#     while n > 0:
#         print("hello world")
#         sleep(1)
#         n -= 1
#
# myfn(6)


def myfn(n):
    if n > 0:
        print("hello world")
        sleep(1)
        myfn(n - 1)

myfn(3)