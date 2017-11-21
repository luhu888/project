#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Administrator'
import urllib
import re


def getHtml(url):    # 简单的爬取网页的爬虫
    page = urllib.urlopen(url)       # urllib.urlopen()方法用于打开一个URL地址。
    html = page.read()      # read()方法用于读取URL上的数据，向getHtml()函数传递一个网址，并把整个页面下载下来。执行程序就会把整个网页打印输出。
    print(html)
url = 'http://www.chuiyao.com/manhua/8162/372576.html?p=24'
getHtml(url)
# def getImage(html):   # 筛选页面中想要的数据
#     reg = r'src="(.+?\.jpg)" '
#     img = re.compile(reg)      # re.compile() 可以把正则表达式编译成一个正则表达式对象.
#     imglist = re.findall(img, html)    # re.findall() 方法读取html 中包含 imgre（正则表达式）的数据。
#     x = 0     # 将页面筛选的数据保存到本地
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl, '%s.png' % x)    # 这里的核心是用到了urllib.urlretrieve()方法，
#         x += 1                # 直接将远程数据下载到本地。
#     return imglist
# html = getHtml('http://www.chuiyao.com/manhua/8162/372576.html?p=24')
# print getImage(html)
