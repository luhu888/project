#!/usr/bin/python
# -*- coding: UTF-8 -*-
# __author__ = 'Administrator'
'''def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
print my_abs('o')'''

'''
def enroll(name,gender,age=18,city='beijing'):
    print 'name:',name
    print 'gender:',gender
    print 'age:',age
    print 'city:',city
enroll('luhu','男',city='anhui')  #调用函数没有传入参数时，即使用默认值'''


'''
def calc(*numbers):      #可变参数，计算a2平方 + b2平方 + c2平方 + ……
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print calc(1,2,3,4,5,6)'''



'''#关键字参数
def person(name,age,**k):                  #**前为必选参数，**后的可变参数接收的只能是个字典
    print 'name:',name,'age:',age,'other:',k
k={'city':'beijing','job':'engineer'}
person('luhu',18,**k)'''

'''
#参数组合   参数定义的顺序必须是：必选参数，默认参数，可变参数，关键字参数
#            可变参数接收的是一个tuple元组或list，既可以直接传入，也可以先组装list或tuple，再通过*args传入
            #关键字参数接收的是一个dict字典，既可以直接传入，也可以先组装dict，再通过**kw传入
def func(a, b, c=0, *args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw
kw={'city':'beijing','job':'engineer'}
#args=(1,23,45,5)
args=[1,23,45,6,'luhu']
func(*args,**kw)'''



'''
#递归函数    使用递归函数要防止内存溢出
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print fact(1000)'''

def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
print fact(1000)






























