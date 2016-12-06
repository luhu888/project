#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from PIL import Image
'a test module'   #任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'LuHu'


'''
import sys
print __name__
def test():
    args=sys.argv     #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少
                       # 有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args)==1:
        print 'hello,world!'
    elif len(args)==2:
        print 'hello,%s!' %args[1],args[0]
    else :
        print 'Too many arguments!'
print __name__     #__name__系统变量指示模块应如何被加载，他的值为"__main__"时表示当前模块是被直接执行。
    #               由于主程序代码无论模块是被导入还是直接被执行都会运行，所以我们需要一种方式在运行时
#                 检测该模块是被导入还是被直接执行。该方式也就是__name__系统变量。如果模块是被导入，
#                 __name__的值为模块名字；如果是被直接执行，__name__的值为"__main__"。

if __name__=='__main__':   #__name__是指示当前py文件调用方式的方法。如果它等于"__main__"
                           # 就表示是直接执行，如果不是，则用来被别的文件调用，这个时候if就为False，
                           # 那么它就不会执行最外层的代码了
    test()
print sys.argv
'''



'''    #导入第三方模块
im=Image.open('test.png')
print im.format,im.size,im.mode

im.thumbnail((200,120))
im.save('test1.jpg','JPEG')#生成图片缩略图
'''

'''
#Python提供了__future__模块，把下一个新版本的特性导入到当前版本，于是我
# 们就可以在当前版本中测试一些新版本的特性
#为了适应Python 3.x的新的字符串的表示方法，在2.7版本的代码中，
# 可以通过unicode_literals来使用Python 3.x的新的语法：
print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

print 10.0/3
'''



































































