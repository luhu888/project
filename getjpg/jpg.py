#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests


for i in range(22, 23):
    url = "http://m.chuiyao.com/manhua/8162/372576.html?p="+str(i)
    with open('mh'+str(i)+'.jpg', 'wb') as f:
        f.write(requests.get(url).content)
    print(url)