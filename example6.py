#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Administrator'
import os
'''
print os.name
print os.environ    # 操作系统中定义的环境变量，全部保存在os.environ这个dict中
print os.getenv('path')     # 获取某个环境变量的值


# 操作文件和目录
print os.path.abspath('.')    # 查看当前目录的绝对路径
os.path.join('C:\\Users\\Administrator\\PycharmProjects\\first project', 'LuHu')  # 创建目录
os.mkdir('C:\\Users\\Administrator\\PycharmProjects\\first project\\LuHu')   # 添加创建的目录

os.rename('test.txt', 'test.py')     # 文件重命名
'''

'''
# 列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]

# 列出当前文件夹下的指定文件名的文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
'''

'''
# 序列化和反序列化
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
# 我们先看看如何把Python对象变成一个JSON
import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)    # dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
print d

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把
# JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

# 有一点需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str。由于JSON标准规定JSON编码是UTF-8，
# 所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student("卢虎", 99, 99)
# print json.dumps(s)      # 直接把s对象序列化会报错
# 因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student
# 专门写一个转换函数，再把函数传进去即可：


# def student2dict(stu):
#         return {
#            'name': stu.name,
#            'age': stu.age,
#           'score': stu.score
#        }

# print json.dumps(s, default=student2dict)
# 这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON。
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print json.dumps(s, default=lambda obj: obj.__dict__)
# class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str, object_hook=dict2student)
# loads()方法首先转换出一个dict对象，然后传入的object_hook函数负责把dict转换为Student实例
'''


from multiprocessll import Process
import os


def run_proc(name):    # 多进程
    print 'Run child process %s (%s)...'%(name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' %os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()  # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
    p.join()    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print 'Process end.'














