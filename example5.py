#!/usr/bin/python
# -*- coding: UTF-8 -*-       # 文件读写
__author__ = 'Administrator'
try:
    f = open('/Users/Administrator/PycharmProjects/first project/hh.txt', 'rb')
    print f.read().decode('gbk')   # 要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件
finally:
    if f:
        f.close()


d = open('/Users/Administrator/PycharmProjects/first project/test1.jpg', 'rb')  # 读取二进制文件
print d.read()
'''
如果每次都这么手动转换编码嫌麻烦（写程序怕麻烦是好事，不怕麻烦就会写出又长又难懂又没法维护的代码），
Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode'''
import codecs
with codecs.open('/Users/Administrator/PycharmProjects/first project/hh.txt', 'r', 'gbk') as k:
    print k.read()


# 写文件
g = open('/Users/Administrator/PycharmProjects/first project/hh.txt', 'w')
g.write('luhu hahah')
g.close()
'''
你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，
操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
'''
with codecs.open('/Users/Administrator/PycharmProjects/first project/hh.txt', 'w', 'gbk') as l:
    l.write('LuHu2 hahahaha!')








