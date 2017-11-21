#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 出现中文等非asc码字符时，必须添加此文件头，否则会报错
# 文件名：hello python.py
__author__ = 'Administrator'
print "hello python!"  # 第一个单行注释
"""
这是一个多行注释
这是一个多行注释
这是一个多行注释
重要的事说三遍
"""
# raw_input("\n\nPress the enter key to exit.")#等待用户输入，并按回车结束输入
import sys; x = 'haha';sys.stdout.write(x + '\n')   # 同一行可以显示多条语句，以分号隔开

# 变量赋值
counter = 100   # 赋值整型变量
miles = 1000.0   # 浮点型
name = "John"    # 字符串
print 'ount=', counter
print 'miles=', miles
print 'name=', name

# 多个变量赋值
a=b=c=23,"luhu",89;
d="hello"
del d,a, #删除对多个对象的引用
#print d,a;

#字符串
s="afdfajk lkvkk"
print s[0:4]
print s[2:]
print s[1]
print s*2#表示重复操作两次
print s[-5:-1]#-1为结尾，不能写成[-1:-5]
print s+"12"#不同数据之间不能用+相连


#列表
list1=['erer',343,'fdf','fde','er5f',345]
list2=[12,'dd']
print list1
print list1[0:2]
print list1[3:]
print list1[-3]
print list2*2
print list1+list2  #打印组合列表
print list1[2]
list1[2]=110
print list1[2]  # 更新列表中的数据

# 元组   与list列表类似，但元组中的数据是不可以更新的
tuple1 = (12, 'wer', 34, '232', 'feere')
tuple2 = (12, "ere")
print tuple1
print tuple1[1:3]
# tuple1[2]=100  是错的
print tuple1[2]


# 元字典     字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字
# 典是无序的对象集合。字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
# 类似于键值对
'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值
'''


# 运算符
r = 2
b = 3
c = r**b
print 'c=',c   # 幂运算
print 1 == 2  # 比较两个对象是否相等
if r > b:
    print 'r>b'
else:
    print 'r<=b'   # if和else要对齐，否则会报错

a = 21
b = 10
c = 0

c = a + b   # c = a + b 将 a + b 的运算结果赋值为 c
print "1 c 的值为：", c

c += a   # c += a 等效于 c = c + a
print "2 - c 的值为：", c

c *= a    # c *= a 等效于 c = c * a
print "3 - c 的值为：", c

c /= a    # c /= a 等效于 c = c / a
print "4 - c 的值为：", c

c = 2
c %= a     # c %= a 等效于 c = c % a
print "5 - c 的值为：", c

c **= a     # 等效于 c = c ** a
print "6 - c 的值为：", c

c //= a    # 取整除赋值运算符
print "7 - c 的值为：", c


a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b        # 12 = 0000 1100 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
print "1 - c 的值为：", c

c = a | b        # 61 = 0011 1101   按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
print "2 - c 的值为：", c

c = a ^ b       # 49 = 0011 0001   按位异或运算符：当两对应的二进位相异时，结果为1
print "3 - c 的值为：", c

c = ~a           # -61 = 1100 0011   按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1
print "4 - c 的值为：", c

c = a << 2     # 240 = 1111 0000   左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
print "5 - c 的值为：", c

c = a >> 2   # 15 = 0000 1111
print "6 - c 的值为：", c