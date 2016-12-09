#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Administrator'
import urllib
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def getHtml(url):    # 简单的爬取网页的爬虫
    page = urllib.urlopen(url)
    html = page.read()
    return html
gh = getHtml('http://www.jianshu.com/')
with open('C:\Users\Administrator\PycharmProjects\project\getjpg\\test5.html', 'wb') as f:
    f.write(gh)
import shutil