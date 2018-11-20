import _thread
from time import sleep,ctime

def loop0():
    print("loop0 开始于：{0}".format(ctime()))
    sleep(4)
    print('loop0 结束于：{0}'.format(ctime()))

def loop1():
    print("loop1 开始于：{0}".format(ctime()))
    sleep(2)
    print('loop1 结束于：{0}'.format(ctime()))

def main():
    print('线程开始于：{0}'.format(ctime()))
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print('Over :{0}'.format(ctime()))

if __name__ == '__main__':
    main()