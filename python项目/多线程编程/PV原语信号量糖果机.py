from atexit import register
from random import randrange
from threading import BoundedSemaphore,Lock,Thread
from time import ctime,sleep

lock = Lock()
MAX = 5
candtray = BoundedSemaphore(MAX)

def refill():
    #with lock:
    lock.acquire()
    print('Refilling candy...')
    try:
        candtray.release()
    except ValueError:
        print('full,skipping')
    else:
        print('OK')
    lock.release()

def buy():
    #with lock:
    lock.acquire()
    print('Buy candy...')
    if candtray.acquire(False):
        print('OK')
    else:
        print('empty,skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def main():
    print('staring at:{}'.format(ctime()))
    nloops = randrange(2,6)
    print('The candy mechine (full with {} bars)!'.format(MAX))
    Thread(target=consumer,args=(randrange(nloops,nloops+MAX+2),)).start()
    Thread(target=producer,args=(nloops,)).start()

@register
def _atexit():
    print('All Done at :{}'.format(ctime()))

if __name__=='__main__':
    main()