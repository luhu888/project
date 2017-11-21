# -*- coding: utf-8 -*-
# __author__=luhu
import requests
url = 'http://api.feige.ee/SmsService/Send'
data = {'Pwd': '0b834ef51b5b83a8923c4ba96', 'Account': 'shiyuanqi', 'Content': '你好，欢迎光临诗远启！', 'Mobile': 15856691310,
        'SignId': 33985}
r = requests.post(url=url, data=data)
print r.status_code
print r.text
