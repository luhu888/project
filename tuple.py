#!/usr/bin/python
#-*- coding: UTF-8 -*-

__author__ = 'Administrator'
'''
classmates=['ha','en','yu','wo','ta']
classmates.insert(1,'luhu')
classmates.append('ll')
classmates.append('ll')
classmates.append('ll')

classmates.pop(2)
classmates[3]='lll'
print classmates
list=[12,23,2,34,[1,2,3,4,5,],89,'ll']  #list里面可以嵌套list，可以看成二维数组，或多维数组




print list[4][2]
sum=0
for s in[1,2,3,4,5,6,7,8,9,0]:
    sum=sum+s
print sum

'''
x=1    #阶乘
for y in range(4):
    x=x*(y+1)
print x

'''
import math    #游戏的位移
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny
print move(100,100,60,math.pi/6)'''

'''
def square(x,n=2): #平方函数的扩展
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print square(7,3)
print square(7)
'''


















