#!/usr/bin/python
# -*- coding: utf-8 -*-
print'\\\n\\'
a=100
if a>100:
    print a
else:
    print -a
    print "I'm \"OK\""
a="abc"
b=a
a='cde'
print a, b

print u'中文'
print 'Hello,%s' % 'world'
print '%2d-%02d'%(3,1)
print '%.2f' % 3.1415926
print 'Age: %s. Gender: %s' % (25, True)# %s 占位符 就是字符串，万能占位符
name=raw_input(u"请输入你的名字：")
print u'%s你好，真是一个不错的名字，欢迎来到%s'%(name,u'法兰城')   #u'法兰城'表示将法兰城字符串改为用unicode编码
print 'grow rate: %d%%'%7
print 'abc'.decode('utf-8')