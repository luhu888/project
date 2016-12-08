#!/usr/bin/python
# -*- coding: UTF-8 -*-
from multiprocessing import Pool,Queue,Process
import os, time, random, threading

'''
def long_time_task(name):      # 多进程
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()     # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
    print 'All subprocesses done.'            # 调用close()之后就不能继续添加新的Process了
# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电
# 脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制


def write(q):     # 进程间的通信
    for value in['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
'''

'''
def loop():      # 多线程，任何进程都会默认开启一个主线程
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')  # 创建一个子线程
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
'''

import time, threading
'''
# 假定这是你的银行存款,这样运行会产生负值，
balance = 0


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()     # 双线程会抢夺执行权，单个线程中的+n-n运算会中断，会出现两次-n的情况
t2.start()     # 所以就要引入锁的概念
t1.join()
t2.join()
print balance
'''


balance = 0
lock = threading.Lock()


def run_thread(n):    # 加锁之后就会返回零
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance     # 全局变量
    balance = balance + n
    balance = balance - n
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance


















































































