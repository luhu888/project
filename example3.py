#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Administrator'    #m面向对象的编程思想
'''
class Student(object):
    def __init__(self,name,score):#__init__方法的第一个参数永远是self，表示创建的实例本身，因此，
                     # 在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
        self.__name=name    #把属性的名称前加两个下划线，就变成了一个私有变量，只有内部可以访问，外部不可以访问
        self.__score=score
       #  self.name=name
       #  self.score=score
    def print_score(self):
        print'%s:%s' %(self.__name,self.__score)
bart=Student('Bart simpson',77)
lisa = Student('Lisa simpson',99)
bart.print_score()
lisa.print_score()
try:
     print lisa.__name   #外部无法访问私有变量
except AttributeError,e:
     print '私有变量，外部无法访问'
'''

'''
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
''''''
在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，
 不能用__name__、__score__这样的变量名。''''''
lisa = Student('Lisa simpson',99)
print lisa.get_score()
print lisa.get_name()     #通过调用内部方法访问私有变量
lisa.set_score(100)
lisa.set_name("luhu")
print lisa.get_score()
print lisa.get_name()
'''

'''
# 继承
class Animal(object):
    def run(self):
        print '父类Animal is running.....'


class Dog(Animal):
    pass


dog = Dog()
dog.run()
Dog().run()

# 获取对象信息
print type(7890)
print type('hello')
print type(dog)

# Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入
import types
print type('uij') == types.StringType


# 最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType
print type(int) == type(str) == types.TypeType

a = Dog()
print isinstance(a, Dog)
print isinstance(a, Animal)

print dir('abc')  # 获取一个对象的所有属性和方法
'''
'''
from types import MethodType


class Student(object):   # 动态绑定
    pass


def set_age(self, age):
    self.age = age
Student.set_age = MethodType(set_age, None, Student)
''''''s = Student()
s.set_age = MethodType(set_age, s, Student)
s.set_age(25)
print s.age
s1 = Student()
s2 = Student()
s1.set_age(24)
s2.set_age(46)
print s1.age
print s2.age
'''

'''
class Student(object):    # 限制类的动态绑定 __slots__
    __slots__ = ('name', 'age')  # 限制类允许绑定的属性名称只有name和age
s = Student()
s.name = 'LuHu'
s.age = 89
# s.score = 99    # 会报错，slots不允许绑定score属性
print s.name
print s.age


class GrandStudent(Student):   # 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，
    pass                          # 对继承的子类是不起作用的
g = GrandStudent()
g.score = 89
g.name = 'Jane'
g.age = 98
'''

'''
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter            # 通过@property创建的@score. setter装饰器，
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!!!')
        if value < 0 or value > 100:
            raise ValueError('score must be 0~100!!!!')
        self._score = value
s = Student()
s.score = 78
print s.score
s.score = 99
print s.score
'''

'''
class Student(object):
    @property
    def birth(self):    # _birth：只是一个成员变量名，之所以前面加一个下划线是表示这个变量是私有的，
                        # 外部不能访问。（但实际是可以访问的，但你要明白它是私有的不能访问，全靠自己自觉）
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return 2016-self.__birth
s = Student()
s.birth = 2000
print s.birth
print s.age
# print s.__birth     # 非法的，外部不能直接访问__birth
'''

'''
class Student(object):    # 定制类
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name
print Student('LuHu')
print callable(Student)
'''

'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):      # __iter__使得一个类可以被for...in 循环
        return self    # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration();
        return self.a     # 返回下一个值

    def __getitem__(self, n):   # 使用__getitem__获取角标对应元素的值，使斐波拉契数列具有list属性
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, b + a     # 判断__getitem__()传入的参数是一个int还是slice切片，否则传入slice会报错
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            list1 = []
            for x in range(stop):
                if x >= start:
                    list1.append(a)
                a, b = b, a+b
            return list1
for n in Fib():
    print n
f = Fib()
print f[10]
print f[0:5]
'''

'''
class Student:
    def __init__(self):
        self.name = 'LuHu'

    def __getattr__(self, item):    # 动态添加属性
        if item == 'score':
            return 99
        elif item == 'age':   # 动态添加函数
            return lambda: 18
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)
s = Student()   # 注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
print s.name   # 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
print s.score
print s.age()
print s.acb
'''

'''
class Chain(object):

    def __init__(self,  path=''):
        self._path = path

    def __getattr__(self,  path):
        return Chain('%s/%s' % (self._path,  path))

    def __str__(self):
        return self._path

    def users(self, path):
        return Chain('%s/users/:%s' % (self._path, path))
print Chain().users('Michael').repos
'''

'''
import logging
               # 异常处理机制
try:
    print 'try...'
    r = 10/0
    print 'result', r
except ZeroDivisionError, e:
    print 'except:', e
    logging.exception(e)     # 打印错误日志
finally:
    print 'finally ...'
print 'end'
'''


import pdb


class NegError(StandardError):    # 自定义抛出错误
    pass


def neg(s):
    n = int(s)

    if n < 0:       # raise语句如果不带参数，就会把当前错误原样抛出
        raise NegError('invalid value: %s' % s)
    elif n == 0:
        raise NegError('modulo by zero')
    return 10/n
print neg(2)
pdb.set_trace()    # 运行到这里会自动暂停
assert neg(2) == 2, 'neg(2)应该等于5'   # 断言，如果结果前面的语句为false，后面代码就会出错，
                                         # 就意味着断言失败，就会抛出AssertionError






















