#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import Frame, Label, Button
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
'''

'''
local_school = threading.local()   # 自动传递参数，使得不同线程共用同一个全局变量，
                                # 同时也消除了std对象在每层函数中的传递问题


def process_student():
    print 'Hello %s (in %s)' % (local_school.student, threading.current_thread().name)


def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('LuHu',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
'''


'''
# 正则表达式
s = 'ABC\\-001'
print s      # match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
import re
print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')  # 匹配
print re.match(r'^\d{3}\-\d{3,8}$', '010 12345')  # 不匹配返回None

test = '001-12545'
if re.match(r'\d{3}\-\d{3,8}$', test):
    print '匹配成功'
else:
    print '不匹配'

print re.split(r'[\s,;\']+', 'a ,b  \'c;;;   ,, d')   # 正则表达式切分字符
'''


'''
# 分组
import re
h = re.match(r'^(\d{3})-(\d{3,8})$', '010-15423')
print h.group(0)   # 正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
print h.group(1)
print h.group(2)
print h.groups()
'''

'''
[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。
'''

'''
import re   # 贪婪匹配，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print re.match(r'^(\d+?)(0*)$', '102300').groups()
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
'''

'''
from collections import namedtuple
point = namedtuple('Point', ['x', 'y'])
p = point(1, 2)
print p.x
print p.y
'''

'''
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
        '''
'''
from Tkinter import *         # 图形界面
import tkMessageBox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('hello python')
app.mainloop()
'''
import urllib
print dir(urllib.urlopen)    # 查看模块中的方法






















