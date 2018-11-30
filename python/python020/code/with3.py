class A:
    """此类对象可以用于with语句进行管理"""
    def __enter__(self):
        print('1此方法已进入是在with语句内执行的')
        return self         # self将被with中的as变量绑定

    def __exit__(self, exc_type, exc_val, exc_tb):
        """exc_type：用来绑定错误类型，当没有错误发生时，绑定None
           exc_val：用来绑定错误对象，当没有发生异常时绑定None
            exc_tb：用来绑定Traceback对象，，如果没有绑定None"""
        if exc_type is None:
            print('3您已离开with语句，你离开时没有发生任何异常')
        else:
            print('3您已离开with语句')
            print('错误类型是exc_type', exc_type)
            print('错误对象是exc_val', exc_val)
            print('Traceback对象是exc_tb', exc_tb)


with A() as a:
    print('2这个with语句内部的输出')
    int(input('请输入整数'))


print("4程序正常结束")
